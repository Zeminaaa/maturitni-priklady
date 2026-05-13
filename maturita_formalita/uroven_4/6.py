import math
class Circle:
    def __init__(self, radius):
        self.radius=radius
    
    def obvod(self):

        return round(math.pi*2*self.radius, 2)
    
circle=Circle(67)
print(circle.obvod())