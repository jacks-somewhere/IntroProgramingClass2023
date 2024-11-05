
# Lab 6 Part 1
# Five Little Monkeys Jumping on the Bed

# Asks user to input a number 
monkeys = int(input('How many monkeys start jumping on the bed? '))

# Starts the count down loop using user input as a starting point
for monkeys in reversed(range(1, monkeys + 1)):
    print(' ')
    print(f'{monkeys} little monkeys jumpin on the bed, 1 fell off and')
    print('bumped his head, momma called the doctor and the')
    print('doctor said, no more monkeys jumping on the bed.')
    




