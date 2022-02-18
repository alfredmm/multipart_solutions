import math

print("PI Approximator -- Given Number of Terms")
print("----------------------------------------")
terms = int(input("Enter the Number of Terms: "))

total = 0
for i in range(terms):
    total = total + 4*(-1) ** i/ (2*i + 1)

print("Estimate Value of PI: ", total)
print("Error: ", math.pi - total)
