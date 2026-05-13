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
print(f"Průměr: {sum(nums)/length}")
bigger_than_average=[]
for num in nums:
    if num>sum(nums)/length:
        bigger_than_average.append(num)
print(f"Hodnoty větší než průměr: {bigger_than_average}")