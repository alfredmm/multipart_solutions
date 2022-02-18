annual_rate = 150.0 
monthly_rate = annual_rate/12
balance = 1000
month = 1 # current month
# loop for 50 years updating balance
while month <= 12:
    interest = balance*(monthly_rate/100)
    balance = balance + interest
    month = month + 1
    formatted = "${:.2f}".format(balance)
    print("Final amount",formatted)