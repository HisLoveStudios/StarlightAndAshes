'''
ITEM_DATA.PY

This file simply contains dictionaries for the properties of every item in the game.
The original item definitions are placed last because of the size of the dictionary,
except aliases, because they necessarily require using the item definition dictionary.
No functions are stored here, but ALL data having to do with objects is.
'''

from nlp_functions import *

# This dictionary allows items to be referenced by more than one name.
item_aliases = {
    'bread': 'loaf of bread',
    'poison': 'bottle of poison',
    'piece of cake': 'cake',
    'chairs': 'chair',
    'bar of soap': 'soap'
}

get_conditions = {
    
}

openable_items = {
    
}

item_inventories = {
    
}

# Set up item statistics.
# Each inventory item's fighting properties. [<fightable?>, <fight_advantage>, <health>, <damage>, <losable>]
# Each kind of food is associated with a list indicating [<how it tastes>, <how it affects health>, <how it affects energy>]
items = {
    'nothing' : {
        'description': 'What is nothing?',
        'fight': [False, 1, None, None, False],
        'food': None,
        'get': False,
        'look': False
        },
    'spinach': {
        'description': 'A nutritious, but bitter green.',
        'fight': [False, -4, None, None, True],
        'food': ['bitter',10, 3],
        'get': True,
        'look': True
        },
    'rat': {
        'description': 'A filthy vermin, but perhaps an ally.',
        'fight': [True, 3, 4, 4, False, 2],
        'food': None,
        'get': True,
        'look': True
        },
    'ice cream' : {
        'description': 'Sweet to the taste, bad for the health!',
        'fight': [False, -5, None, None, True],
        'food': ['very sweet', -1, 10],
        'get': True,
        'look': True
        },
    'bottle of poison': {
        'description': 'An alluring glass bottle, with purple fluid inside.',
        'fight': [True, 2, 0, None, True, 'Fighting with poison is a losing battle.'],
        'food': ['terrible', -10000000, 0],
        'get': False,
        'look': False
        },
    'fountain': {
        'description': 'An elegant statue of a bouquet of flowers, tinkling with water sounds. A coin lies in the bottom of the fountain.',
        'fight': None,
        'food': None,
        'get': False,
        'look': True
        },
    'coin': {
        'description': 'An ancient Roman coin. Must be worth a fortune.',
        'fight': [False, 0.5, None, None, False],
        'food': None,
        'get': True,
        'look': False
        },
    'orange tree': {
        'description': 'There are many different fruit trees here. You see an orange on this one.',
        'fight': None,
        'food': None,
        'get': False,
        'look': True
        },
    'pear tree': {
        'description': 'There are many different fruit trees here. You see a pear on this one.',
        'fight': None,
        'food': None,
        'get': False,
        'look': True
        },
    'apple tree': {
        'description': 'There are many different fruit trees here. You see an apple on this one.',
        'fight': None,
        'food': None,
        'get': False,
        'look': True
        },
    'apple': {
        'description': 'A common fruit of reddish and gold hue.',
        'fight': [False, 0.5, None, None, True],
        'food': ['sweet and crisp', 2, 6],
        'get': True,
        'look': False
        },
    'orange': {
        'description': 'A Christmas delight.',
        'fight': [False, 0.5, None, None, True],
        'food': ['tart', 1, 4],
        'get': True,
        'look': False
        },
    'pear': {
        'description': 'Alluring. Augustine\'s temptation.',
        'fight': [False, 0.5, None, None, True],
        'food': ['bittersweet', 1, 4],
        'get': True,
        'look': False
        },
    'bed': {
        'description': 'A neatly made bed, made with Chinese silk sheets and Ottoman covers.',
        'fight': [True, 0, 10000, 2, False, 10000],
        'food': None,
        'get': False,
        'look': True
        },
    'chest': {
        'description': 'A heavy chest of acacia wood, with a gold-embossed circular recess in the front with an image of a man.',
        'fight': None,
        'food': None,
        'get': False,
        'look': True,
        'opened': False,
        'alt_desc': lambda self, inv : interior_desc(self, inv, '') + " which looks as though it has been buried a long time." if len(inv) != 0 else interior_desc(self,inv)
        },
    'note': {
        'description': "The note reads, 'Dear Archibald Craven, we are eternally indebted to your wife's love of gardens. Please, sir, will you join us there in the Northeast? -Mary Lennox'",
        'fight': None,
        'food': None,
        'get': True,
        'look': True
        },
    'tile': {
        'description': 'A once beautiful tile has been broken to reveal a hidden safe.',
        'fight': None,
        'food': None,
        'get': False,
        'look': True
        },
    'toilet': {
        'description': 'Really, you wanted to look at a toilet?',
        'fight': None,
        'food': None,
        'get': False,
        'look': True
        },
    'bathtub': {
        'description': 'A quality bathtub with jets (very relaxing). At the side of the bathtub is a bar of soap.',
        'fight': None,
        'food': None,
        'get': False,
        'look': True
        },
    'sink': {
        'description': 'The sink is filled with a bowl of suspicious looking ramen.',
        'fight': None,
        'food': None,
        'get': False,
        'look': True
        },
    'ramen': {
        'description': 'This ramen has a mysterious odor.',
        'fight': [False,1,None,None,True],
        'food':['savory and tasty, but it has gone bad',-2,4],
        'get': True,
        'look': False
        },
    'soap': {
        'description': 'Some slippery soap slides in your hands.',
        'fight': [False,1,None,None,False],
        'food': ['Why did you try to eat soap?', 0, -4],
        'get': True,
        'look': False
        },
    'safe': {
        'description': 'A metal safe. What secrets does it hold?',
        'fight': None,
        'food': None,
        'get': False,
        'look': False,
        'opened': False,
        'alt_desc': lambda self, inv : interior_desc(self, inv)
        },
    'staff': {
        'description': 'Gandalf\'s staff, a powerful magical weapon',
        'fight': [False,25,None,None,False],
        'food': None,
        'get': False,
        'look': False
        },
    'troll': {
        'description': 'A hulking behemoth with a heart of gold stands before you.',
        'fight': [True,30,60,10,False,'You monster, you killed the kindly troll!'],
        'food': None,
        'get': True,
        'look': True
        },
    'desk': {
        'description': 'Subject to many years of use by Lord Archibald Craven, the desk is worn, having lost its initial luster and sheen. Who knows what was scratched across the papers that have sat on this desk throughout the years?',
        'food': None,
        'fight': None,
        'get': False,
        'look': True
        },
    'pen': {
        'description': 'An ivory fountain pen, formed from the tusk of one of General Zaroff\'s famed hunts. Who knows what it would be made from it he had chose to hunt another, more dangerous game that day? A useful weapon. After all, the pen is mightier than the sword.',
        'food': None,
        'fight': [False, 3, None, None, False],
        'get': True,
        'look': True
        },
    'files': {
        'description': 'Would you dare snoop in Lord Archibald Craven\'s private files?',
        'food': None,
        'fight': None,
        'get': True,
        'look': True
        },
    'books': {
        'description': 'A vast collection of books, "Wings of Dawn," "Chronicles of Narnia," "The Scarlet Letter," "The Phantom Tollbooth," and many others claim the shelves.',
        'food': None,
        'fight': [False, 5, None, None, False],
        'get': True,
        'look': True
        },
    'flowers': {
        'description': 'You bend and sniff the flowers. Their enticing aroma fills your mind with color. No wonder this place is one of healing.',
        'food': ['shockingly sweet',2,0],
        'fight': None,
        'get': True,
        'look': True
        },
    'chair': {
        'description': 'The hairs on the chair are all curiously brushed one way, as if someone had been sliding off them recently... and perhaps stifling giggles all the while.',
        'food': None,
        'fight': None,
        'get': False,
        'look': True
        },
    'Monet': {
        'description': 'Beautiful, miniature strokes and incredible color palattes blend to form scenes of gardens.',
        'food': None,
        'fight': None,
        'get': False,
        'look': True
        },
    'Van Gogh': {
        'description': 'Wild and wonderful, the man\'s turbulent personality is reflected in accurate proportions of flow.',
        'food': None,
        'fight': None,
        'get': False,
        'look': True
        },
    'Escher': {
        'description': 'You pull back the picture and see a sign saying, "This is a red herring."',
        'food': None,
        'fight': None,
        'get': False,
        'look': True
        },
    'Almanzo': {
        'description': 'A multi-talented farmer boy who could brave a raging blizzard to save a starving town AND make legendary pancakes.',
        'food': None,
        'fight': [True, 10, 30, 10, False, -30],
        'get': True,
        'look': True
        },
    'Archibald': {
        'description': 'A seemingly cranky old man, but kind at heart.',
        'food': None,
        'fight': None,
        'get': True,
        'look': True
        },
    'vase': {
        'description': 'Inside you see a shiny key.',
        'food': None,
        'fight': [False, 5, None, None, True],
        'get': True,
        'look': True
        },
    'old key': {
        'description': 'An old key that looks as if it had been buried a long time.',
        'food': None,
        'fight': None,
        'get': False,
        'look': False
        },
    'shiny key': {
        'description': 'A shiny, oiled key. Perhaps it opens something...',
        'food': None,
        'fight': None,
        'get': True,
        'look': False
        },
    'loaf of bread': {
        'description': 'Good homemade white bread.',
        'food': ['sweet and dry', 0, 6],
        'fight': None,
        'get': False,
        'look': False
        },
    'sweetbread': {
        'description': 'Good sweetbread, full of raisins.',
        'food': ['sweet and moist', 0, 8],
        'fight': None,
        'get': False,
        'look': False
        },
    'cake': {
        'description': 'A source of energy, at least.',
        'food': ['stale', 0, 6],
        'fight': None,
        'get': False,
        'look': False
        },
    'prisoner': {
        'description': 'A scraggly, devious human, lying on the floor.',
        'food': None,
        'fight': [True, 0, 15, 10, False, -7],
        'get': False,
        'look': True
        },
    'vines': {
        'description': 'The tangled vines cover an ancient wall. Ivy leaves coat the wall with bizarre patterns.',
        'food': None,
        'fight': [True,None,50,0,None,0],
        'get': False,
        'look': False
    },
    'hidden door': {
        'description': 'An ancient wooden door with a rusty keyhole.',
        'food': None,
        'fight': None,
        'get': False,
        'look': True
    },
    'big cabinet': {
        'description': 'A large cabinet that looks like it is filled with food.',
        'food': None,
        'fight': None,
        'get': False,
        'look': True,
        'opened': False,
        'alt_desc': lambda self, inv : interior_desc(self, inv)
    },
    'small cabinet': {
        'description': 'A small cabinet that may contain something special.',
        'food': None,
        'fight': None,
        'get': False,
        'look': True,
        'opened': False,
        'alt_desc': lambda self, inv : interior_desc(self, inv)
    },
    'Laura': {
        'description': 'A young farm girl looking for her bridegroom.',
        'food': None,
        'fight': [True, 10, 20, 100, False, -20],
        'get': True,
        'look': True
    }
}