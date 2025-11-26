class Highscore_räknare:
    """Hanterar highscore för ett spel
        Attribut:
        -Miss (int): håller koll på antal missade skott
        -Träff (int): håller koll på antal träffade skepp
        
        Metoder:
        -räknare(): Ökar antalet missar.
        -räknare_träff(): Ökar antalet träffar.
        -träffsäkerhet(): Procentuellt träffsäkerhet.
        -highscore(): Uppdaterar listan om krav uppnåtts.
       """
    def __init__(self):
        """Initierar highscore räknaren¨

           Attribut:
           -self.miss antal missade skott
           -self.träff antal träffade skepp
           """
        self.miss=0
        self.träff=0


    def highscore(self):
        """Denna laddar in Scoreboard.txt lägger till nya vinnare sorterar om och laddar upp en sparad upplaga."""

        with open("Scoreboard.txt", "r" ,encoding= "utf-8")as fil:  #Läser in filen
            lista = [rad.strip() for rad in fil]     
            rad_med_minsta_poäng=min(lista, key=poäng_från_rad)
            minsta_poäng=poäng_från_rad(rad_med_minsta_poäng)
            ny_poäng=self.träffsäkerhet()
            if ny_poäng>minsta_poäng:                                       #Jämför tidigare vinnare med ny för att se vem som är bäst
                lista.remove(rad_med_minsta_poäng)
                namn=input("Grattis! du har hamnat i topp 10! \nVad heter du? ")
                lista.append(f"{ny_poäng}% {namn}")
                lista.sort(key=poäng_från_rad, reverse=True)
                with open("Scoreboard.txt", "w", encoding="utf-8") as f:    #Laddar upp filen
                    for rad in lista:
                        f.write(rad + "\n")
                for rad in lista:
                    print(rad)
    


    def räknare(self):
        """Räknar missar i heltal"""
        self.miss+=1



    def räknare_träff(self):
        """Räknar träffar i heltal"""
        self.träff+=1
    

    
    def träffsäkerhet(self):
        """Beräknar vad träffsäkerheten är och returnerar procentuellt 0%-100%"""
        if self.miss==0:
            return 100
        return (self.träff/(self.träff+self.miss))*100



def poäng_från_rad(rad):
    """Extraherar talet före i Highscore listan för varje spelare returnerar 0-100"""
    return float(rad.split("%")[0])