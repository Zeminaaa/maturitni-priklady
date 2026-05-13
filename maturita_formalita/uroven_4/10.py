slovnik={'Adam': 42000, 'Bára': 47000, 'Cyril': 47000, 'Dana': 39500}
max_plat=[0,"name"]
for person in slovnik:
    if slovnik[person]>max_plat[0]:
        max_plat=[slovnik[person]]
        max_plat.append(person)
    elif slovnik[person]==max_plat[0]:
        max_plat.append(person)
print(f"Nejvyšší mzda: {max_plat[0]}")
print(f"Zaměstnanci s nejvyšší mzdou: {", ".join(max_plat[1:])}")