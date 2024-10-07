import random

def flip_biased_coin(p):
    if random.randint(0, 10) < p * 10:
        return "Pana"
    else:
        return "Orel"

# Otestování funkce
print(flip_biased_coin(0.7))  # Simulace hodu s 70% šancí na výhru
