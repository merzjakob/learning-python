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
