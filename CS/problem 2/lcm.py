import matplotlib.pyplot as plt
import numpy as np
import random
import math



def linear_congruential_generator(a, b, c, M, num_terms):
    sequence = []
    x = c
    for _ in range(num_terms):
        sequence.append(x)
        x = (a * x + b) % M
    return sequence

# Ask user for input values
print("Linear Congruential Generator (LCG) Simulation")
a = int(input("Enter the multiplier (a): "))
b = int(input("Enter the increment (b): "))
c = int(input("Enter the seed (c): "))
M = int(input("Enter the modulus (M): "))
n = int(input("Enter how many terms to generate: "))

# Generate sequence
lcg_sequence = linear_congruential_generator(a, b, c, M, n)

# Output
print("\nGenerated LCG Sequence:")
for i, val in enumerate(lcg_sequence):
    print(f"x{i} = {val}")











'''

a=5
b=3
c=7
M=16
n=10



import matplotlib.pyplot as plt

# Function to read parameters from file
def read_input_file(filename):
    params = {}
    with open(filename, 'r') as file:
        for line in file:
            if '=' in line:
                key, value = line.strip().split('=')
                params[key.strip()] = int(value.strip())
    return params

# Linear Congruential Generator function
def linear_congruential_generator(a, b, c, M, num_terms):
    sequence = []
    x = c
    for _ in range(num_terms):
        sequence.append(x)
        x = (a * x + b) % M
    return sequence

# Read parameters from input.txt
params = read_input_file('input.txt')
a = params['a']
b = params['b']
c = params['c']
M = params['M']
n = params['n']

# Generate sequence
lcg_sequence = linear_congruential_generator(a, b, c, M, n)

# Output
print("\nGenerated LCG Sequence:")
for i, val in enumerate(lcg_sequence):
    print(f"x{i} = {val}")

    

# Plotting the LCG sequence
plt.figure(figsize=(8, 4))
plt.plot(range(n), lcg_sequence, marker='o', linestyle='-', color='blue')
plt.title("Linear Congruential Generator Sequence")
plt.xlabel("Index")
plt.ylabel("Value")
plt.grid(True)
plt.show()

'''