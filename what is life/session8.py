# C4T List Create

    # 0
array = ["apple", "banana", "orange"]
array.append("grapefruit")
print(array)

    # 1
array = ["apple", "banana", "orange"]
fav = input("Add a thing you like!\nThing: ")
array.append(fav)
print("New list of your favourite fruits!\n{0}".format(array))



# C4T List read & index
    # Clean print

        # 1
array = ["dogs", "cats", "sweets"]
new = input("Add a thing that you like: ")

array.append(new)
string = ""

for i in array:
    print(i, end = " ")

        # 2
array = ["dogs", "cats", "sweets"]
new = input("Add a thing that you like: ")

array.append(new)
string = ""

for i in array:
    print(i, end = ", ")

        # 3
array = ["dogs", "cats", "sweets"]
new = input("Add a thing that you like: ")

array.append(new)
string = ""

for i in array:
    print(i, end = " | ")

    # List read

        # 4
array = ["dogs", "cats", "sweets"]
new = input("Add a thing that you like: ")
print(array[0], array[len(array - 1)], array[len(array - 2)])

        # 5
array = ["dogs", "cats", "sweets"]
new = input("Add a thing that you like: ")
print(array[0].upper(), array[len(array - 1)].upper(), array[len(array - 2)].upper())



# List update
    # 1
array = ["dogs", "cats", "sweets"]
new = input("Add a thing that you like: ")
array[0] = new
print(array)

    # 2
array = ["dogs", "cats", "sweets"]
array[len(array) - 1] = "h"
print(array)

    # 3
array = ["dogs", "cats", "sweets"]
pos = input("Position: ")
new = input("Add a thing that you like: ")
array[int(pos)] = new
print(array)



# List delete
    # 1
array = ["dogs", "cats", "sweets"]
array.pop(1)
print(array)

    # 2
array = ["dogs", "cats", "sweets"]

if array.count("dog") > 0:
    array.remove("dog")
    print(array)
else:
    print("Value 'dog' is not in list.")

    # 3
array = ["dogs", "cats", "sweets"]
remove = input("Give index of what you want to delete in list.\nIndex: ")

if remove.isdigit() == False:
    print("Not a valid index.")
elif int(remove) > len(array) - 1:
    print("Index not available.")
else:
    print("Removing the item '{0}' out of the list..".format(array[int(remove)]))
    array.pop(int(remove))
    print(array)

    # 4
array = ["dogs", "cats", "sweets"]
remove = input("Give the object of what you want to delete in list.\nName: ")

if array.count(remove) < 1:
    print("There's no object with that value.")
else:
    print("Removing item '{0}' from the list..".format(remove))
    array.remove(remove)
    print(array)



# List FOR
    # 1 (ADD 3)
array = array = ["dogs", "cats", "sweets"]
add = 0

print(array)

while add < 3:
    ad = input("Add more to the list!\nThing: ")
    if len(ad) < 1:
        print("Add a value, would you?\nThing: ")
    else:
        array.append(ad)
        print(array)
        add += 1

for x in array:
    print(x)

    # 2 (CAPITALISE)
array = array = ["dogs", "cats", "sweets"]

for x in array:
    print(x.upper())

    # 3 (BULLETS)
array = array = ["dogs", "cats", "sweets"]

for x in range(0, len(array)):
    print("{0}. {1}".format(x+1, array[x]))

    # 4 (SELECTION)
array = array = ["dogs", "cats", "sweets"]

for x in array:
    if x.count("e") > 0 or x.count("E") > 0:
        print(x.upper())



# CRUD
    # 1
array = ["dogs", "cats", "sweets"]

while True:
    command = input("Input either 'C', 'R', 'U' or 'D'.\nYour input: ")

    if command.lower() == "c":
        print(array)
        add = input("Would you like to add something to the list?\nThing to add: ")

        while len(add) < 1:
            add = input("A valid change, please.\nEnter the changes you'd like to commit: ")
            if len(add) > 0:
                break

        array.append(add)
        print("New list: {0}".format(array))
    
    if command.lower() == "r":
        if len(array) < 1:
            print("There're no items in this list.")
        else:
            for x in array:
                print(x)

    if command.lower() == "u":
        print(array)
        index = input("Enter the index where you would want to commit changes: ")

        while index.isdigit() == False or int(index) < 0 or int(index) > len(array) - 1:
            index = input("Cannot find that index.\nEnter the index where you would want to commit changes: ")
            if index.isdigit() == True and int(index) > -1 and int(index) < len(array):
                break

        change = input("Enter the changes you'd like to commit: '{0}' -> ".format(array[int(index)]))
        while len(change) < 1:
            change = input("A valid change, please.\nEnter the changes you'd like to commit: ")
            if len(change) > 0:
                break

        array[int(index)] = change
        print("New list: {0}".format(array))

    if command.lower() == "d":
        print(array)
        index = input("Enter the index where you would want to delete the item: ")

        while index.isdigit() == False or int(index) < 0 or int(index) > len(array) - 1:
            index = input("Cannot find that index.\nEnter the index where you would want to delete the item: ")
            if index.isdigit() == True and int(index) > -1 and int(index) < len(array):
                break

        print("You'll be deleting '{0}'.".format(array[int(index)]))
        array.pop(int(index))
        print("New array: {0}".format(array))

        

# String n List
    # 1 (Split with ',')
things = input("Things that you like: ")

array = things.split(',')
print("Your things: ")

for x in array:
    print(x)

    # 2 (SHUFFLE WORDS)
import random
word = input("Enter your word: ")

array = list(word)
random.shuffle(array)
print("Your shuffled word: ")

for x in array:
    print(x)

    # 3 (SHUFFLE GAME)
import random

words = ["unique", "abstract", "friendly", "overwhelming", "cute", "charming", "optimistic", "bright", "pretty", "fancy", "fantastic", "extraordinary"]
score = 0
question = 0
lives = 3
print("Welcome to Jumble! All you need to do is to rearrange the jumbled words!\n")

while True:
    chosen = words[random.randint(0, len(words) - 1)]
    chosen2 = list(chosen)
    random.shuffle(chosen2)
    chosen2 = "".join(chosen2)
    answer = input("Q{0}: {1}\nYour answer: ".format(question, chosen2))

    if answer.lower() == chosen:
        score += len(chosen)
        question += 1
        print("Way to go!\nScore: {0}".format(score))
    else:
        lives += -1
        if lives > 0:
            print("Wrong! The answer is '{0}'.\nYou now have {1} live(s).".format(chosen, lives))
        else:
            print("Wrong! The answer is '{0}'.\n".format(chosen))
            break

print("You lost!\nQuestions answered: {0}\nScore: {1}".format(question, score))