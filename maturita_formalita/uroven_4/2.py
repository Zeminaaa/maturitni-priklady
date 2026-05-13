text=input("Zadej text: ")
slovnik={}
for pismeno in text:
    if pismeno==" ":
        pismeno="''"
    if pismeno not in slovnik:
        slovnik[pismeno]=1
    else:
        slovnik[pismeno]=slovnik[pismeno]+1
slovnik=sorted(slovnik.items())
for polozka in slovnik:
    print(f"{polozka[0]}: {polozka[1]}")