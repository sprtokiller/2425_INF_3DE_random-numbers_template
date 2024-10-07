import random

def roll_die(k):
    return random.randint(1, k)

# Otestování funkceg
print(roll_die(6))  # Simulace hodu 6-hranou kostkou
