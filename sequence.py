import random

def generate_sequence(n):
    for _ in range(n):
        print(random.randint(0, 100))
    return

# Otestování funkce
generate_sequence(10)  # Vygeneruje 10 náhodných čísel
