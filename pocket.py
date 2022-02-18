print("Pocket Change Calculator")
print("========================")


quarters = int(input("How many quarters?"))

dimes = int(input("How many dimes?"))

nickels = int(input("How many nickels?"))

pennies = int(input("How many pennies?"))
print("==================================")
amount= ((quarters*25) +(dimes*10)+(nickels*5)+pennies)/100
formatted_str = "$ {:.2f}".format(amount)
print("You have: ", formatted_str)