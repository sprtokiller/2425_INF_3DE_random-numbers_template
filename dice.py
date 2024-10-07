import random

def roll_die(k):
    # Tvůj kód zde
    return random.randrange(1, k);

# Otestování funkce
print(roll_die(6))  # Simulace hodu 6-hranou kostkou
