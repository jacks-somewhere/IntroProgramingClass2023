
# Programing Exercise #8 Chapter 2 Python Book
# Tip, Tax, and Total

# Variables
TIP = .18
TAX = .07

#Get user to input the cost of their meal before tip and tax
meal=float(input('What is cost of your meal? $ '))

#Find the cost of the meal with tip
tip_cost = meal * TIP
meal_w_tip = meal + tip_cost
print(f'The cost of the meal with a tip is ${meal_w_tip:.2f}')

#Find the cost of the meal with tip and tax
tax_cost = meal * TAX
meal_tip_tax = meal + tip_cost + tax_cost
print(f'The cost of the meal with tip and tax included is ${meal_tip_tax:.2f}')

