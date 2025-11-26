#Har använt mig av chatgpt för att hitta metoder att komma vidare när jag fastnat! Samt hitta och korrigera stavfel.
 
from felhantering_sanka_skepp import Giltiga_mål
import slumpgenerator
import Highscore
import sys
class Bräde:
    """Hanterar brädet för spelet.
        Attribut:
        -spelplan (lista): Innehåller koordinater för skeppen.
        -spelplan_fullsänkt (lista): Innehåller en lista med skepp där varje skepp är en lista av koordinater
        -sänkta_fartyg (lista): Träffade koordinater
        -missade_fartyg (lista): Tidigare skjutna och missade koordinater 
        -highscore_länkning: Objekt som hanterar träffprocenten
        
        
        Metoder:
        -kontroll: Tar in och validerar angivna koordinater
        -skjuta: Utför ett skott och uppdatera spelplanens listor
        -rita_bräde: Skriver ut spelplanen
        -fullsänkt: Kontrollerar när användaren sänkt ett helt skepp och markerar runt om 
    """
    def __init__(self):   
        """Initierar ett nytt objekt av spelplanen och skapar en slumpmässigt bräde
        
        Attribut:
        -spelplan(lista): Lista över fartygens koordinater
        -spelplan_fullsänkt(lista): Lista över alla hela fartyg
        -sänkta_fartyg(lista): Lista över sänkta fartygs koordinater
        -missade_fartyg(lista): Lista över missade skott
        -highscore_länkning: Objekt för att hantera highscore
        """ 
        slump_bräde = slumpgenerator.Slumpande()
        self.spelplan,self.spelplan_fullsänkt=slump_bräde.slumpgenerator()
        self.sänkta_fartyg=[]
        self.missade_fartyg=[]
        self.highscore_länkning=Highscore.Highscore_räknare()
    
    def kontroll(self):
        """Denna metod tittar om angivna koordinaten redan angetts eller är utanför spelplanen eller om man träffar/missar
           Returns:
           tuple: (True/False, koordinat)
        """
        while True:
            skott_val=input("Vad vill du skjuta? ").upper()
            skott_granskning=Giltiga_mål(skott_val)       #Tittar om koordinaterna är inom A1-H8
            
            if skott_granskning is True:
                if skott_val in self.spelplan and skott_val not in self.sänkta_fartyg and skott_val not in self.missade_fartyg:
                    print("Träff! ")
                    return True , skott_val
                
                elif skott_val in self.sänkta_fartyg or skott_val in self.missade_fartyg:
                    print("Du har redan skjutit där! ")
                    continue
                
                else:
                    print("Miss! ")
                    return False, skott_val
            
            elif skott_granskning is False:
                continue
   
   

    def skjuta(self):
        """
        Hanterar ett skott:
        - validerar skottet
        - uppdaterar träffar och missar
        - kontrollerar om spelet är vunnet
        - ritar upp brädet efter varje skott
        """

        resultat, träff_eller_miss=self.kontroll()
        
        if resultat==True:    
            self.spelplan.remove(träff_eller_miss)
            self.sänkta_fartyg.append(träff_eller_miss)
            
            for inre_lista in self.spelplan_fullsänkt:
                if träff_eller_miss in inre_lista:
                    i=inre_lista.index(träff_eller_miss)
                    inre_lista[i]=f"{träff_eller_miss}:"
                    break
            
            self.fullsänkt()
            self.highscore_länkning.räknare_träff()
            
            if len(self.spelplan)==0:               #Här tittas de om spelet är klart genom att alla skepp är sänkta
                self.rita_bräde(extra=True)
                print("Du har vunnit!!")
                self.highscore_länkning.highscore()
                sys.exit()
        
        elif resultat==False:
            self.missade_fartyg.append(träff_eller_miss)
            self.highscore_länkning.räknare()
        
        self.rita_bräde()


    def rita_bräde(self,extra=False):
        """Ritar ut brädet med eller utan skeppens position beroende på om extra=True
            
           Argument:
           extra (bool): Om True visas skeppens koordinater        
        """
        bokstäver="ABCDEFGH"
        siffror="12345678"
       
        print("    "+"  ".join(siffror))    #Här och nedanför skrivs hela brädet ut i konsolen.
        
        for bokstav in bokstäver:           
            rad=[bokstav.upper()+" "]
           
            for siffra in siffror:
                ruta=bokstav+siffra
                
                if ruta in self.missade_fartyg:
                    rad.append("O")
                elif ruta in self.sänkta_fartyg:
                    rad.append("#")
                elif extra and ruta in self.spelplan:
                    rad.append("X")
                else:
                    rad.append(".")

            print("  ".join(rad))

    def fullsänkt(self):
        """Denna metod kontrollerar efter varje skott om ett skepp är sänkt och i så fall markerar runt om som omöjliga positioner för skepp att ta"""
        for inre_lista_i_fullsänkt in self.spelplan_fullsänkt:   
            
            if all(":" in x for x in inre_lista_i_fullsänkt):  #tittar vilket skepp som är fullt sänkt
                for i in range(len(inre_lista_i_fullsänkt)):
                    inre_lista_i_fullsänkt[i]=inre_lista_i_fullsänkt[i].replace(":","")   
                
                for i in inre_lista_i_fullsänkt:               #hanterar vilka koordinater som skeppet är samt vad delar av koordinaterna runt om kring är siffra ± 1 , bokstav ± 1
                    bokstav=i[0]                                
                    siffra=int(i[1])
                    bokstav_minus=chr(ord(bokstav) - 1)
                    bokstav_plus=chr(ord(bokstav) + 1)
                    siffra_minus=siffra-1
                    siffra_plus=siffra+1
                    
                    self.missade_fartyg.extend([x for x in[
                        f"{bokstav_minus}{siffra_minus}",       #lista för omkringliggande koordinater till sänktskepp
                        f"{bokstav_minus}{siffra}",              
                        f"{bokstav_minus}{siffra_plus}",
                        f"{bokstav}{siffra_minus}",
                        f"{bokstav}{siffra_plus}",
                        f"{bokstav_plus}{siffra_minus}",
                        f"{bokstav_plus}{siffra}",
                        f"{bokstav_plus}{siffra_plus}"
                        ]if x not in self.sänkta_fartyg]) 
                    
                inre_lista_i_fullsänkt=[]


def main():
    """Hanterar logiken i spelet om man 
       [1] Skjuta 
       [2] Fuska 
       [3] Stänga av programmet
    """
    databas=Bräde()     #införskaffar tillgång till en instans av klassen.
    
    while True:
        meny_val=input("Vad vill du göra? \n Skjuta kanonkula [1] \n Fuska och titta på brädet [2] \n avsluta programmet [3]\n")
        
        if meny_val=="1":
            databas.skjuta()
        elif meny_val=="2":
            databas.rita_bräde(extra=True)
        elif meny_val=="3":
            print("Programmet Avslutar.....")
            databas.rita_bräde(extra=True)
            sys.exit() 
        else:
            print("Du måste ange ett heltal 1,2 eller 3")

main()