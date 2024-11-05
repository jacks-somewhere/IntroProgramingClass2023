
# Lab 9, Part 1
# Picnic Planning

# Var
HOTDOG = 10
BUNS = 8

# Main function, gets user input and show outputs
def main():
    num_people = int(input('How many people are coming to the picnic? '))
    num_dog = int(input('How many hot dogs is each person going to eat? '))
    dogs = num_people * num_dog 
    dog_pack = packages_to_buy(dogs, HOTDOG) 
    buns_pack = packages_to_buy(dogs, BUNS)
    left_dogs = leftover(dogs, dog_pack, HOTDOG)
    left_buns = leftover(dogs, buns_pack, BUNS)
    print(f'Hot dogs packages needed: {dog_pack}')
    print(f'Hot dog bun packages needed: {buns_pack}')
    print(f'Hot dogs left over: {left_dogs}')
    print(f'Hot dog buns left over: {left_buns}')
    
# Calculates the number of packages for needed
def packages_to_buy(dogs, pack_numb):
    import math
    packs = math.ceil(dogs / pack_numb) 
    return packs 

# Calculates the number of left overs
def leftover(dogs, pack, PACK_NUM):
    left = (pack * PACK_NUM) - dogs 
    return left 

# Calles Main function
main()



