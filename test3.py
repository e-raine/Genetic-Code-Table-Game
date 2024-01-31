import random

generated_sets = []

i = 0
while i < 64:

    def generate_random():
        a = random.randint(1, 4)
        b = random.randint(1,4)
        C = random.randint(1, 4)

        return [a, b, C]

    def generate_unique_set():
        while True:
            random_set = generate_random()
            # Check if the set already exists
            if random_set not in generated_sets:
                return random_set

# Keep track of generated sets to ensure uniqueness
    generated_sets.append(generate_unique_set())

# Example: Generate 5 unique sets

    i += 1

print(generated_sets)