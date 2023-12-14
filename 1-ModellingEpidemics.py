# Ask for parameters
n = float(input('n? '))
mu = float(input('mu? '))
sigma = float(input('sigma? '))
x = int(input('x? '))

# Define the value of e
e = 2.71828

# Turn the function into python code
fx = int(n * e ** -(((x - mu) ** 2) / (2 * (sigma ** 2))))

# Print the result
print(f"Estimated number of cases on day {x} is {fx}")
