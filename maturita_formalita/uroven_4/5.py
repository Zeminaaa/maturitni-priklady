vstup=[[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI '], [5, 'Zachary Simon', 'VII']]
slovnik={}
for name in vstup:
    id=name[0]
    jmeno=name[1]
    trida=name[2]
    slovnik[id]=[jmeno,trida]
print(f"Vstup: {vstup}")
print(f"Výstup: {slovnik}")