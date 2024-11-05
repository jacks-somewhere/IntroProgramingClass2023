
# Task 1 
# Final Project "Greek God Fighting simulator: 1 vs 1"

# VARABLES
second_attack = 2      #If first attack is less then or equal to this, second attack will become available
p_dodge_damage = 0     #Damage the player takes when dodging
m_second_dodge = 100   #Makes the monster not be able to dodge the second attack

# Fighter 'Zeus'
FIGHTER_HTH = 25
FIGHTER_DAM = 10 
FIGHTER_DODGE = 70
# Ranged 'Artemis'
RANGED_HTH = 18
RANGED_DAM = 14
RANGED_DODGE = 60
# Thief 'Hermes'
THIEF_HTH = 18
THIEF_DAM = 10
THIEF_DODGE = 50
# Engineer 'Athena'
ENGINEER_HTH = 16
ENGINEER_DAM = 18
ENGINEER_DODGE = 65
# Monster
MONSTER_HEALTH = 33
m_damage = 4 
m_dodge = 90
m_dodge_damage = .25

def main():
    #Opening
    print('')
    print('Welcome to the Greek God Fighting Simulator: 1 vs 1')
    print('___________________________________________________')
    print('---------------------------------------------------')
    print('Here you can play out your very own Greek battle as one of the')
    print('ancient gods or goddesses! Join them as they fight against their')
    print('old foes in an epic battle.')
    print('')
    print('Battles: 1-Zeus vs Typhon 2-Artemis vs The Aloadae Brothers')
    print('         3-Hermes vs Hippolytus 4-Athena vs Medusa')
    # Askes for user to pick battle and assigns correct information
    p_health, p_damage, p_dodge, p_name, monster, p_weapon, m_weapon = player_generator()
    print('')
    m_health = MONSTER_HEALTH
    play_round = 1 

    #Starts the loop that ends when the monster or players health hits 0
    while p_health > 0 and m_health > 0:
        print(f'*Round {play_round}*')

        #Player damage to monster
        dealt, hit, m_health, dodge_damage = user_turn_damage(p_damage, m_dodge, m_health, m_dodge_damage)

        #Shows player output based on if they where hit or dodged
        if hit == True:
            print(f'{p_name} hit {monster} with {p_weapon} dealing {dealt} damage')
        else:
            print(f'{monster} dodged {p_name} but was still hit with {p_weapon} dealing {dodge_damage} damage')

        #Second attack option for player if first attack is low 
        if dealt <= second_attack:
                attack_choice = attack_type(p_name)
                dealt, hit, m_health, dodge_damage= user_turn_damage(p_damage, m_dodge, m_health, m_dodge_damage)
                if attack_choice == 1:
                    print(f'In a suprise second attack, {p_name} hit {monster} with {p_weapon} dealing {dealt} damage')
                if attack_choice == 2:
                    print(f'{monster} tripped allowing {p_name} to push {monster} over dealing {dealt} damage')
                    print(f'That was very childish of {p_name}! {monster} did not appeciate that.')
                if attack_choice == 3:
                    print(f'{p_name} threw a large rock at {monster} head, leaving a large cut dealing {dealt} damage')
                    print(f'Where did {p_name} pull that rock from? We will never know...')
            
        #Monster damage to player
        dealt, hit, p_health, dodge_damage = computer_turn_damage(m_damage, p_dodge, p_health, p_dodge_damage)

        # Shows the correct statement based on hit the monster was hit or dodged
        if hit == True: 
            print(f'{monster} hit {p_name} with {m_weapon} dealing {dealt} damage')
        else:
            print(f'{p_name} dodged {monster}')
        
        #Round Results
        play_round += 1
        print(f'Round Results: {p_name}= {p_health} HP, {monster}= {m_health} HP')
        print('')

    #Checks to see who is the winner
    winner = check_for_winner(p_health, m_health, p_name, monster)
    play_round -= 1
    #Final output for player
    print(f'\t_____________________________________')
    print(f'\t-------------------------------------')
    print(f'\tOutcome of the battle: {winner}')
    print(f'\tNumber of Rounds: {play_round}')
    print(f'\t_____________________________________')
    print(f'\t-------------------------------------')
    
    
