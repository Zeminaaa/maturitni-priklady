class Auto():
    def __init__(self, znacka, vykon_kw):
        self.znacka=znacka
        self.vykon_kw=vykon_kw
    def custom_print(self, nazev):
        print(f"{nazev}: {self.znacka}, {self.vykon_kw} kW")
autoA=Auto("Škoda", 85)
autoB=Auto("VW", 110)

autoA.custom_print("Auto A")
autoB.custom_print("Auto B")

if autoA.vykon_kw > autoB.vykon_kw:
    print(f"Výkonnější je: {autoA.znacka} ({autoA.vykon_kw} kW)")
elif autoB.vykon_kw > autoA.vykon_kw:
    print(f"Výkonnější je: {autoB.znacka} ({autoB.vykon_kw} kW)")
else:
    print("Obě auta mají stejný výkon.")