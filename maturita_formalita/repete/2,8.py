delka = int(input("Zadej počet čísel: "))
total = 0
for i in range(delka):
    num = float(input(f"Zadej číslo {i+1}/{delka}: "))
    total += num
print(f"Celkový součet je: {total}")
