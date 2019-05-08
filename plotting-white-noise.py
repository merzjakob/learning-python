# import numpy package to work with arrays, math functions, generate random numbers and linear algebra
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

# version 1
x = np.random.randn(100)
plt.plot(x)
plt.show()

#version 2
# set desired length of time series
ts_length = 100
# Empty list
ϵ_values = []

#draws random number from time series
for i in range(ts_length):
  # indented lines will be executed before moving on
  # all lines of block have to have same indentation
  # start of block
    e = np.random.randn()
    ϵ_values.append(e)
  # end of block
plt.plot(ϵ_values)
plt.show()

# We can include heterogeneous data inside a list
# first index is also zero
x = [10, 'foo', False]
#output of what kind of object
type(x)

x.append(2.5)
x

animals = ['dog', 'cat', 'bird']
# for variable_name in sequence:
for animal in animals:
    print("The plural of " + animal + " is " + animal + "s")

# while loops
ts_length = 100
ϵ_values = []
i = 0
while i < ts_length:
    e = np.random.randn()
    ϵ_values.append(e)
    i = i + 1
plt.plot(ϵ_values)
plt.show()

# Break program into two parts:

# 1. define function that generates a list of n random variables
def generate_data(n):
  # indent function body
    ϵ_values = []
    for i in range(n):
      # indent code block inside loop
        e = np.random.randn()
        ϵ_values.append(e)
      # end of loop
    return ϵ_values

# 2. main part of the program will
#   a. call function to get data
#   b. plot data
data = generate_data(100)
plt.plot(data)
plt.show()

#adding if statement to function

def generate_data(n, generator_type):
    ϵ_values = []
    for i in range(n):
        if generator_type == 'U':
            e = np.random.uniform(0, 1)
        else:
            e = np.random.randn()
        ϵ_values.append(e)
    return ϵ_values

print('uniform values')
data = generate_data(100, 'U')
plt.plot(data)
plt.show()

print('random values')
data = generate_data(100, 'N')
plt.plot(data)
plt.show()

# simplified code
def generate_data(n, generator_type):
    ϵ_values = []
    for i in range(n):
        e = generator_type()
        ϵ_values.append(e)
    return ϵ_values

data = generate_data(100, np.random.uniform)
plt.plot(data)
plt.show()


# Excercise 1
def factorial(n):
    # counter
    num = 1
    # check if number is positive
    while n >= 1:
      # reassign counter to current value of n * current value of n
        num = num * n
        # reduce current value of n by 1
        n = n - 1
    # return value of num
    return num

# call function
factorial(7)

# Excercise 2
from numpy.random import uniform

def binomial_rv(n, p):
    count = 0
    for i in range(n):
        U = uniform()
        if U < p:
            count = count + 1    # Or count += 1
    return count

binomial_rv(10, 0.5)

# Excercise 3
n = 100000

count = 0
for i in range(n):
    u, v = np.random.uniform(), np.random.uniform()
    d = np.sqrt((u - 0.5)**2 + (v - 0.5)**2)
    if d < 0.5:
        count += 1

area_estimate = count / n

print(area_estimate * 4)  # dividing by radius**2

# Excercise 4
from numpy.random import uniform

payoff = 0
count = 0

for i in range(10):
    U = uniform()
    count = count + 1 if U < 0.5 else 0
    if count == 3:
        payoff = 1

print(payoff)

# Excercise 5
α = 0.9
ts_length = 200
current_x = 0

x_values = []
for i in range(ts_length + 1):
    x_values.append(current_x)
    current_x = α * current_x + np.random.randn()
plt.plot(x_values)
plt.show()

# Excercise 6
αs = [0.0, 0.8, 0.98]
ts_length = 200

for α in αs:
    x_values = []
    current_x = 0
    for i in range(ts_length):
        x_values.append(current_x)
        current_x = α * current_x + np.random.randn()
    plt.plot(x_values, label=f'α = {α}')
plt.legend()
plt.show()






