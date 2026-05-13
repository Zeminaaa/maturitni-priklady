def je_prvocislo(x):
    check=2
    for i in range(x-2):
        if x%check==0:
            return False
        else:
            check+=1
    return True
vstup=(int(input("Zadej číslo: ")))
if je_prvocislo(vstup):
    print(f"{vstup} je prvočíslo.")
else:
    print(f"{vstup} není prvočíslo.")