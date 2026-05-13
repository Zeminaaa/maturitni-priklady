def bin_na_dec(s):
    num2=[]
    for i in str(s):
        num2.append(i)
    num2.reverse()
    index=0
    num10=0
    print(num2)
    for char in num2:
        if char=="1":
            num10+=2**index
        index+=1
    return num10

while True:
    s = input("Zadej číslo ve dvojkové: ")
    je_validni = True
    
    for znak in s:
        if znak not in ("0","1"): 
            je_validni = False
            break
    if je_validni and len(s)>0:
            vysledek = bin_na_dec(s)
            print(f"Desítkově: {vysledek}")
            break
    else:
        print("Chyba: Zadej pouze nuly a jedničky!")   