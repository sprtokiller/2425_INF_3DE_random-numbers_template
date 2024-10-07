import random

def flip_biased_coin(p):
    # Tvůj kód zde
    coinflip = ["heads", "tails"];
    return random.choice(coinflip);

# Otestování funkce
print(flip_biased_coin(0.7))  # Simulace hodu s 70% šancí na výhru
