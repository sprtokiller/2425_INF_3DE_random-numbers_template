import random

def flip_coin():
    # Tvůj kód zde
    coinflip = ["heads", "tails"];
    return random.choice(coinflip);

# Otestování funkce
print(flip_coin())
