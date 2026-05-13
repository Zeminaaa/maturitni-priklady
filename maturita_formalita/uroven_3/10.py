def kombinace(d):
    print(f"Data: {d}")
    seznam_vseho=list(d.values())
    pocet_seznamu=len(seznam_vseho)

    def vytvor_combo(index,aktualni_string):
        if index==pocet_seznamu:
            print(aktualni_string)
            return
        
        for znak in seznam_vseho[index]:
            vytvor_combo(index+1, aktualni_string + znak)
    
    vytvor_combo(0,"")

DATA={'1': ['a', 'b'], '2': ['c', 'd'], '3': ['x', 'z'], }
kombinace(DATA)