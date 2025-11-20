#Har använt mig av chatgpt för att hitta metoder att komma vidare när jag fastnat!
 
from felhantering_sanka_skepp import Gilltigta_mål
import slumpgenerator
import Highscore
import sys
class Bräde:
    def __init__(self):
        
        slump_bräde = slumpgenerator.Slumpande()
        self.spelplan,self.spelplan_fullsänkt=slump_bräde.slumpgenerator()
        self.sänkta_fartyg=[]
        self.missade_fartyg=[]
        self.highscore_länkning=Highscore.Highscore_räknare()
    def kontroll(self):
        while True:
            skott_val=input("Vad vill du skjuta? ").upper()
            skott_granskning=Gilltigta_mål(skott_val)
            if skott_granskning==True:
                if skott_val in self.spelplan and skott_val not in self.sänkta_fartyg and skott_val not in self.missade_fartyg:
                    print("Träff! ")
                    return True , skott_val
                elif skott_val in self.sänkta_fartyg or skott_val in self.missade_fartyg:
                    print("Du har redan skjutigt där! ")
                    continue
                else:
                    print("Miss! ")
                    return False, skott_val
            elif skott_granskning==False:
                continue
   
   
   
    def skjuta(self):
         
        resultat, träff_eller_miss=self.kontroll()
        if resultat==True:    
            self.spelplan.remove(träff_eller_miss)
            self.sänkta_fartyg.append(träff_eller_miss)
            for innre_lista in self.spelplan_fullsänkt:
                if träff_eller_miss in innre_lista:
                    innre_lista.remove(träff_eller_miss)
                    break
            self.fullsänkt()
            self.highscore_länkning.räknare_träff()
            if len(self.spelplan)==0:
                self.rita_bräde(extra=True)
                print("Du har vunnit!!")
                self.highscore_länkning.highscore(extra=True)
                sys.exit()
        elif resultat==False:
            self.missade_fartyg.append(träff_eller_miss)
            self.highscore_länkning.räknare()
        self.rita_bräde()
            
    def rita_bräde(self,extra=False):
        self.missade_fartyg
        self.sänkta_fartyg
        self.spelplan
        bokstäver="ABCDEFGH"
        siffror="12345678"
        print("    "+"  ".join(siffror))
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
        while [] in self.spelplan_fullsänkt:
            self.spelplan_fullsänkt.remove([])
            for i in self.sänkta_fartyg:
                bokstav=i[0]
                siffra=int(i[1])
                bokstav_minus=chr(ord(bokstav) - 1)
                bokstav_plus=chr(ord(bokstav) + 1)
                siffra_minus=siffra-1
                siffra_plus=siffra+1
                self.missade_fartyg.extend([x for x in[f"{bokstav_minus}{siffra_minus}",f"{bokstav_minus}{siffra}",f"{bokstav_minus}{siffra_plus}",f"{bokstav}{siffra_minus}",f"{bokstav}{siffra_plus}",f"{bokstav_plus}{siffra_minus}",f"{bokstav_plus}{siffra}",f"{bokstav_plus}{siffra_plus}"]if x not in self.sänkta_fartyg]) 
                


def main():
    databas=Bräde()
    print(databas.spelplan)
    while True:
        meny_val=input("Vad vill du göra? \n Sjuta kanonkula [1] \n Fuska och titta på brädet [2] \n avsluta programmet [3]\n")
        if meny_val=="1":
            databas.skjuta()
        elif meny_val=="2":
            databas.rita_bräde(extra=True)
        elif meny_val=="3":
            print("Programmet Avslutar.....")
            databas.rita_bräde(extra=True)
            sys.exit() 
        else:
            print("Du måste ange ett heltal 1,2,3")
main()