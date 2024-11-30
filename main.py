'''
MAIN.PY

Python file that is called for running the game. 
Initializes the game and imports all necessary functions and files.
'''

import grishelm.grishelm_settings as gset # Global variables, such as player stats and the game map.
from grishelm.ch1_items import * # Data on the properties and stats for every in-game item.
from nlp_functions import * # Functions to assist natural language processing.
from commands import commands # Commands for user interaction/gameplay.

# Initialize the global variables, like player stats and the game map.
gset.init()

# As long as the game isn't over, play another turn
while gset.game_continues :
    
    # ---- BASIC USER INTERACTION --- #

    # Tell user current location and their current stats.
    room = gset.player_status[3]
    print('You are in the ' + gset.game_map[room]['name'] + '. You have ' + str(gset.player_status[0]) + ' health, ' + str(gset.player_status[1]) + ' energy, and ' + str(gset.player_status[2]) + ' achievement.')
    
    directions = ', '.join(gset.game_map[room]['links'])
    print('You can go in the following directions: ' + directions + '.')
    
    # Let the user issue a command
    from_user = input().strip()

    # If there is a space in the user's input, separate it into two variables.
    if ' ' in from_user :
        first_space = from_user.index(' ')
        command = from_user[:first_space]
        direct_object = (from_user[first_space+1:]).strip()

        # If the direct object is an alternative name for an object, change it to the original name.
        if direct_object in item_aliases:
            direct_object = item_aliases[direct_object]
    else:
        command = from_user
        direct_object = None

    # Execute that command, if valid, otherwise, present user with list of valid commands.
    # Commands is a dict of functions (from commands.py).
    if command in commands :
        gset.game_continues = commands[command](direct_object)
    else :
        print('You cannot ' + command + '. Try one of these commands: ' + list_to_eng([key for key in commands], 'or') + '.')
        gset.inaction = True


   
    # -- UPDATE PLAYER STATS -- #
        
    # Consume one energy point if you actually perfomed an action.
    if gset.player_status[1] > 0 and not gset.inaction :
        gset.player_status[1] -= 1

    # If energy is zero, decrease one health point
    if gset.player_status[1] <= 0 :
        print('You are starving.')
        gset.player_status[0] -= 1

    # If health is zero, player has died---end game
    if gset.player_status[0] <= 0 :
        print('You have died.')
        gset.game_continues = False

    # Check if the player has won. (Achievement status.)
    if not gset.won and gset.player_status[2] >= 15:
        print('You have won. Do you want to continue playing?')
        response = input()
        check = False
        while check == False:
            if response == 'y' or response == 'Y' :
                check = True
                break
            elif response == 'n' or response == 'N' :
                check = True
                gset.game_continues = False
            elif response != 'y' or response != 'n':
                print('Please answer with y or n.')
                response = input()
        gset.won = True

 # ---- GAME STAT UPDATES --- #

    # Update stats for items that can be locked away.
    for item in get_conditions:
        items[item]['get'] = items[get_conditions[item]]['opened']
    
    # Switch inaction to False
    if gset.inaction: gset.inaction = False


# Exit message.
print('See you next time.')
