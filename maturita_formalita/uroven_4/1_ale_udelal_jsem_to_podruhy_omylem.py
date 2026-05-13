slovnik={}
num_of_students=int(input("Počet studentů: "))
for student in range(num_of_students):
    name=input(f"Jméno studenta {student+1}/{num_of_students}: ")
    marks=[]
    num_of_marks=int(input(f"Počet známek pro {name}: "))
    for mark in range(num_of_marks):
        marks.append(int(input(f"Zadej známku {mark+1}/{num_of_marks}: ")))
    slovnik[name]=marks

print("Průměry:")
averages=[]
for student in slovnik:
    marks=slovnik[student]
    average=round(sum(marks)/len(marks), 2)
    print(f"{student}: {average}")
    averages.append(average)

print(f"Třídní průměr: {round(sum(averages)/len(averages), 2)}")