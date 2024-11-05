
# Lab 6 Part 2
# Counting by the number N

# Variables
base = 0

# Shows program title to user
print('Let\'s count to 200.')

# Asks for user input
n = int(input('By what number do you wish to count? '))

# Loop for output
while base < 200:
    base += n
    print(base, end=', ')


