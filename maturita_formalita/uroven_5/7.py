import random
slova=[]
with open("CPJ.txt", "r") as soubor:
    for line in soubor:
        slovo=""
        for znak in line:
            if znak != "\n":
                slovo+=znak
        slova.append(slovo)

current_slovo=slova[random.randint(0,len(slova)-1)]

slovo_list=[]
for pismeno in current_slovo:
    slovo_list.append(pismeno)
#print(slovo_list)

guess=[]
for i in range(len(slovo_list)):
    guess.append("_")
#print(guess)

pokusy=5
wrong=[]
win=False

while pokusy>0 and win != True:
    num_of_blank=0
    for znak in guess:
        if znak=="_":
            num_of_blank+=1
        print(znak,end=" ")
    print("|",end=" ")
    print(f"špatné: {wrong}",end=" | ")
    print(f"zbývá: {pokusy}")

    if num_of_blank==0:
        win=True
        break
    
    tip=str(input("Tipni písmeno: "))

    index=0
    spravne_pozice=[]
    for pismeno in slovo_list:
        if pismeno==tip:
            spravne_pozice.append(index)
        index+=1

    for pozice in spravne_pozice:
        guess[pozice]=tip
    if len(spravne_pozice)==0:
        pokusy-=1
        wrong.append(tip)

if win:
    print(f"Gratuluji, uhlodl jsi slovo: {current_slovo}")
else:
    print(f"Je mi líto, prohrál jsi. Slovo bylo: {current_slovo}")