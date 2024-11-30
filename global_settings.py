'''
GLOBAL_SETTINGS.PY

This file contains all the initialization of the global variables for the game such as:
- Game map.
- Achievement booleans.
- Player stats.
'''

def init():
    
    # Initialize all the variables as global variables.
    global player_status, player_inventory, game_continues, inaction, ungardened, vines_alive, reunited, won, game_map, end
    

    # Make the game map.
    # The game map is a dictionary from room identifiers (R0 etc)
    # to a dictionary per room. A room's dictionary has keys
    # for the name of the room, a description, the room's
    # inventory, and the room's links.

    game_map = {}

    for i in range(11):
        room_id = 'R'+str(i)
        # Read in the name, description, and inventory of each room
        with open(room_id) as room_file :
            room_lines = room_file.readlines()
            game_map[room_id] = {'name':room_lines[0].rstrip(),
                             'description':room_lines[1].rstrip(),
                             'inventory':room_lines[2].rstrip().split(',')}
            if game_map[room_id]['inventory'] == [''] :
                game_map[room_id]['inventory'] = []


    # Set up the geography of the map, which rooms are linked to which other rooms
    game_map['R0']['links'] = {'N':'R4', 'SE': 'R1', 'SW': 'R7'}
    game_map['R1']['links'] = {'S':'R10', 'W':'R0'}
    game_map['R2']['links'] = {'W': 'R0'}
    game_map['R3']['links'] = {'W':'R4'}
    game_map['R4']['links'] = {'S':'R0', 'W':'R5', 'E':'R3'}
    game_map['R5']['links'] = {'E':'R4'}
    game_map['R6']['links'] = {'N':'R5'}
    game_map['R7']['links'] = {'S':'R8', 'E':'R0'}
    game_map['R8']['links'] = {'N':'R7'}
    game_map['R9']['links'] = {'E':'R10'}
    game_map['R10']['links'] = {'N': 'R1', 'W': 'R9'}
    game_map['R0']['hidden_links'] = {}
    game_map['R1']['hidden_links'] = {}
    game_map['R2']['hidden_links'] = {}
    game_map['R3']['hidden_links'] = {}
    game_map['R4']['hidden_links'] = {}
    game_map['R5']['hidden_links'] = {}
    game_map['R6']['hidden_links'] = {}
    game_map['R7']['hidden_links'] = {}
    game_map['R8']['hidden_links'] = {}
    game_map['R9']['hidden_links'] = {}
    game_map['R10']['hidden_links'] = {}
    game_map['R0']['hidden_links'] = {'NE': ['R2', 'old key']}
    

    # ----- PLAYER ----- #

    # Player status: health, energy, accomplishment, and current room.
    player_status = [10,10,0, 'R0']
    # Items the player has.
    player_inventory = []
    # Whether the game is over or not.
    game_continues = True

    # Identifying an action as a 'looking' action. (No energy decrease if it is.)
    inaction = False

    # ----- ACHIEVEMENTS ----- #
    ungardened = True
    vines_alive = True
    reunited = False
    won = False

    # ---- OTHER BOOLEANS ---- #
    end = True