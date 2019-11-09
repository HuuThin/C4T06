# b1
print("b1: Your name and age, please.")
name = input("Name please.\nName: ")
age = input("Age please.\nAge: ")

print("I'm {0}, I'm {1} years old.".format(name, age))

# b2
print("b2: a (+-*/) b")
a = 5
b = 4
print("a + b = {0}\na - b = {1}\na * b = {2}\na / b = {3}".format(a+b, a-b, a*b, a/b))

# b3
print("b3: The average of two numbers")
a = int(input("First number: "))
b = int(input("Second number: "))
c = (a+b)/2
print("Average: {0}".format(c))

# b4
print("b4: something idk")
a = int(input("First number: "))
b = int(input("Second number: "))
p = a*b
s = a+b
q = 2*s + p * (s - a) * (p + b)
print("{0} {1} {2}".format(p, s, q))

# b5
print("b5: That scary Lorem Ipsum paragraph")
para = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
paraNew = para.replace(",", ".")
length = len(para)
print("Number of times the word 'Lorem' existed: {0}".format(para.count("Lorem")))
print("Paragraph length: {0}".format(length))
print(paraNew)