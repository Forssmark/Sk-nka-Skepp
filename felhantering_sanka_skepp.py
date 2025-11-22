def Gilltigta_mål(skott):

    if len(skott)!=2:
        print("Du måste ha en bokstav följt av ett tal! ")
        return False

    if skott[0] < "A" and skott[0] > "I":
        print("Det första tecknet måste vara en bokstav mellan A-H!")
        return False

    if skott[1] < "0" and skott[1] >"8":
        print("Det andra tecknet måste vara en siffra mellan 1-8!")
        return False


    return True


