seznam_uctu=[]
seznam_operaci=[]
pocet_operaci=0
chybne_operace=0
with open("operations.txt", "r") as i:
    for line in i:
        temp=[]
        slovo=""
        for znak in line:
            if znak != ";":
                if znak != "\n":
                    slovo+=znak
            else:
                temp.append(slovo)
                slovo=""
        temp.append(slovo)
        if len(temp)==3:
            seznam_operaci.append(temp)
        else:
            chybne_operace+=1
        pocet_operaci+=1

class BankovniUcet():
    def __init__(self,majitel,zustatek):
        self.majitel=majitel
        self.zustatek=zustatek

    def vlozit(self,sum):
        self.zustatek+=sum

    def vybrat(self,sum):
        if self.zustatek>=sum:
            self.zustatek-=sum
        else:
            return False

    def zustatek(self):
        print(self.zustatek)
    
    def new_user(vstup):
        majitel=vstup[0]
        ucet=BankovniUcet(majitel,0)
        return ucet

for line in seznam_operaci:
    jmeno=line[0]
    operace=line[1]
    castka=int(line[2])

    aktivni_ucet=None
    for ucet in seznam_uctu:
        if ucet.majitel==jmeno:
            aktivni_ucet=ucet

    if aktivni_ucet is None:
        aktivni_ucet=BankovniUcet.new_user(line)
        seznam_uctu.append(aktivni_ucet)

    if operace=="VKLAD":
        aktivni_ucet.vlozit(castka)
    elif operace=="VYBER":
        if aktivni_ucet.vybrat(castka) == False:
            chybne_operace+=1
    
print(f"Načteny operace: {pocet_operaci}")
print(f"Chybných operací: {chybne_operace}")
print("Účty:")

seznam_uctu.sort(key=lambda x: x.majitel)
for ucet in seznam_uctu:
    print(f"{ucet.majitel}: {ucet.zustatek}")