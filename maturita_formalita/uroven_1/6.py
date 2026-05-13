num1=float(input("Zadej první číslo: "))
num2=float(input("Zadej druhé číslo: "))
print(f"Součet: {num1+num2}")
print(f"Součet: {num1-num2}")
print(f"Součet: {num1*num2}")
if num2 == 0:
    print("Není možné dělit nulou!")
else:
    print(f"Součet: {num1/num2}")