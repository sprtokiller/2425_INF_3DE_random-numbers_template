import random

def generate_sequence(n):
    if n < 0:
        return ValueError
    else:
        sequence = []

        for _ in range(n):
            sequence.append(random.random())

        return sequence

# Otestování funkce
print(generate_sequence(10))  # Vygeneruje 10 náhodných čísel
