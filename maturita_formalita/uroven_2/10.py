print("Načítám data z 'DATA.TXT'...")
try:
    with open("DATA.TXT", "r") as f:
        data_crude = (f.read()).split()
        data=[]
        for i in data_crude:
            num=float(i)
            data.append(num)
except:
    print("Nepodařilo se načíst :(")
minimum=int(input("Zadejte dolní mez A: "))
maximum=int(input("Zadejte horní mez B: "))
if minimum>maximum:
    temp=minimum
    minimum=maximum
    maximum=temp
print(f"Interval: <{minimum}; {maximum}>")
v_intervalu=[]
for num in data:
    if minimum <= num and num <= maximum:
        v_intervalu.append(num)
print(f"Čísla v intervalu: {v_intervalu}")
print(f"Počet: {len(v_intervalu)}")