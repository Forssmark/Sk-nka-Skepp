from slumpgenerator import Slumpande
from collections import Counter

def kontrollera_bräde(koordinater):
    """Returnerar False om något ligger utanför A1-H8"""
    for tal in koordinater:
        tiotal = tal // 10
        ental = tal % 10
        if not (1 <= tiotal <= 8 and 1 <= ental <= 8):
            return False
    return True

def test_slumpgenerator(antal_test=1000, meddelande_varje=100):
    statistik_antal_skepp = Counter()
    statistik_längder = Counter()
    orienteringar = Counter()
    fel_utanför = 0

    for i in range(1, antal_test + 1):
        s = Slumpande()
        s.slumpgenerator()
        
        for skepp in s.översättningslista_fulltsänkt:
            statistik_längder[len(skepp)] += 1

            # Orientering
            if all(skepp[j] - skepp[j-1] == 10 for j in range(1, len(skepp))):
                orienteringar['lodrätt'] += 1
            elif all(skepp[j] - skepp[j-1] == 1 for j in range(1, len(skepp))):
                orienteringar['vågrätt'] += 1
            else:
                orienteringar['annan'] += 1

            # Kontrollera utanför bräde
            if not kontrollera_bräde(skepp):
                fel_utanför += 1

        # Antal skepp per test
        statistik_antal_skepp[len(s.översättningslista_fulltsänkt)] += 1

        # Progressuppdatering
        if i % meddelande_varje == 0:
            print(f"{i} tester har körts...")

    # Slutrapport
    print("\n=======================================")
    print(f"✅ Testade {antal_test} gånger färdigt")
    print("=======================================\n")

    print("Antal skepp per test:")
    for antal, frekvens in sorted(statistik_antal_skepp.items()):
        print(f"  {antal} skepp: {frekvens} gånger")

    print("\nSkeppslängder:")
    for längd, frekvens in sorted(statistik_längder.items()):
        print(f"  Längd {längd}: {frekvens} gånger")

    print("\nOrienteringar:")
    for ori, frekvens in orienteringar.items():
        print(f"  {ori}: {frekvens} gånger")

    if fel_utanför:
        print(f"\n❌ Antal skepp med koordinater utanför brädet: {fel_utanför}")
    else:
        print("\nAlla koordinater ligger inom A1-H8 ✅")

# Kör testet
test_slumpgenerator(1000000, meddelande_varje=100)
