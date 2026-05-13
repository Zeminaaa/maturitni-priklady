soubor="text.txt"
print(f"Soubor: {soubor}")
with open(soubor, "r") as i:
    vstup=i.read()
slova=[]
vety=0
oddelovace=[".","?","!"]
slovo=""
predchozi=None

for znak in vstup:
    if znak not in oddelovace and predchozi != "\n":
        if znak!=",":
            if znak==" " or znak == "\n":
                if slovo != "":
                    slova.append(slovo)
                slovo=""
            else:
                slovo+=(znak)
                predchozi=znak
    else:
        if predchozi not in oddelovace and predchozi != "\n":
            vety+=1
    predchozi=znak
slova.append(slovo)

seznam_delek=[]
for slovo in slova:
    seznam_delek.append(len(slovo))
prumerna_delka=sum(seznam_delek)/len(seznam_delek)

print(f"Věty: {vety}")
print(f"Slova: {len(slova)}")
print(f"Průměrná délka slova: {round(prumerna_delka, 2)}")