while True:
    user_input=int(input("Zadej počet prvků: "))
    if user_input>0:
        length=user_input
        break
    else:
        print("Zadejte prosím kladnou celočíselnou hodnotu!")
nums=[]
for i in range(length):
    nums.append(int(input(f"Zadej číslo {i+1}/{length}: ")))
nums_reversed=[]
for i in range(length):
    nums_reversed.append("")
index=1
for num in nums:
    nums_reversed[length-index]=num
    index+=1
print(f"Původní: {nums}")
print(f"Obrácený: {nums_reversed}")