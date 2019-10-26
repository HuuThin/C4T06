print("Hello there! You seem like a new person here. Introduce yourself.\nEnter your name.\n")
name = raw_input("Your name: ")

print("\nSo, your name is {0}. Enter your birth year.".format(name))

year = raw_input("Your birth year: ")
age = 2019 - int(year) + 1

print("\nOooh, so your birth year is {0}.\n...\nWait.. is that all? I thought this thing was programmed to be more specific..".format(age))