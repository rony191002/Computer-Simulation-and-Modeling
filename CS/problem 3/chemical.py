import matplotlib.pyplot as plt
import random
import math

A = 100.0
B = 60.0
C = 0.0
dt = 0.1
k1 = 0.008
k2 = 0.002
time = 0
list_a = [A]
list_b = [B]
list_c = [C]
list_time = [time]
t_max = 100.0
loop = (int)(t_max / dt)


for i in range (loop):
    rate = k1 * A*B - k2*C
    dC = rate*dt

    A -= dC
    B -= dC
    C += dC
    A = max(0, A)
    B = max(0, B)

    time += dt
    list_a.append(A)
    list_b.append(B)
    list_c.append(C)
    list_time.append(time)

plt.figure(figsize = (10, 10))
plt.plot(list_time, list_a, label = 'Substance A' , color = 'green')
plt.plot(list_time, list_b, label = 'Substance B', color = 'red')
plt.plot(list_time, list_c, label = 'Substance C', color = 'blue')
plt.title("Simulation...")
plt.xlabel("Time")
plt.ylabel("Amount")
plt.legend()
plt.grid(True)
plt.show()







'''
A=100.0
B=60.0
C=0.0
dt=0.1
k1=0.008
k2=0.002
t_max=100.0



import matplotlib.pyplot as plt

# Function to read parameters from a file
def read_input_file(filename):
    params = {}
    with open(filename, 'r') as file:
        for line in file:
            if '=' in line:
                key, value = line.strip().split('=')
                params[key.strip()] = float(value.strip())
    return params

# Read values from file
params = read_input_file('input.txt')

# Assign values
A = params['A']
B = params['B']
C = params['C']
dt = params['dt']
k1 = params['k1']
k2 = params['k2']
t_max = params['t_max']

# Initialization
time = 0
list_a = [A]
list_b = [B]
list_c = [C]
list_time = [time]
loop = int(t_max / dt)

# Simulation loop
for i in range(loop):
    rate = k1 * A * B - k2 * C
    dC = rate * dt

    A -= dC
    B -= dC
    C += dC
    A = max(0, A)
    B = max(0, B)

    time += dt
    list_a.append(A)
    list_b.append(B)
    list_c.append(C)
    list_time.append(time)

# Plotting
plt.figure(figsize=(10, 10))
plt.plot(list_time, list_a, label='Substance A', color='green')
plt.plot(list_time, list_b, label='Substance B', color='red')
plt.plot(list_time, list_c, label='Substance C', color='blue')
plt.title("Simulation from File Input")
plt.xlabel("Time")
plt.ylabel("Amount")
plt.legend()
plt.grid(True)
plt.show()

'''