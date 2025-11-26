def Giltiga_mål(skott):
    """Kollar om skottet som kommer in är 2 i längd samt mellan A-H och 1-8"""

    if len(skott)==2:
        if skott[0]in "ABCDEFGH" and skott[1] in "12345678":
            return True
        else:
            print("Du skjöt utanför spelplanen! ")
            return False
    else: 
        print("Du måste ha en bokstav följt av en siffra! ") 
        return False
        
        