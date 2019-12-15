import random

# Initial settings
game = {
    "player": "P",
    "inventory": [],
    "key": "K",
    "key_count": 3,         # How many keys do you need to unlock the exit?
    "exit": "E",
    "wall": "W",
    "wall_count": 1,        # How many walls are there?
    "map": ["P", "E"],
    "over": False
}

def start_game(game):

    # Add keys into the map
    for x in range(game["key_count"]):
        game["map"].append("K")

    # Add walls into the map
    for x in range(game["wall_count"]):
        game["map"].append("W")

    # Appending 33 '-'s into the map (therefore getting 36 cells)
    for x in range(36 - len(game["map"])):
        game["map"].append("-")

    # Shuffle the entire map
    random.shuffle(game["map"])

    # Print the map
    def print_map(map):
        map_print = ""
        for x in range(36):
            if x % 6 == 0:
                map_print += "\n\n {0}  ".format(map[x])
            else:
                map_print += " {0}  ".format(map[x])
        return "Key : K\nExit: E\nWall: W\nYou : P{0}".format(map_print)

    def move(move, index, map):
        if map[index + move] == "E":
            if game["inventory"].count("K") < game["key_count"]:
                print("\nYou don't have enough keys ({0}/{1})! Try and find some!".format(game["inventory"].count("K"), game["key_count"]))
            else:
                print("\nCongratulations, you found the exit!")
                map[index + move] = "E"
                map[index] = "-"
                game["over"] = True
        if map[index + move] == "K":
            game["inventory"].append("K")
            print("\nYou found a key!")
            map[index + move] = "P"
            map[index] = "-"
        if map[index + move] == "W":
            print("\nYou can't pass through a wall!")
        if map[index + move] == "-":
            map[index + move] = "P"
            map[index] = "-"
        print(print_map(map))

    def act(action, map):
        valid = False
        index = map.index("P")
        while valid == False:
            if action == "w":
                if map.index("P") < 6:
                    action = input("Invalid move.\n[W] UP | [A] LEFT | [S] DOWN | [D]: RIGHT\nYour move: ")
                else:
                    valid = True
                    move(-6, index, map)
            elif action == "a":
                if map.index("P") % 6 == 0:
                    action = input("Invalid move.\n[W] UP | [A] LEFT | [S] DOWN | [D]: RIGHT\nYour move: ")
                else:
                    valid = True
                    move(-1, index, map)
            elif action == "s":
                if map.index("P") > 29:
                    action = input("Invalid move.\n[W] UP | [A] LEFT | [S] DOWN | [D]: RIGHT\nYour move: ")
                else:
                    valid = True
                    move(6, index, map)
            elif action == "d":
                index2 = map.index("P")
                if index2 == 5 or index2 == 11 or index2 == 17 or index2 == 23 or index2 == 29 or index2 == 35:
                    action = input("Invalid move.\n[W] UP | [A] LEFT | [S] DOWN | [D]: RIGHT\nYour move: ")
                else:
                    valid = True
                    move(1, index, map)

    print(print_map(game["map"]))

    while game["over"] == False:
        action = input("[W] UP | [A] LEFT | [S] DOWN | [D]: RIGHT\nYour move: ")
        valid = False
        while valid == False:
            if action.isalpha() == True:
                action = action.lower()
                if action == "w" or action == "a" or action == "s" or action == "d":
                    act(action, game["map"])
                    valid = True
                else:
                    action = input("Invalid move.\n[W] UP | [A] LEFT | [S] DOWN | [D]: RIGHT\nYour move: ")
            else:
                action = input("Invalid move.\n[W] UP | [A] LEFT | [S] DOWN | [D]: RIGHT\nYour move: ")

if game["key_count"] < 1:
    print("Key count must be greater than 0! Check your game setup.")
else:
    start_game(game)