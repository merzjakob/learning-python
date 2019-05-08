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

