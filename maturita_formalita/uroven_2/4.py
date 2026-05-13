while True:
    user_input=int(input("Zadej délku prvního seznamu: "))
    if user_input>0:
        length=user_input
        break
    else:
        print("Zadejte prosím kladnou celočíselnou hodnotu!")
nums1=[]
for i in range(length):
    nums1.append(int(input(f"Zadej číslo {i+1}/{length}: ")))
while True:
    user_input=int(input("Zadej délku druhého seznamu: "))
    if user_input>0:
        length=user_input
        break
    else:
        print("Zadejte prosím kladnou celočíselnou hodnotu!")
nums2=[]
for i in range(length):
    nums2.append(int(input(f"Zadej číslo {i+1}/{length}: ")))

nums_combined=[]
index=0
for i in range(len(nums1)):
    nums_combined.append(nums1[index])
    index+=1
index=0
for i in range(len(nums2)):
    nums_combined.append(nums2[index])
    index+=1

print(f"První: {nums1}")
print(f"Druhý: {nums2}")
print(f"Spojený: {nums_combined}")