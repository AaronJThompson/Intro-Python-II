from room import Room
from player import Player
from item import Item
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                    "North of you, the cave mount beckons",
                    [
                        Item("Sword", "A steel greatsword"),
                        Item("Coins", "100 gold coins")
                    ]),

    'foyer':    Room("Foyer",
                    "Dim light filters in from the south. Dusty passages run north and east."),

    'overlook': Room("Grand Overlook",
                    "A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm."),

    'narrow':   Room("Narrow Passage",
                    "The narrow passage bends here from west to north. The smell of gold permeates the air."),

    'treasure': Room("Treasure Chamber",
                    "You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south."),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

player = Player(input("What's your name? "), room['outside'])

full_direction = {
    "n": "North",
    "e": "East",
    "s": "South",
    "w": "West",
}

def next_room(dir, current_room):
    direction = dir + "_to"
    return getattr(current_room, direction)

def move_player(ply, dir):
    room = next_room(dir, ply.current_room)
    if room:
        ply.current_room = room
        print(f"You move {full_direction[dir]} and find yourself somewhere new")
        return True
    else:
        return False
# Make a new player object that is currently in the 'outside' room.

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

done = False
help_string = """
Commands:
    n, e, s, w - to move in a direction specified
    get/take [ITEM NAME] - pickup item
    drop [ITEM NAME] - drop item
    i/inventory - list all items in inventory
    quit - to quit the game
    help - to view these commands again
"""
print(f"""
Welcome {player.name}!
{help_string}
""")

while not done:
    player.current_room.print()
    commands = input("Where would you like to go? ").strip().lower().split(" ")
    if commands[0] in ["n", "e", "s", "w"]:
        if move_player(player, commands[0]):
            continue
        else:
            print("There is no room that way")
            continue
    elif commands[0] in ["take", "give"]:
        inv = player.pickup_item(commands[1])
        if not inv:
            print(f"You tried to find a {commands[1]}, but there was none to be found")
            continue
    elif commands[0] == "drop":
        item = player.drop_item(commands[1])
        if not item:
            print(f"You don't have a {commands[1]} on you")
            continue
    elif commands[0] == "quit":
        done = True
        continue
    elif commands[0] == "help":
        print(help_string)
        continue
    else:
        print("Invalid command")
        continue