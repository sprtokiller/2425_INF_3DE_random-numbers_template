import random

def flip_biased_coin(p):
    if p < 0:
        return ValueError
    else:
        return random.random() < p

# Otestování funkce
print(flip_biased_coin(0.7))  # Simulace hodu s 70% šancí na výhru
