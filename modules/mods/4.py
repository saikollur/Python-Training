import random

print("Printing random numbers using Random Module.")
for i in range(10):
    print(random.randint(1, 100))

nums = [i for i in range(1, 100)]
random_num = random.choice(nums)
print(f"Choosing a random number from the list : {random_num}")
