amount= float(input("Enter total bill: "))
tip = 15

while tip <= 25:
    tip_amount = amount * (tip/100)
    pct_str = "{:.0f}%".format(tip) # as percent
    tip_str = "${:.2f}".format(tip_amount) # in dollars
    print("A",pct_str, "tip is", tip_str)

    tip += 1