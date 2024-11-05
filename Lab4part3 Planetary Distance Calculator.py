
# Lab 4
# Menu System: Planetary Distance Calculator
#see SWPlanets.txt

# Variables
# Assign number to plant from user list
MERCURY = 1
VENUS = 2
MARS = 3
ASTEROID_BELT = 4
JUPITER = 5
SATURN = 6
URANUS = 7
NEPTUNE = 8
PLUTO_KUIPER_BELT = 9
# Number of miles a plant is away from the sun
EARTH_NUM = 93000000
MERCURY_NUM = 35000000
VENUS_NUM = 67000000
MARS_NUM = 142000000
ASTEROID_BELT_NUM = 297000000
JUPITER_NUM = 484000000
SATURN_NUM = 889000000
URANUS_NUM = 1790000000
NEPTUNE_NUM = 2880000000
PLUTO_KUIPER_BELT_NUM = 3670000000
# Time it takes for a laser to travel miles/sec
LASER = 186000 


# User introduction
print("Welcome to the Planetary Distance Calculator from Earth program!")
print("1) Mercury 2) Venus 3) Mars 4) Asteroid Belt 5) Jupiter")
print("6) Saturn 7) Uranus 8) Neptune 9) Pluto / Kuiper Belt")

# Get user to select a plant from above list
picked_plant = int(input("Choose a plant by it's corresponding number: "))

# Connects user input to plant and calculates the distance bewteen plants
if picked_plant >= 10 or picked_plant <= 0:
    print('Please restart the Distance Calculator and pick a number between 1-9')
elif picked_plant == MERCURY:
    result = EARTH_NUM - MERCURY_NUM
    plant = 'Mercury'
elif picked_plant == VENUS:
    result = EARTH_NUM - VENUS_NUM
    plant = 'Venus'
elif picked_plant == MARS:
    result = MARS_NUM - EARTH_NUM
    plant = 'Mars'
elif picked_plant == ASTEROID_BELT:
    result = EARTH_NUM - ASTEROID_BELT
    plant = 'Asteroid Belt'
elif picked_plant == JUPITER:
    result = JUPITER_NUM - EARTH_NUM
    plant = 'Jupiter'
elif picked_plant == SATURN:
    result = SATURN_NUM - EARTH_NUM
    plant = 'Saturn'
elif picked_plant == URANUS:
    result = URANUS_NUM - EARTH_NUM
    plant = 'Uranus'
elif picked_plant == NEPTUNE:
    result = NEPTUNE_NUM - EARTH_NUM
    plant = 'Neptune'
elif picked_plant == PLUTO_KUIPER_BELT:
    result = PLUTO_KUIPER_BELT_NUM - EARTH_NUM
    plant = 'Pluto / Kuiper Belt'
    
print(f'The distance between Earth and {plant} is: {result:,} miles')

# calculates how long it takes a laser beam to travel between Earth and user selected plant
if picked_plant <= 9 and picked_plant >= 1:
    laser_time = result / LASER
    print(f"The time it takes for a laser beam to travel this distance is: {laser_time:,.2f} seconds")
