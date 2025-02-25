import random

def generate_random_numbers():
    numbers = [random.randint(0, 100) for _ in range(4)]
    print("Random numbers:", numbers)

generate_random_numbers()
