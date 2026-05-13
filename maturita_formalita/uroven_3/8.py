def dec_na_bin():
    while True:
        user_input=int(input("Zadej číslo v desítkové: "))
        if user_input>0:
            num10=user_input
            break
        else:
            print("Zadejte prosím kladnou celočíselnou hodnotu!")
    num2=[]
    zbytek=num10
    while zbytek>0:
            num2.append(zbytek%2)
            zbytek=zbytek//2

    return num2[::-1]

print(dec_na_bin())