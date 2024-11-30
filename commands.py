'''
COMMANDS.PY

This file contains the command functions for the commands the player can declare, sorted alphabetically.
'''

# import global_settings as gset # Global variables, such as player stats and the game map.
import grishelm.grishelm_settings as gset
from grishelm.ch1_items import * # Data on the properties and stats for every in-game item.
from nlp_functions import * # Functions to assist natural language processing.

# Container for command functions.
commands = {}


# --- DROP --- #
def drop(direct_object) :
    room_id = gset.player_status[3]
    gset.inaction = True
    if direct_object == None:
        print('You must specify what to drop.')
    elif direct_object not in items:
        print('You cannot drop ' + direct_object + '.')
    elif direct_object not in gset.player_inventory:
        print('You do not have ' + gset.player_inventory + ' in your inventory.')
    else :
        print('You drop the ' + direct_object + ' in the ' + gset.game_map[room_id]['name'] + '.')
        gset.game_map[room_id]['inventory'] += [direct_object]
        gset.player_inventory.remove(direct_object)
    return True

commands['drop'] = drop # -- Key function by its name in a string.

# --- EAT --- #

# Each kind of food is associated with a list indicating:
# [<how it tastes>,<how it affects health>, <how it affects energy>]

# Load in the edible items from the item dictionary into a local dictionary.
food_results = {item: items[item]['food'] for item in items if items[item]['food'] != None}

# Eat function
def eat(direct_object) :
    room_id = gset.player_status[3]
    gset.inaction = True
    if direct_object == None :
        print('You must specify what to eat')
    elif direct_object not in gset.player_inventory and direct_object not in gset.game_map[room_id]['inventory']:
        print('You do not have ' + direct_object + '.')
    elif direct_object not in food_results :
        print('You cannot eat ' + direct_object + '.')
    elif (direct_object in gset.game_map[room_id]['inventory'] or direct_object in gset.player_inventory) and items[direct_object]['get']:
        results = food_results[direct_object]
        print('It tastes ' + results[0] + '.')
        gset.player_status[0] += results[1]
        gset.player_status[1] += results[2]
        if direct_object in gset.player_inventory :
            gset.player_inventory.remove(direct_object)
        else :
            gset.game_map[room_id]['inventory'].remove(direct_object)
            for item in item_inventories:
                if item in gset.game_map[room_id]['inventory'] and direct_object in item_inventories[item]:
                    item_inventories[item].remove(direct_object)
                    break
    else:
        print('You do not have ' + direct_object + '.')
    return True

commands['eat'] = eat # -- Key function by its name in a string.


# ---- FIGHT ---- #

# Each inventory item's fighting properties:
# [<fightable?>, <fight_advantage>, <health>, <damage>, <losable>]

# Load in the items from the item dictionary which can be used in or fought against in a fight.
fight_dict = {item: items[item]['fight'] for item in items if items[item]['fight'] != None}

