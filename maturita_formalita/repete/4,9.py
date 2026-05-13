class Kniha():
    def __init__(self, titul, autor, rok):
        self.titul=titul
        self.autor=autor
        self.rok=rok

    def mezni_rok(self, mez):
        if self.rok < mez:
            print(f"{self.autor} - {self.titul} ({self.rok})")

kniha1 = Kniha("Konin Velký", "Jak osedlat koně 2", 1987)
kniha2 = Kniha("Petr P", "O životě v cracku", 2001)
kniha3 = Kniha("Michal Mazgal", "Kutilův návod na postavení akumulační stěny", 2024)
kniha4 = Kniha("Michal Mazgal", "Jak jsem přežil atentát: Vzkaz narkomanům", 2026)

knihovna = [kniha1, kniha2, kniha3, kniha4]
mezni_rok=int(input("Zadej mezní rok: "))
print("Starší knihy:")
for kniha in knihovna:
    kniha.mezni_rok(mezni_rok) 