import random

def flip_coin():
    x = random.randint(0,1)
    if x == 0:
        return "Heads"
    else: 
        return "Tails"

# Otestování funkce
result = flip_coin()
print(result)