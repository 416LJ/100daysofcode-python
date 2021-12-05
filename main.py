# size = input("Size? S? M? L? ")
# total = 0
#
# topping = input("Pepperoni? Y? N?")
# if topping == "Y" or topping == "y":
#     topping = True
#
# cheese = input("Extra Cheese? Y? N?")
# if cheese == "Y" or cheese == "y":
#     cheese = True
#
# if size == "S" or size == "s":
#     total = 15
#     if cheese == True:
#         total += 1
#     if topping == True:
#         total += 2
#
# if size == "M" or size == "m":
#     total = 20
#     if cheese == True:
#         total += 1
#     if topping == True:
#         total += 3
#
# if size == "L" or size == "l":
#     total = 25
#     if cheese == True:
#         total += 1
#     if topping == True:
#         total += 3
#
# print(f"the total is ${round((total*1.13),2)}")

# print("Welcome to the love the Calculator")
# name1 = input("enter first persons name : ")
# name2 = input("enter second persons name : ")
# newName = name1 + name2
# countTrue = newName.count("t")
# countTrue += newName.count("r")
# countTrue += newName.count("u")
# countTrue += newName.count("e")
# print(countTrue)
# countLove = newName.count("l")
# countLove += newName.count("o")
# countLove += newName.count("v")
# countLove += newName.count("e")
# print(countLove)

print('''
888                                                          
888                                                          
888                                                          
888888888d888 .d88b.  8888b. .d8888b 888  888888d888 .d88b.  
888   888P"  d8P  Y8b    "88b88K     888  888888P"  d8P  Y8b 
888   888    88888888.d888888"Y8888b.888  888888    88888888 
Y88b. 888    Y8b.    888  888     X88Y88b 888888    Y8b.     
 "Y888888     "Y8888 "Y888888 88888P' "Y88888888     "Y8888 
''')
print("welcome to treasure island")
direction = input("left or right? ").lower()
if direction == "right":
    print("game over")
    exit()
elif direction == "left":
    swim = input("swim or wait? ").lower()
    if swim == "swim":
        print("game over")
        exit()
    elif swim == "wait":
        door = input("red or blue or yellow door? ").lower()
        if door == "red":
            print("game over")
            exit()
        elif door == "blue":
            print("game over")
            exit()
        elif door == "yellow":
            print("you win!")

name = input("enter your name in the Hall of Fame").upper()
print(f"Congratulations\n{name}\nYou are now in the Hall of Fame")