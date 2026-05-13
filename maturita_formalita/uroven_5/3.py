validity=True
vstup_list=[]
for znak in str(input("Zadej rodné číslo: ")):
    vstup_list.append(znak)
if vstup_list[6]=="/":
    vstup_list.pop(6)
if len(vstup_list)!=10:
    validity=False

rok=int(vstup_list[0]+vstup_list[1])
if rok>26:
    rok+=1900
else:
    rok+=2000

mesic=int(vstup_list[2])
if mesic>4:
    mesic-=5
if mesic>1:
    mesic-=2
mesic=str(mesic)+vstup_list[3]

den=vstup_list[4]+vstup_list[5]

datum_narozeni=(den+"."+mesic+"."+str(rok))

vstup_list=list(map(int, vstup_list))

if validity:
    gender="muž"
    if vstup_list[2]>4:
        gender="žena"

    rc=0
    index=9
    for cislo in vstup_list:
        rc+=int(cislo)*(10**index)
        index-=1
    if rc%11!=0:
        validity=False

if validity==False:
    print("Platné RČ: NE")
else:
    print("Platné RČ: ANO")
    print(f"Datum narození: {datum_narozeni}")
    print(f"Pohlaví: {gender}")