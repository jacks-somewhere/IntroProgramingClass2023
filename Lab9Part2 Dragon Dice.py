
# Lab 9, Part 2
# Dragon Dice Rolling


#Main function
def main():
    #Shows user opening and askes for input to start program
    print('Welcome to the Dragon Dice Rolling Simulator')
    print('++++++++++++++++++++++++++++++++++++++++++++')
    print('Enter Zero to end the program')
    print('')
    dice = int(input('What dice would you would like to roll (d4, d6, d8, d10, d12, d20)?: '))

    #Starts the loop 
    while dice == 4 or dice == 6 or dice == 8 or dice == 10 or dice == 12 or dice == 20:
        roll_num = int(input(f'How many times would you would like to roll the the d{dice}?: '))
        total = 0
        print('You have rolled a:')
        #Starts loop for the random number generator  and shows outputs
        for count in range(roll_num):
            rolled_num = roll(roll_num, dice)
            total += rolled_num
            print(f'{rolled_num}')
        print(f'You have rolled a grand total of: {total}')
        #Askes for user input to start loop again or end it
        print('')
        dice = int(input('What dice would you would like to roll (d4, d6, d8, d10, d12, d20)?: '))

    #Shows user programing ending
    print('')
    print('Thank you for using the Dragon Dice Rolling Simulator')

#Roll function, generates random number based on user picked dice
def roll(roll_num, dice):
    import random
    rolled_num = random.randint(1, dice) 
    return rolled_num

#Calls main function  
main()
