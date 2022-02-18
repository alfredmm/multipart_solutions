amount_dollars= float(input('Enter amount in Dollars: '))

quarters = amount_dollars // 0.25
rem1 = amount_dollars % 0.25

dimes = rem1 // 0.10
rem2 = rem1 % 0.10

nickels = rem2 // 0.05
rem3 = rem2 % 0.05

pennies = rem3 // 0.01


print("Quarters = ", quarters)
print("Dimes = ", dimes)
print("Nickels = ", nickels)
print("Pennies = ", pennies)

