def frekvence_slov(text):
    text = text.lower()
    pocet_slov = {}
    temp = ""
    konina = [" ", ",", "."]
    
    for pismeno in text:
        if pismeno not in konina:
            temp += pismeno
        else:
            if temp != "":
                if temp in pocet_slov:
                    pocet_slov[temp] += 1
                else:
                    pocet_slov[temp] = 1
            temp = ""

    if temp != "":
        if temp in pocet_slov:
            pocet_slov[temp] += 1
        else:
            pocet_slov[temp] = 1
            
    return pocet_slov

vstup = input("Zadej větu: ")
vysledek = frekvence_slov(vstup)
serazena_slova = sorted(vysledek)

for slovo in serazena_slova:
    print(f"{slovo}: {vysledek[slovo]}")