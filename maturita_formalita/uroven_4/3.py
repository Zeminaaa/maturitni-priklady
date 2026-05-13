vstup=[ {'Obilí': 90, 'Zelenina': 92}, {'Obilí': 89, 'Zelenina': 94}, {'Obilí': 92, 'Zelenina': 88} ]
klic=input("Klíč: ")
vystup=[]
for slovnik in vstup:
    vystup.append(slovnik[klic])
print(vystup)