from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

commands = {}

for k, v in {
    ('n', 'north'): 'n_to',
    ('s', 'south'): 's_to',
    ('e', 'east'): 'e_to',
    ('w', 'west'): 'w_to',
    ('q', 'quit', 'exit', 'leave'): 'q',
    ('get', 'pickup', 'take'): 'get',
    ('drop', 'leave'): 'drop',
    ('inventory', 'bag', 'items', 'inv', 'i'): 'inv',
    ('go', 'move', 'travel'): 'go'
}.items():
    for key in k:
        commands[key] = v


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

room['outside'].__items__ = [
    Item('Candy', "A tasty sweet"),
    Item('key', 'opens the special lock')
]

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
name = input("Greetings Adventurer! What is your name?: ")
new_player = Player(name, room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
selection = ""
print(new_player)
while(selection != 'q'):
    selection = str.lower(input("What do you do?::  "))
    selection = selection.split()
    command = commands.get(selection[0], "")
    if command == 'go':
        command = commands.get(selection[1], "")
    if command == 'q':
        print("Thank you for playing!")
    elif command == 'inv':
        print(new_player.viewInventory())
    elif command == 'get':
        print(new_player.get(selection[1]))
    elif command == 'drop':
        print(new_player.drop(selection[1]))
    else:
        print(new_player.move(command))
