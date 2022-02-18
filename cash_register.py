count = 0
total_price = 0

while True:
    price = input("Enter price:  ")
    count = count +1
    price = int(price)

    total_price = total_price + price
    print ("Items Entered: ", count)
    print("Total Price: ", total_price)

    if not price:
        break
    print("Success")
print("Exited...")