# Fight function
def fight(direct_object) :
    global inaction
    room_id = gset.player_status[3]
    room_inventory = [item for item in gset.game_map[room_id]['inventory']]

    # - Set award variable for easier code comprehension.
    if direct_object in fight_dict:
        award = fight_dict[direct_object][5]

    if direct_object == None :
        print("You must specify what to fight.")
        gset.inaction = True
    elif direct_object not in items:
        print("You cannot fight " + direct_object + '.')
        gset.inaction = True
    elif items[direct_object]['fight'] == None:
        print("You cannot fight " + direct_object + '.')
        gset.inaction = True
    elif not fight_dict[direct_object][0] :
        print("You cannot fight " + direct_object + '.')
        gset.inaction = True
    elif direct_object not in room_inventory:
        print("You can't fight something that's not there.")
        gset.inaction = True
    elif fight_dict[direct_object][0] and direct_object in room_inventory:
        print("What do you want to fight with? (nothing is an option)")
        weapon = input()
        if weapon == '' or weapon == ' ':
            weapon = 'nothing'

        if weapon not in fight_dict:
            print("You can't fight with " + weapon + '.')
            gset.inaction = True
        elif weapon not in gset.player_inventory and weapon != 'nothing':
            print('Please choose an item in your inventory or nothing.')
            gset.inaction = True
        else :
            if direct_object == 'troll' and weapon == 'staff':
                gset.game_map[room_id]['inventory'].remove(direct_object)
                gset.game_map[room_id]['inventory'].append('Laura')
                print('Although you were planning to fight the troll, as you approach with the staff, light jumps from it to the troll revealing that she was enchanted.')
                print('Laura Ingalls Wilder appears where the troll once was. "Thank you for releasing me from the enchantment," she says gratefully.') 
                print('You decide this is not the best time to tell her you were planning to slay her in troll form, that would have been an mistake.')
                gset.player_status[2] += 5
            else:
                strength = 3 + fight_dict[weapon][1] # - Calculate player's total fighting strength.
                fight_dict[direct_object][2] -= strength # - Deal damage to target's health.
                gset.player_status[0] -= fight_dict[direct_object][3] # - Deal damage to player's health.

                # - Lose item if fighting involves its breaking.
                if fight_dict[weapon][4]:
                    gset.player_inventory.remove(weapon)
                    print("You lost the " + weapon + ".")

                # - If the player is dead just exit now.
                if gset.player_status[0] < 0:
                    return True
                
                # - If the target dies...
                if fight_dict[direct_object][2] <= 0:
                    
                    if type(award) == str: # - Items that cause you to lose the game.
                        print(award) # - Print fight/death message.
                        return False # - End game
                    elif award <= 0: # - Items with negative reward.
                        gset.player_status[2] += award # - Adjust player acheivement accordingly.
                        print('Murder doesn\'t win you anything. You lost ' + str(award) + ' achievement.') # - This is programmed specifically to discourage murder.
                    else: # - Otherwise, it has positive reward.
                        gset.player_status[2] += award
                        print("You defeated the " + direct_object + '. Gain ' + str(award) + ' achievement.')
                else : # - Otherwise, find out if the player wants to fight it again.
                    print('The ' + direct_object + ' has ' + str(fight_dict[direct_object][2]) + ' health left. You have ' + str(gset.player_status[0]) + ' health left. Do you want to fight again?')
                    response = input()
                    check = False
                    while check == False:
                        if response == 'y' or response == 'Y' :
                            check = True
                            gset.player_status[1] -= 1
                            fight(direct_object)
                        elif response == 'n' or response == 'N':
                            print('The ' + direct_object + ' is still here.')
                            check = True
                        elif response != 'y' or response != 'n':
                            print('Please answer with y or n.')
                            response = input()
                    
    return True

commands['fight'] = fight # -- Key to function call is the name of the function as a string.


# ---- GET ---- $

def get(direct_object) : 
    room_id = gset.player_status[3]
    if direct_object in gset.game_map[room_id]['inventory'] and items[direct_object]['get']:
        gset.player_inventory.append(direct_object)
        gset.game_map[room_id]['inventory'].remove(direct_object)
        for item in item_inventories:
            if item in gset.game_map[room_id]['inventory'] and direct_object in item_inventories[item]:
                item_inventories[item].remove(direct_object)
                break
        print("Item acquired.")
    elif direct_object not in items :
        print("We\'re sorry, this item does not exist.")
        gset.inaction = True
    elif not items[direct_object]['get']:
        print("You cannot get this item.")
        gset.inaction = True
    else:
        print("Item is not here.")
        gset.inaction = True
    return True
        
commands['get'] = get # -- Key to the function call as name of function in string.


# ---- GO ---- #

def go(direct_object) :
    room_id = gset.player_status[3]
    room_links = gset.game_map[room_id]['links']
    hidden_links = gset.game_map[room_id]['hidden_links']

    if direct_object == None :
        print('You must specify where to go.')
        gset.inaction = True
    elif direct_object == 'help':
        print("You can go in the following directions: ")
        gset.inaction = True
        for direction in room_links :
            print(direction)
    elif direct_object in hidden_links and hidden_links[direct_object][1] in gset.player_inventory:
        gset.player_status[3] = hidden_links[direct_object][0]
        gset.player_status[2] += 2
    elif not direct_object in room_links :
        print('You cannot go ' + direct_object + ' from here.')
        gset.inaction = True
    else :
        gset.player_status[3] = room_links[direct_object]
    return True

commands['go'] = go # Key to the function call is name of function in a string.


# ---- HELP ---- #

