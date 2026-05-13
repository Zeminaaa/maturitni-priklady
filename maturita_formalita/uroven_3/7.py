rows=int(input("Zadej počet řádků: "))
columns=int(input("Zadej počet sloupců: "))
p=[]
index=1
for row in range(rows):
    vstup=input(f"Zadej řádek {index}/{rows} ({columns} hodnot): ")
    p.append([int(x) for x in vstup.split()])
    index+=1

def matice_print(matice):
    for row in matice:
        for num in row:
            print(num, end=" ")
        print("")

print("Původní matice: ")
matice_print(p)

def transpose(mat):
    transposed_mat=[]
    index=0
    temp=[]
    for i in range(columns):
        for row in mat:
            temp.append(row[index])
        transposed_mat.append(temp)
        temp=[]
        index+=1
    return(transposed_mat)

print("Transponovaná:")
matice_print(transpose(p))