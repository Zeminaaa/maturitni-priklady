def matice_print(matice):
    for radek in matice:
        for num in radek:
            print(num, end=" ")
        print("")

r = int(input("Zadej počet řádků: "))
c = int(input("Zadej počet sloupců: "))

matice = []
for i in range(r):
    row = input(f"Zadej řádek {i+1}/{r} ({c} hodnot): ")
    matice.append(list(map(int, row.split())))
print("Původní matice:")
matice_print(matice)

transposed_matice = []
for i in range(c):
    transposed_matice.append([])
for row in matice:
    index = 0
    for znak in row:
        transposed_matice[index].append(znak)
        index += 1
print("Transponovaná:")
matice_print(transposed_matice)