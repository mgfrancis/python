# 1.
x = 5
y = 10
if 2 * x > 10:
    print("Question 1 works!")
else:
    print("oooo needs some work")
#Answer: 2*x = 10 so print("oooo needs some work") will run.

# 2.
x = 5
y = 10
if len("Dog") < x:
    print("Question 2 works!")
else:
    print("Still missing out")
#Answer:  Nothing will run because there's no "Dog" variable


# 3.
x = 2
y = 5
if (x ** 3 >= y) and (y ** 2 < 26):
    print("GOT QUESTION 3!")
else:
    print("Oh good you can count")
# Answer: x**3 = 8 and y**2 = 25 so print("GOT QUESTION 3!") will run.


# 4.
name = "Dan"
group_one = ["Greg", "Tony", "Susan"]
group_two = ["Gerald", "Paul", "Ryder"]
group_three = ["Carla", "Dan", "Jefferson"]

if name in group_one:
    print(name + " is in the first group")
elif name in group_two:
    print(name + " is in group two")
elif name in group_three:
    print(name + " is in group three")
else:
    print(name + " does not have a group")
#Answer: "Dan" is in group_three so print(name + " is in group three") will run.

# 5.
height = 66
age = 16
adult_permission = True

if (height > 70) and (age >= 18):
    print("Can ride all the roller coasters")
elif (height > 65) and (age >= 18):
    print("Can ride moderate roller coasters")
elif (height > 60) and (age >= 18):
    print("Can ride light roller coasters")
elif ((height > 50) and (age >= 18)) or ((adult_permission) and (height > 50)):
    print("Can ride bumper cars")
else:
    print("Stick to lazy river")
#Answer: none of the if/elif conditions hold true for both height and age so print("Stick to lazy river") will run.