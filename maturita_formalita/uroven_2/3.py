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
for i in range(length):
    for j in range(length - 1 - i): 
        if nums[j] > nums[j+1]:
            temp = nums[j]
            nums[j] = nums[j+1]
            nums[j+1] = temp
print(f"Maximum: {nums[length-1]}")