def help(direct_object) :
    
    gset.inaction = True

    if direct_object == 'eat' :
        print('To eat something, the item has to be in the room you are in or in your inventory and be edible. Some things increase your energy or health. Others damage it. To eat it, type \'eat <item_to_eat>\'.')
    elif direct_object == 'fight' :
        print('Some things are worth fighting... others are not. Only some objects can be used to fight with and only some can be fought. Use the command \'fight <item_to_fight>\'. A prompt will appear, asking if you would like to fight with anything else. Some items can be used to increase your fighting strength.')
    elif direct_object == 'get' :
        print('This command allows you to pick up an object and store it in your inventory. Type \'get <item_to_get>\'.')
    elif direct_object == 'go' :
        print('To go somewhere, type \'go <direction_to_go>\'.')
    elif direct_object == 'look' :
        print('There are several things you can look at: your inventory (inventory), the room (room), or an item (<item_name>). Use \'look <what_to_look_at>\'.')
    elif direct_object == 'open' :
        print('Perhaps some things can be opened...? You\'ll have to find out.')
    elif direct_object == 'quit':
        print('You don\'t want to give up, do you?')
    elif direct_object == None :
        print(' ')
        print('Help Directory')
        print('eat <edible_item> -- Eat an item.')
        print('fight <fightable_item> -- Fight an item or person.')
        print('get <accessible_item> -- Add item to inventory.')
        print('go <direction> -- Move around the map.')
        print('help -- View help directory.')
        print('help <command_name> -- View detailed help about a specific command.')
        print('look (inventory, room, or <item>) -- Take a closer look.')
        print('open <openable_item> -- Open an item.')
        print('quit -- Exit the game.')
        print(' ')

    return True

commands['help'] = help # -- Key to the function call as name of function in string.


# --- LOOK --- #

def look(direct_object) :
    room_id = gset.player_status[3]
    room_inventory = inv_to_eng([item for item in gset.game_map[room_id]['inventory'] if items[item]['look']])
    gset.inaction = True
    if direct_object == None :
        print('You must specify what to look at (room or inventory)')
    elif direct_object == 'room':
        print(gset.game_map[room_id]['description'])
        if len(room_inventory) == 0 :
            print('You don\'t see anything in the room.')
        else :
            print('In this room you see ' + list_to_eng(room_inventory) + '.')
    elif direct_object == 'inventory':
        if len(gset.player_inventory) == 0 :
            item_list = 'nothing'
        else :
            item_list = ', '.join(gset.player_inventory)
        print('You have ' + item_list + ' in your inventory')
    elif direct_object in gset.game_map[room_id]['inventory'] or direct_object in gset.player_inventory:                                                                              
        if direct_object in items :
            if direct_object in item_inventories and items[direct_object]["opened"]:
                print(items[direct_object]['description'](direct_object, inv_to_eng(item_inventories[direct_object])))
            else:
                print(items[direct_object]['description'])
        else :
            print('Oops! That item is supposed to be in the game code, but it\'s not. Please report this to the developers with error code: missing_inventory_item.')
    else :
        print('You cannot look at ' + direct_object + '.')
    return True

commands['look'] = look # -- Key the function with its name in a string.


# ---- OPEN ---- #

def open(direct_object):
    room_id = gset.player_status[3]
    room_inventory = [item for item in gset.game_map[room_id]['inventory']]
    if direct_object == None:
        print("You must specify what to open.")
        gset.inaction = True
    elif (direct_object == 'big cabinet' or direct_object == 'small cabinet') and direct_object in room_inventory:
        items[direct_object]['opened'] = True
        items[direct_object]['description'] = items[direct_object]['alt_desc']
        print("You open the " + direct_object + ".")
    elif direct_object in openable_items and direct_object in room_inventory:
        print("What do you want to open the " + direct_object + " with?")
        tool = input()
        if tool == openable_items[direct_object] and tool in gset.player_inventory:
            items[direct_object]['opened'] = True
            items[direct_object]['description'] = items[direct_object]['alt_desc']
            gset.player_status[2] += 1
            gset.player_inventory.remove(tool)
            print("You open the " + direct_object + " with the " + tool + '.')
        elif tool not in gset.player_inventory:
            print("The " + tool + " is not in your inventory.")
            gset.inaction = True
        else:
            print("That fails to open the " + direct_object + '.')
            # Note that we are not including the gset.inaction = True line here because you actually did something manual
    elif direct_object not in room_inventory :
        print("There is no " + direct_object + " in this room.")
        gset.inaction = True
    else:
        print("You cannot open this item.")
        gset.inaction = True
    return True

commands['open'] = open # Key the function call by its name in a string.


# ---- QUIT --- #

def quit(direct_object) :
    if direct_object == None:
        return False
    else:
        print('Type only \'quit\' to quit.')

commands['quit'] = quit # Key the function call by its name in a string.

