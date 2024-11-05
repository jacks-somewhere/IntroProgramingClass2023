
# Lab 7 Part 2
# Budget Program From a Flowchart


# Variables
expense = 1
total = 0


# Intro message
print('Welcome to the Budget Program!')
print('******************************')
budget = float(input('Please enter your budget: '))

# Asks for all of users expenses
while expense != 0:
    expense = float(input('\t Enter one expense (0 to end): '))
    total += expense
    

# Math to find if budget was under or over
final = budget - total

# ifs for final user output
if final > 0:
    word = 'under by'
    print(f'You are under your final budget by ${final:,.2f}.')
if final < 0:
    final = total - budget
    print(f'You are over your final budget by ${final:,.2f}.')
if final == 0:
    print('You are currently on budget.')
