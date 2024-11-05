
# Task 2
# Final Project "Greek God Fighting simulator: 100 Battles"

# VARABLES
p_dodge_damage = 0
MAX_ROUNDS = 100

# Fighter 'Zeus'
F_HTH = 22
F_DAM = 10 
F_DODGE = 70
F_NAME = 'Zeus'
F_MONS = 'Typhon'
# Ranged 'Artemis'
R_HTH = 18
R_DAM = 14
R_DODGE = 60
R_NAME = 'Artemis'
R_MONS = 'The Aloadae Brothers'
# Thief 'Hermes'
T_HTH = 18
T_DAM = 10
T_DODGE = 50
T_NAME = 'Hermes'
T_MONS = 'Hippolytus'
# Engineer 'Athena'
E_HTH = 16
E_DAM = 18
E_DODGE = 65
E_NAME = 'Athena'
E_MONS = 'Medusa'
# Monster
MONSTER_HEALTH = 33
m_damage = 4 
m_dodge = 90
m_dodge_damage = .25

def main():
    #Opening
    print('')
    print(f'Welcome to the Greek God Fighting Simulator: {MAX_ROUNDS} Battles')
    print('________________________________________________________')
    print('--------------------------------------------------------')
    print(f'Each of the battles listed below will fight {MAX_ROUNDS} times. The final number')
    print('of battles that each god or goddess won will be shown after all battles')
    print('have finished. The god or goddess with the most wins will be given the title')
    print('of The Ultimate Winner. We don\'t believe in ties here, only winners.')
    print('')
    print('Battles: Zeus vs Typhon, Artemis vs The Aloadae Brothers')
    print('         Hermes vs Hippolytus, Athena vs Medusa')

    m_health = MONSTER_HEALTH

    #Runs loop for each battle based on MAX_ROUNDS and returns number of battles won
    fighter_rounds = battle_loop(F_HTH, F_DAM, F_DODGE, F_NAME, m_health)
    ranged_rounds = battle_loop(R_HTH, R_DAM, R_DODGE, R_NAME, m_health)
    theif_rounds = battle_loop(T_HTH, T_DAM, T_DODGE, T_NAME, m_health)
    engineer_rounds = battle_loop(E_HTH, E_DAM, E_DODGE, E_NAME, m_health)

    #Shows user final number of won rounds for each battle and ultimate winner
    print('____________________________________________________________________')
    print('--------------------------------------------------------------------')
    print(f'{F_NAME} won {fighter_rounds} rounds out of {MAX_ROUNDS} against {F_MONS}')
    print(f'{R_NAME} won {ranged_rounds} rounds out of {MAX_ROUNDS} against {R_MONS}')
    print(f'{T_NAME} won {theif_rounds} rounds out of {MAX_ROUNDS} against {T_MONS}')
    print(f'{E_NAME} won {engineer_rounds} rounds out of {MAX_ROUNDS} against {E_MONS}')
    print('')

    #Show user the player with the most rounds won
    if fighter_rounds > (max(ranged_rounds, theif_rounds, engineer_rounds)):
        print(f'The Ultimate Winner with {fighter_rounds} rounds won: {F_NAME}')
    elif ranged_rounds > (max(fighter_rounds, theif_rounds, engineer_rounds)):
        print(f'The Ultimate Winner with {ranged_rounds} rounds won: {R_NAME}')
    elif theif_rounds > (max(fighter_rounds, ranged_rounds, engineer_rounds)):
        print(f'The Ultimate Winner with {theif_rounds} rounds won: {T_NAME}')
    elif engineer_rounds > (max(fighter_rounds, ranged_rounds, theif_rounds)):
        print(f'The Ultimate Winner with {engineer_rounds} rounds won: {E_NAME}')
    else:
        print('There was a tie for the Ultimate Winner,')
        print('the title will not be awarded at this time')
    print('____________________________________________________________________')
    print('--------------------------------------------------------------------')

        
#Runs loop for each battle based on MAX_ROUNDS and returns number of battles won
def battle_loop(HEATH, DAMAGE, DODGE, NAME, m_health):
    play_round = 0
    final_count = 0
    p_health, p_damage, p_dodge, p_name = player_generator(HEATH, DAMAGE, DODGE, NAME)
    while play_round < MAX_ROUNDS:
        round_won = battle(p_health, p_damage, p_dodge, p_name, m_health)
        final_count += round_won
        play_round += 1
    return final_count

#Calculates the winner 
def battle(p_health, p_damage, p_dodge, p_name, m_health):
    while p_health > 0 and m_health > 0:
        #Player damage to monster
        dealt, m_health, dodge_damage = user_turn_damage(p_damage, m_dodge, m_health, m_dodge_damage)
        #Monster damage to player
        dealt, p_health, dodge_damage = computer_turn_damage(m_damage, p_dodge, p_health, p_dodge_damage)
    winner = check_for_winner(p_health, m_health, p_name)
    if winner == True:
        round_won = 1
    else:
        round_won = 0
    return round_won
    
#Assigns to correct stats to the battle
def player_generator(p_hth, p_dam, p_dodge, p_name):
    health = p_hth
    damage = p_dam
    dodge = p_dodge
    name = p_name
    return health, damage, dodge, name

#Random number generator based on damage 
def die_roll(damage):
    import random
    dealt = random.randint(1, damage)
    return dealt

#Generates the damage the player does to the monster
def user_turn_damage(p_damage, m_dodge, m_health, m_dodge_damage):
    dealt = die_roll(p_damage)
    m_health, dodge_damage = hit_check(m_dodge, m_health, dealt, m_dodge_damage)
    return dealt, m_health, dodge_damage

#Generates the damage the monster does to the player
def computer_turn_damage(m_damage, p_dodge, p_health, p_dodge_damage):
    dealt = die_roll(m_damage)
    p_health, dodge_damage = hit_check(p_dodge, p_health, dealt, p_dodge_damage)
    return dealt, p_health, dodge_damage

#Checks to see if player/monster dodged and calulates health 
def hit_check(dodge, health, dealt, dodge_damage): 
    import random
    chance = random.randint(1, 100) 
    if chance > dodge: 
        import math
        dodge_damage = math.floor(dealt * dodge_damage)
        health -= dodge_damage
    if chance <= dodge:
        health -= dealt
    return health, dodge_damage

def check_for_winner(p_health, m_health, name):
    if p_health > 0 and m_health <= 0:
        winner = True
    else:
        winner = False
    return winner

#Calls the main function 
main()
