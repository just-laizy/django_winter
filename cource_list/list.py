# !!! list introduction !!! 

# numbers = [1,2,3,4,5]
# strings = [" hi ", "bye"]
# bools = [True , False]

# mix = ["Python ", True ,23]

# print(f"{numbers}\n{strings}\n{bools}\n{mix}")
# print(type(bools))

# list1

# name = input("Name please : ")
# surname = input("surname please : ")
# students=[]
# students.append(name)
# students.append(surname)

# print(students)

# list2
c = int(input("How many people do you want to enter : "))
print(f"You must enter {c} people")
lists = []

for i in range(c):
    c1 = input("Name : ")
    c2 = input("surname : ")
    lists.append(c1)
    lists.append(c2)
print(lists)


