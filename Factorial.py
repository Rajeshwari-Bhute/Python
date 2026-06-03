# Read input
n = int(input())

# Initialize factorial
factorial = 1

# Calculate factorial using loop
if n < 0:
    print("Factorial not defined")
else:
    for i in range(1, n + 1):
        factorial *= i
    print(factorial)
