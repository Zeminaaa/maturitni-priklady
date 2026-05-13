text=input("Zadej text: ")
symbol=input("Zadje znak: ")
reps=0
for znak in text:
    if znak==symbol:
        reps+=1
print(f"Počet výskytů znaku '{symbol}': {reps}")