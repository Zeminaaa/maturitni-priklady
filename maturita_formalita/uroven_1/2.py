nums=[]
for num in range(3):
    num=int(input("Zadejte číslo: "))
    nums.append(num)
nums.sort()
if nums[2]==nums[1]==nums[0]:
    print(f"největší čísla jsou {nums[2]}, {nums[1]} a {nums[0]}")
elif nums[2]==nums[1]:
    print(f"největší čísla jsou {nums[2]} a {nums[1]}")
else:
    print(f"největší číslo je {nums[2]}")