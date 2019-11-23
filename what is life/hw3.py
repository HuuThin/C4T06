# 1
for x in range(0, 7):
    text = "*" * (7 - x)
    print(text)

# 2
numbers = []
main = input("Input a number.\nInput: ")
state = False

while state == False:
    if main.isnumeric():
        numbers.append(int(main))
        main = input("Numbers: {0}\nWould you like to input more numbers? Type 'exit' to cancel.\nYour input: ".format(numbers))
    else:
        if main.lower() == "exit":
            if len(numbers) > 0:
                state = True
                break
            else:
                print("At least input a number..")
                main = input("Input: ")
        else:
            print("Bad! That wasn't a number! Try again.")
            main = input("Input: ")

total = 0

for x in range(0, len(numbers)):
    total = total + numbers[x]

print("Numbers: {0}\nTotal: {1}\nAverage: {2}".format(numbers, total, total/len(numbers)))

# 3
year = input("Input a year.\nInput: ")

while True:
    if year.isnumeric():
        break
    else:
        print("That's not a valid year.")

if int(year) % 4 != 0:
    print("The year {0} is not a leap year.".format(year))
else:
    if int(year) % 100 == 0:
        if int(year) % 400 == 0:
            print("The year {0} is a leap year.".format(year))
        else:
            print("The year {0} is not a leap year.".format(year))
    else:
        print("The year {0} is a leap year.".format(year))

# 4
from math import sqrt
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if a == 0:
    if b == 0:
        if c == 0:
            print("Infinite solutions.")
        else:
            print("No solutions.")
    else:
        if c == 0:
            print("There's 1 root: x = 0.")
        else:
            print("There's 1 root: x = {0}.".format(-c/b))
else:
    if b == 0:
        if c == 0:
            print("There's 1 root: x = 0.")
        else:
            d = b^2 - 4*a*c
            if d < 0:
                print("No real roots.")
            else:
                sol1 = (-b + sqrt(b^2 - 4*a*c)) / (2 * a)
                sol2 = (-b - sqrt(b^2 - 4*a*c)) / (2 * a)
                print("Two solutions: {0} and {1}.".format(sol1, sol2))
    else:
        if c == 0:
            print("Two solutions: {0} and {1}".format(-b/a, "0"))
        else:
            d = b * b - (4*a*c)
            if d < 0:
                print("No real roots.")
            else:
                sol1 = (-b + sqrt(b * b - 4*a*c)) / (2 * a)
                sol2 = (-b - sqrt(b * b - 4*a*c)) / (2 * a)
                print("Two solutions: {0} and {1}.".format(sol1, sol2))