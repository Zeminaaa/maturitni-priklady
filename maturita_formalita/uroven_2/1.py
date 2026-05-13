while True:
    user_input=int(input("Zadej počet prvků: "))
    if user_input>0:
        length=user_input
        break
    else:
        print("Zadejte prosím kladnou celočíselnou hodnotu!")
nums=[]
for i in range(length):
    nums.append(float(input(f"Zadej číslo {i+1}/{length}: ")))
total=0
for num in nums:
    total+=num
average=total/length
print(f"{average:.2f}")