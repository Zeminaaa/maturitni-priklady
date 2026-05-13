class Kniha():
    def __init__(self, nazev, autor, rok):
        self.nazev=nazev
        self.autor=autor
        self.rok=rok
    
    def mezni_rok(self, mezni_rok):
        if self.rok<mezni_rok:
            print(f"{self.autor} - {self.nazev} ({self.rok})")

kniha1=Kniha("Bobeš", "Karel Hynek Macha", 1987)
kniha2=Kniha("Kokeš", "Karel Hynek Zapachal", 1787)
kniha3=Kniha("Krkavec", "EDagr Poe", 1987)
kniha4=Kniha("Prvok, Šampon, Tečka a Karel", "Patrik Hartl", 2007)

knihovna=[kniha1,kniha2,kniha3,kniha4]
mez=int(input("Zadej mezní rok: "))
print("Starší knihy:")
for kniha in knihovna:
    kniha.mezni_rok(mez)