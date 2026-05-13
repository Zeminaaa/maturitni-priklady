class Rectangle():
    def __init__(self, delka, sirka):
        self.delka=delka
        self.sirka=sirka

    def obsah(self):
        return self.sirka*self.delka
    
rectangle = Rectangle(15,10)
print(f"Délka: {rectangle.delka}, šířka: {rectangle.sirka}")
print(f"Obsah obdelníku: {rectangle.obsah()}")