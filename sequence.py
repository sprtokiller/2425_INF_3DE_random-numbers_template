import random

def generate_sequence(n):
    # Tvůj kód zde
    for _ in range(n):
        print(random.randint(0, 9))

# Otestování funkce
generate_sequence(10)  # Vygeneruje 10 náhodných čísel
