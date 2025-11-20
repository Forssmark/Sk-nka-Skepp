def Gilltigta_mål(skott):

    if len(skott)==2:
        if skott[0]in "ABCDEFGH" and skott[1] in "12345678":
            return True
        else:
            print("Du skjöt utanför spelplanen! ")
            return False
    else: 
        print("Du måste ha en bokstav följt av ett tal! ") 
        return False
        
        