#Assigns to correct stats to user picked player
def player_generator():
    picked_class = int(input('Enter the number of your choosen battle: '))

    #Checks for input errors
    while picked_class <= 0 or picked_class > 4:
        #put in range?
        print('Error: pick 1, 2, 3, or 4 when prompted')
        picked_class = int(input('Enter the number of your choosen battle: '))
        
    if picked_class == 1:
        health = FIGHTER_HTH
        damage = FIGHTER_DAM
        dodge = FIGHTER_DODGE
        name = 'Zeus'
        monster = 'Typhon'
        weapon = 'his thunderbolt'
        monster_weapon = 'his flames'
    if picked_class == 2:
        health = RANGED_HTH
        damage = RANGED_DAM
        dodge = RANGED_DODGE
        name = 'Artemis' 
        monster = 'The Aloadae brothers'
        weapon = 'their own spears' 
        monster_weapon = 'their spears'
    if picked_class == 3:
        health = THIEF_HTH
        damage = THIEF_DAM
        dodge = THIEF_DODGE
        name = 'Hermes'
        monster = 'Hippolytus'
        weapon = 'his golden sword'
        monster_weapon = 'his fists'
    if picked_class == 4:
        health = ENGINEER_HTH
        damage = ENGINEER_DAM
        dodge = ENGINEER_DODGE
        name = 'Athena'
        monster = 'Medusa'
        weapon = 'her sword'
        monster_weapon = 'her snakes'
    return health, damage, dodge, name, monster, weapon, monster_weapon

#Random number generator based on damage 
def die_roll(damage):
    import random
    dealt = random.randint(1, damage)
    return dealt

#Generates the damage the player does to the monster 
def user_turn_damage(p_damage, m_dodge, m_health, m_dodge_damage):
    dealt = die_roll(p_damage)
    hit, m_health, dodge_damage = hit_check(m_dodge, m_health, dealt, m_dodge_damage)
    return dealt, hit, m_health, dodge_damage

#Generates the damage the monster does to the player
def computer_turn_damage(m_damage, p_dodge, p_health, p_dodge_damage):
    dealt = die_roll(m_damage)
    hit, p_health, dodge_damage = hit_check(p_dodge, p_health, dealt, p_dodge_damage)
    return dealt, hit, p_health, dodge_damage

#Prompts player to pick the output for second chance
def attack_type(p_name):
    print(f'{p_name} has a chance to attack for a second time!')
    print(f'{p_name} can do 1 of 3 different types of attacks: suprise- 1 childish- 2 magical-3')
    attack_choice = int(input(f'Enter the number of your choosen attack: '))
    while attack_choice <= 0 or attack_choice > 3:
        print('Error: pick a number associated with a attack type')
        attack_choice = int(input(f'Enter the number of your choosen attack: '))
    return attack_choice

#Checks to see if player/monster dodged and calulates health 
def hit_check(dodge, health, dealt, dodge_damage): 
    chance = die_roll(100) 
    if chance > dodge: 
        hit = False
        import math
        dodge_damage = math.floor(dealt * dodge_damage)
        health -= dodge_damage
    if chance <= dodge:
        hit = True
        health -= dealt
    return hit, health, dodge_damage

#Checks to see who won or if there was a tie
def check_for_winner(p_health, m_health, name, monster):
    if p_health <= 0 and m_health > 0:
        winner = f'{monster} Won'
    if p_health > 0 and m_health <= 0:
        winner = f'{name} Won'
    if p_health <= 0 and m_health <= 0:
        winner = 'Tie'
    return winner

#Calls the main function 
main()
