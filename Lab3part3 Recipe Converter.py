
# Lab 3 Part 3 Recipe Converter

# Shows the amount of ingredients that is required to make the amount of
# cookies a user enters.

# Variables 
    # SUGER, BUTTER, and FLOWER are cups, VANILLA is teaspoons
SUGER = 1.5
BUTTER = .5
FLOUR = 2.5
VANILLA = 1
COOKIE_AMT = 36

# Find the amount required of each ingredients to make 1 cookie
suger_adj = SUGER / COOKIE_AMT
butter_adj = BUTTER / COOKIE_AMT
flour_adj = FLOUR / COOKIE_AMT
vanilla_adj = VANILLA / COOKIE_AMT

desired_amt = float(input('How many cookies would you like to make today? '))

# Calculate the amount of ingredients required
suger_tot = desired_amt * suger_adj
butter_tot = desired_amt * butter_adj
flour_tot = desired_amt * flour_adj
vanilla_tot = desired_amt * vanilla_adj

# Shows final amounts to the user
print('')
print('The total required amount of each ingredient is shown below')
print(f'Suger - {suger_tot:.2f} cups')
print(f'Butter - {butter_tot:.2f} cups')
print(f'Flour - {flour_tot:.2f} cups')
print(f'Vanilla - {vanilla_tot:.2f} teaspoons')
