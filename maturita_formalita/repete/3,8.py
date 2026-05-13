def dec_na_bin(dec_num):
    index=0
    while dec_num >= (2**index):
        index += 1
    print(index)

    bin_num = 0
    for i in range(index+1):
        if dec_num >= (2**(index)):
            bin_num += 10**index
            dec_num -= (2**(index))
        index -= 1

    return bin_num

print(f"Dvojkově: {dec_na_bin(int(input("Zadej nezáporné celé číslo: ")))}")