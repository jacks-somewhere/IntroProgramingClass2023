
# Lab 7
# Input Validation


# Variables
PAR = 75


print('Welcome to our Golf Course')
print('--------------------------')

# Gets user input
score = int(input('Enter your golf score: '))

# Checks for errors and loops intel correct number is entered
while score < 18 or score > 105:
    print('Score out of range [18-105].')
    score = int(input('Enter your golf score: '))

# Determines final number over par and shows correct print phrase
if score >= 75:
    score = score - PAR
    print(f'You scored {score} over par.')
else:
    score = PAR - score
    print(f'Your scored {score} under par.')
                
