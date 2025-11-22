# dash_sanka_skepp.py
from dash import Dash, html, Output, Input, State
import dash
import dash_bootstrap_components as dbc
from sänka_skepp_main import Bräde  # Importera din Bräde-klass här

# Skapa app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
spel = Bräde()  # vår spelklass

# Skapa 8x8-grid
bokstäver = "ABCDEFGH"
siffror = "12345678"

def skapa_grid():
    grid = []
    for bokstav in bokstäver:
        rad = []
        for siffra in siffror:
            ruta = bokstav + siffra
            btn = dbc.Button(
                "",
                id=f"btn-{ruta}",
                n_clicks=0,
                style={"width": "50px", "height": "50px", "margin": "2px"},
            )
            rad.append(btn)
        grid.append(html.Div(rad, style={"display": "flex"}))
    return grid

app.layout = html.Div([
    html.H2("Sänka Skepp"),
    html.Div(id="grid-container", children=skapa_grid()),
    html.Br(),
    html.Div(id="resultat"),
    html.Br(),
    dbc.Button("Visa hela brädet (fuska)", id="visa-brade", n_clicks=0),
])

# Callback för att hantera skott
@app.callback(
    Output("resultat", "children"),
    [Input(f"btn-{b}{s}", "n_clicks") for b in bokstäver for s in siffror],
    State("resultat", "children")
)
def skjut(*args):
    ctx = dash.callback_context
    if not ctx.triggered:
        return ""

    knapp_id = ctx.triggered[0]["prop_id"].split(".")[0]  # tex btn-A1
    ruta = knapp_id.replace("btn-", "")

    # Kolla om man redan skjutit där
    if ruta in spel.sänkta_fartyg or ruta in spel.missade_fartyg:
        return f"Du har redan skjutit på {ruta}!"

    # Skjut
    resultat, _ = (ruta in spel.spelplan), ruta
    if resultat:
        spel.spelplan.remove(ruta)
        spel.sänkta_fartyg.append(ruta)
        text = f"Träff på {ruta}!"
    else:
        spel.missade_fartyg.append(ruta)
        text = f"Miss på {ruta}!"

    # Kontrollera vinst
    if len(spel.spelplan) == 0:
        text += " Du har vunnit!!"

    return text

# Callback för fuska-knappen
@app.callback(
    [Output(f"btn-{b}{s}", "style") for b in bokstäver for s in siffror],
    Input("visa-brade", "n_clicks")
)
def visa_brade(n):
    styles = []
    for bokstav in bokstäver:
        for siffra in siffror:
            ruta = bokstav + siffra
            base_style = {"width": "50px", "height": "50px", "margin": "2px"}
            if ruta in spel.sänkta_fartyg:
                base_style["backgroundColor"] = "#f55"  # rött = träff
            elif ruta in spel.missade_fartyg:
                base_style["backgroundColor"] = "#55f"  # blått = miss
            elif n > 0 and ruta in spel.spelplan:
                base_style["backgroundColor"] = "#aaa"  # fuska = visa plats
            styles.append(base_style)
    return styles

if __name__ == "__main__":
    app.run(debug=True)
