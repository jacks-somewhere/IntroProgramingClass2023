
# Lab 8 Part 2
# Liters to Gallons

# Variables
LITER_TO_GALLON = 3.785

# Main Function, gets user input and displays output
def main():
    liters = float(input('Enter the number of liters pumped: '))
    price = float(input('Enter the total price to fill your tank: '))
    gallon = liters_to_gallons(liters)
    cost = price_per_gallon(liters, price)
    print(f'You put {gallon:.2f} gallons of gas into your tank.')
    print(f'You paid the equivalent of ${cost:.2f} per gallon.')

# Does conversion from liters to gallons and shows output
def liters_to_gallons(liters):
    gallon = liters / LITER_TO_GALLON
    return gallon
    
# Does conversion for the price from liters to gallons and shows output
def price_per_gallon(liters, price):
    cost = (price / liters) * LITER_TO_GALLON
    return cost 

# Calls main fuction
main()
