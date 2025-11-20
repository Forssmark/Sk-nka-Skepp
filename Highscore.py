class Highscore_räknare:
    def __init__(self):
        self.miss=0
        self.träff=0
    def highscore(self, extra=False):
        """denna måste hålla koll på highscoret samt sortera"""

        with open("Scoreboard.txt", "r" ,encoding= "utf-8")as fil:
            lista = [rad.strip() for rad in fil]
            lista.sort(key=poäng_från_rad, reverse=True)
        if extra:    
            rad_med_minsta_poäng=min(lista, key=poäng_från_rad)
            minsta_poäng=poäng_från_rad(rad_med_minsta_poäng)
            ny_poäng=self.träffsäkerhet()
            if ny_poäng>minsta_poäng:
                lista.remove(rad_med_minsta_poäng)
                namn=input("Grattis du har hamnat i topp 10! \nVad heter du? ")
                lista.append(f"{ny_poäng}% {namn}")
                with open("Scoreboard.txt", "w", encoding="utf-8") as f:
                    for rad in lista:
                        f.write(rad + "\n")
                for rad in lista:
                    print(rad)
    def räknare(self):
        self.miss+=1
    def räknare_träff(self):
        self.träff+=1
    def träffsäkerhet(self):
        if self.miss==0:
            return 100
        return (self.träff/(self.träff+self.miss))*100

def poäng_från_rad(rad):
    return float(rad.split("%")[0])