size = input("Size? S? M? L? ")
total = 0

topping = input("Pepperoni? Y? N?")
if topping == "Y" or topping == "y":
    topping = True

cheese = input("Extra Cheese? Y? N?")
if cheese == "Y" or cheese == "y":
    cheese = True

if size == "S" or size == "s":
    total = 15
    if cheese == True:
        total += 1
    if topping == True:
        total += 2

if size == "M" or size == "m":
    total = 20
    if cheese == True:
        total += 1
    if topping == True:
        total += 3

if size == "L" or size == "l":
    total = 25
    if cheese == True:
        total += 1
    if topping == True:
        total += 3

print(f"the total is ${round((total*1.13),2)}")
