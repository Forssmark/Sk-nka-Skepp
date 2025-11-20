import random
class Slumpande:
    def __init__(self):
        self.skicka_lista=[]
        self.skicka_lista_fullsänkt=[]
        self.översättningslista=[]
        self.översättningslista_fulltsänkt=[]
        self.temporärlista=[]
    def antal(self):
        antal=random.randrange(1,5) # 1-4 skepp
        return antal
    def längd(self):
        längd=random.randrange(0,5) # 0-4 längd
        return längd
    def orgentering(self):
        """Om orgentering ger 1 blir skeppet lodrätt om orgentering blir 2 blir skeppet vågrätt"""
        riktning=random.randrange(1,3)
        if riktning==1: return "lodrätt"
        else: return "vågrätt"
    def slump_koordinat(self):
        bokstav=random.randrange(1,9)
        siffra=random.randrange(1,9)
        return bokstav*10+siffra
    def granskning_inom_bräde(self):
        for tal in self.temporärlista:
            tiotal=tal // 10
            ental=tal % 10
            if tiotal<1 or tiotal>8 or ental<1 or ental>8:
                return False
        return True
    def granskning_närhet(self):
        for tal in self.temporärlista:
            närliggande={tal+1, tal-1, tal+10, tal-10, tal-11, tal+11, tal-9, tal+9}

            if any(x in self.översättningslista for x in närliggande):
                return False
        return True
    def översättning(self, lista, extra=False):
        if extra:
            for sublista in lista:
                temp_för_lista_i_lista=[]
                for tal in sublista:
                    tiotal=tal // 10
                    ental=tal % 10
                    bokstav=chr(ord("A") + tiotal-1)
                    färdig_koordinat=f"{bokstav}{ental}"
                    temp_för_lista_i_lista.append(färdig_koordinat)
                    self.skicka_lista_fullsänkt.append(temp_för_lista_i_lista)
        else:
            for tal in lista:
                tiotal=tal // 10
                ental=tal % 10
                bokstav=chr(ord("A") + tiotal-1)
                färdig_koordinat=f"{bokstav}{ental}"
                self.skicka_lista.append(färdig_koordinat)

    def slumpgenerator(self):
        antal=self.antal()
        for _ in range(antal):
            while True:
                längd=self.längd()
                start_koordinad=self.slump_koordinat()
                self.temporärlista.append(start_koordinad)
                orgentering=self.orgentering()
                if orgentering=="lodrätt":
                    for i in range(1, längd+1):
                        self.temporärlista.append(start_koordinad + i)
                elif orgentering=="vågrätt":
                    for i in range(1, längd+1):
                        self.temporärlista.append(start_koordinad + i*10)
                else:
                    continue
                granskning=self.granskning_inom_bräde()
                if granskning==True:
                    if any(x in self.temporärlista for x in self.översättningslista):
                        self.temporärlista.clear()
                        continue
                    if not self.granskning_närhet():
                        self.temporärlista.clear()
                        continue
                    self.översättningslista_fulltsänkt.append(self.temporärlista.copy())
                    self.översättningslista.extend(self.temporärlista)
                    self.temporärlista.clear()
                    break
                elif granskning==False:
                    self.temporärlista.clear()
                    continue
                else:
                    continue
        self.översättning(self.översättningslista_fulltsänkt, extra=True)
        self.översättning(self.översättningslista)
        return self.skicka_lista, self.skicka_lista_fullsänkt