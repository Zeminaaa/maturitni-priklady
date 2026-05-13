prvni=input("První slovo/věta: ")
druhe=input("Druhé slovo/věta: ")
caps_ignore=False
if input("Ignorovat velikost pismen? (A/N): ")=="A":
    caps_ignore=True
if caps_ignore:
    prvni=prvni.lower()
    druhe=druhe.lower()

seznam_ignorovanych_znaku=[""," "]

def frekvence_slov(string):
    temp_slovnik={}
    for char in string:
        if char not in temp_slovnik and char not in seznam_ignorovanych_znaku:
            temp_slovnik[char]=1
        elif char in temp_slovnik:
            temp_slovnik[char]+=1
    return temp_slovnik

slovnik1=frekvence_slov(prvni)
slovnik2=frekvence_slov(druhe)

if slovnik1==slovnik2:
    anagramy="ANO"
else:
    anagramy="NE"
print(f"Jsou to anagramy: {anagramy}")