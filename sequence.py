import random

def generate_sequence(number):
    for _ in range(number):
        print(random.randrange(100))
    pass
    

# Otestování funkce
generate_sequence(10)  # Vygeneruje 10 náhodných čísel
