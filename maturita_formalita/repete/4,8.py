class Auto():
    def __init__(self, znacka, vykon_kw, displayed_name):
        self.znacka = str(znacka)
        self.vykon_kw = int(vykon_kw)
        self.displayed_name = displayed_name

    def auto_print(self):
        print(f"{self.displayed_name}: {self.znacka}, {self.vykon_kw} kW")
    
    def check_vykon(car1, car2):
        winner = None
        if car1.vykon_kw > car2.vykon_kw:
            winner = car1
        elif car1.vykon_kw < car2.vykon_kw:
            winner = car2
        
        if winner==None:
            print("Obě auta jsou stejně výkonná")
        else:
            print(f"Výkonnější je: {winner.znacka} ({winner.vykon_kw})")

auto1 = Auto("Škoda", 100, "Auto A")
auto2 = Auto("VW", 150, "Auto B")

garaz = [auto1, auto2]
for auto in garaz:
    auto.auto_print()
Auto.check_vykon(auto1, auto2)