with open("vstup.txt", "r") as f:
    vstup = f.read()
print("Soubor načten: vstup.txt")
print(vstup)

k=int(input("Posun k: "))
vystup=""
ascii_list=[]
for znak in vstup:
    if 64 < ord(znak) < 91:
        pismeno_v_ascii=ord(znak)+k
        while pismeno_v_ascii > 90:
            pismeno_v_ascii=(pismeno_v_ascii-90)+64
        ascii_list.append(pismeno_v_ascii)
    elif 96 < ord(znak) < 123:
        pismeno_v_ascii=ord(znak)+k
        while pismeno_v_ascii > 122:
            pismeno_v_ascii=(pismeno_v_ascii-122)+96
        ascii_list.append(pismeno_v_ascii)
    else:
        ascii_list.append(ord(znak))

vystup=""
for znak in ascii_list:
    vystup+=(chr(znak))
print(vystup)
with open("sifra.txt", "w") as vysledek:
        vstup = vysledek.write(vystup)