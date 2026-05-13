slovnik={'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
print(f"Vstup: {slovnik}")
for polozka in slovnik:
    nums=slovnik[polozka]
    odd_nums=[]
    for num in nums:
        if num%2==0:
            odd_nums.append(num)
    slovnik[polozka]=odd_nums
print(f"Výstup: {slovnik}")