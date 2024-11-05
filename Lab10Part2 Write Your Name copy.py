
# Lab 10, Part 2
# Write your name

#Main function
def main():
    print('This program takes your name and writes it into')
    print('a new file then saves it.')

    #Gets user input for file
    name = input('Please enter your name: ')

    #Openes file and writes name
    name_file = open('name.txt', 'w')
    name_file.write(f'{name}\n')

    #Closes file and show a success message
    name_file.close()
    print('Your name is now writen in name.txt')

#Calls main function
main()
