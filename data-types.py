# Unpacking US cities text file
data_file = open('us_cities.txt', 'r')
for line in data_file:
    # Tuple unpacking
    city, population = line.split(':')
    # Capitalize city names
    city = city.title()
    # Add commas to numbers
    population = f'{int(population):,}'
    print(city.ljust(15) + population)
data_file.close()


# Merge lists through zip function
countries = ('Japan', 'Korea', 'China')
cities = ('Tokyo', 'Seoul', 'Beijing')
for country, city in zip(countries, cities):
    print(f'The capital of {country} is {city}')

# Create dictionary through zip by assigning key value pair
names = ['Tom', 'John']
marks = ['E', 'F']
dict(zip(names, marks))

# Defining functions with multiple return statements
# last line is not by default returned as in Ruby
def f(x):
    if x < 0:
        return 'negative'
    return 'nonnegative'
f(2)

# Try out docstring
def f(x):
    """
    This function squares its argument
    """
    return x**2

f?
f??

# lamda for simple one line functions
f = lamda x: x**3

# example to calculate integral
from scipy.integrate import quad

quad(lambda x: x**3, 0, 2)

# Excercises Data types:

# Excercise 1 Part 1:
x_vals = [2,3,4,5,6,7,8]
y_vals = [20,31,14,25,26,57,78]

sum([x_val * y_val for x_val, y_val in zip(x_vals, y_vals)])

# Excercise 1 Part 2:
x = 0
for i in list(range(100)):
    if i % 2 == 0:
        x += 1
print(x)

# Excercise 1 Part 3:
x = 0
pairs = ((2, 5), (4, 2), (9, 8), (12, 10))
sum([x % 2 == 0 and y % 2 == 0 for x,y in pairs])

# Excercise 2:

# Excercise 3:
def capitalize(x):
    upper = sum(1 for i in x if i.isupper())
    print(upper)

capitalize("HELlo MY LOVE")

# Excercise 4:
def f(seq_a, seq_b):
    is_subset = True
    for a in seq_a:
        if a not in seq_b:
            is_subset = False
    return is_subset

# == test == #

print(f([1, 2], [1, 2, 3]))
print(f([1, 2, 3], [1, 2]))


