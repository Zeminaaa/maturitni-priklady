slovnik={}
pocet_studentu=int(input("Počet studentů: "))
for student in range(pocet_studentu):
    jmeno = input(f"Jméno studenta {student+1}/{pocet_studentu}: ")
    znamky=[]
    pocet_znamek=int(input(f"Počet známek pro {jmeno}: "))
    for i in range(pocet_znamek):
        znamky.append(int(input(f"Zadej známku {i+1}/{pocet_znamek}: ")))
    slovnik[jmeno]=(round(sum(znamky)/len(znamky), ndigits=2))
print("Průměry:")
prumery=[]
for klic in slovnik:
    print(f"{klic}: ", end="")
    print(slovnik[klic])
    prumery.append(slovnik[klic])
print(f"Třídní průměr: {sum(prumery)/len(prumery)}")