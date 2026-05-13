def minimum(seznam):
    nejmensi=seznam[0]
    for num in nums:
        if num<nejmensi:
            nejmensi=num
    return nejmensi

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

print(f"Minimum: {minimum(nums)}")