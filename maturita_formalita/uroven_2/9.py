print("Načítám data z 'DATA.TXT'...")
try:
    with open("DATA.TXT", "r") as f:
        data_crude = (f.read()).split()
        data=[]
        for i in data_crude:
            num=float(i)
            data.append(num)
    print(f"Načteno: {data}")
except:
    print("Nepodařilo se načíst :(")
print(f"Průměr: {sum(data)/len(data)}")

print(f)