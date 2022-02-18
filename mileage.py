print("Your Fuel Economy")
total_miles =0
total_gallons =0

while True:
    miles = int(input("Number of miles Driven: "))
    gallons = int(input("Number of Gallons: "))
    mileage = miles/gallons
    print("Mileages covered: ", mileage)

    total_miles = total_miles + miles
    total_gallons = total_gallons + miles

    print("Total Miles: ", total_miles)