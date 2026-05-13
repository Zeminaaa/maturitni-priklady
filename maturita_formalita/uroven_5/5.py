seznam_radku=[]
pocet_radku=0
preskocene_radky=0
with open("students.csv", "r") as i:
    for line in i:
        pocet_radku+=1
        temp=[]
        slovo=""
        for znak in line:
            if znak != ";":
                if znak != "\n":
                    slovo+=znak
            else:
                temp.append(slovo)
                slovo=""
        temp.append(slovo)
        if len(temp)==3:
            seznam_radku.append(temp)
        else:
            preskocene_radky+=1

slovnik={"jedna": 1,
        "dva": 2,
        "tri": 3,
        "ctyri": 4,
        "pet": 5}

index=0
destroy=[]
for radek in seznam_radku:
    try:
        radek[2]=int(radek[2])
    except:
        try:
            radek[2]=slovnik[radek[2]]
        except:
            destroy.append(index)
            preskocene_radky+=1
    index+=1

index=0
for cislo in destroy:
    cislo=cislo-index
    seznam_radku.pop(cislo)
    index+=1
print(f"Načteno: {pocet_radku} řádků ({preskocene_radky} přeskočeno kvůli chybě)")

slovnik_trid={}
for radek in seznam_radku:
    if radek[1] not in slovnik_trid:
        slovnik_trid[radek[1]]=[radek[2]]
    else:
        slovnik_trid[radek[1]].append(radek[2])

for trida in slovnik_trid:
    slovnik_trid[trida]=sum(slovnik_trid[trida])/len(slovnik_trid[trida])
    print(f"{trida}: {slovnik_trid[trida]}")

with open("report.csv", "w") as vysledek:
    for trida in slovnik_trid:
        kanal=vysledek.write(f"{trida};{slovnik_trid[trida]}\n")