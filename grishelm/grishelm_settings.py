import os

def init():
    
    # Initialize all the variables as global variables.
    global player_status, player_inventory, game_continues, inaction, ungardened, vines_alive, reunited, won, game_map, end
    

    # Make the game map.
    # The game map is a dictionary from room identifiers (R0 etc)
    # to a dictionary per room. A room's dictionary has keys
    # for the name of the room, a description, the room's
    # inventory, and the room's links.

    game_map = {}

    directory = os.fsencode("\grishelm\map")
    
    for file in os.listdir("C:\\Users\\PeterLogan\\StarlightAndAshes\\grishelm\\map"):
        area_id = 'C:\\Users\\PeterLogan\\StarlightAndAshes\\grishelm\\map\\' + os.fsdecode(file)
        # Read in the name, description, and inventory of each room
        with open(area_id) as room_file :
            room_lines = room_file.readlines()
            print(room_lines)
            game_map[os.fsdecode(file)] = {'name':room_lines[0].rstrip(),
                             'description':room_lines[1].rstrip(),
                             'inventory':room_lines[2].rstrip().split(','),
                             'links': {v:k for (k,v) in zip(room_lines[3].rstrip().split(','), room_lines[4].rstrip().split(','))},
                             'hidden_links': {k:v for (k,v) in zip(room_lines[5].rstrip().split(','), [[(i for i in room_lines[6].rstrip().split(',')), (j for j in room_lines[7].rstrip().split(','))]])}
                            }
            if game_map[os.fsdecode(file)]['inventory'] == [''] :
                game_map[os.fsdecode(file)]['inventory'] = []

    '''for i in range(11):
        room_id = 'R'+str(i)
        # Read in the name, description, and inventory of each room
        with open(room_id) as room_file :
            room_lines = room_file.readlines()
            game_map[room_id] = {'name':room_lines[0].rstrip(),
                             'description':room_lines[1].rstrip(),
                             'inventory':room_lines[2].rstrip().split(','),
                             'links': {k:v for (k,v) in zip(room_lines[3].rstrip().split(','), room_lines[4].rstrip().split(','))},
                             'hidden_links': {k:v for (k,v) in zip(room_lines[5].rstrip().split(','), [[(i for i in room_lines[6].rstrip().split(',')), (j for j in room_lines[7].rstrip().split(','))]])}
                            }
            if game_map[room_id]['inventory'] == [''] :
                game_map[room_id]['inventory'] = []'''
    

    # ----- PLAYER ----- #

    # Player status: health, energy, accomplishment, and current room.
    player_status = [10,10,0, 'C2']
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