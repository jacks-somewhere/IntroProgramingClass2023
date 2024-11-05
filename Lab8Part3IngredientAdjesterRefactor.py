
# Lab 8 Part 3
# Ingredient Adjester Refactor

# Variables
ORG_SUGER = 1.5 # CUPS
ORG_BUTTER = 1 # CUP
ORG_FLOUR = 2.75 # CUPS
ORG_COOKIE = 48

# Main fuction, gets user input and shows output
def main():
    adj_cookie = int(input('Enter the number of cookies you would like to make: '))
    ratio = adj_cookie / ORG_COOKIE
    adj_suger = adjust_ingredient(ratio, ORG_SUGER)
    adj_butter = adjust_ingredient(ratio, ORG_BUTTER)
    adj_flour = adjust_ingredient(ratio, ORG_FLOUR)
    # Output for User
    print('')
    print('You will need:')
    print(f'\t{adj_suger:.2f} cups of suger')
    print(f'\t{adj_butter:.2f} cups of butter')
    print(f'\t{adj_flour:.2f} cups of flour')

# Does the math for ingredient amount 
def adjust_ingredient(ratio, ing_amount):
    return ratio * ing_amount
    

# def adjuct_ingredient(ratio, ing_amount):
#    ingredient = ratio * ing_amount
#    return ingredient

# Calls main fuction
main()
