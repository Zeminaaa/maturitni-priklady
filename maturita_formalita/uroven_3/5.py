def unikaty(vstup):
    znaky=[]
    for znak in vstup:
        if znak not in znaky:
            znaky.append(znak)
    return znaky
while True:
    user_input=int(input("Zadej počet prvků: "))
    if user_input>0:
        length=user_input
        break
    else:
        print("Zadejte prosím kladnou celočíselnou hodnotu!")
vstup=[]
for i in range(length):
    vstup.append(str(input(f"{i+1}/{length}: ")))
print(f"Unikátní:{unikaty(vstup)}")