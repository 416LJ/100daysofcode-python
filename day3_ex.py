import random
print("ROCK, PAPER, SCISSORS")

sign = int(input("ENTER : 1 FOR ROCK, 2 FOR PAPER, 3 FOR SCISSORS : "))
if sign == 1:
    rock = sign
    print(f"you entered rock")
elif sign == 2:
    paper = sign
    print(f"you entered paper")
elif sign == 3:
    scissors = sign
    print(f"you entered scissors")
else:
    print("invalid input, please enter a number between 1-3")

compSign = random.randint(1,3)
if compSign == 1:
    rock = compSign
    print(f"comp chose rock")
elif compSign == 2:
    paper = compSign
    print(f"comp chose paper")
elif compSign == 3:
    scissors = compSign
    print(f"comp chose scissors")


if sign == 1 and compSign == 3:
    print("you win")
elif compSign == 1 and sign == 3:
    print("you lose")
elif compSign > sign:
    print("you lose")
elif sign > compSign:
    print("you win")
elif compSign == sign:
    print("tie game")

row_1 = [" "," "," "]
row_2 = [" "," "," "]
row_3 = [" "," "," "]
map = [row_1,row_2,row_3]
print(f"{row_1}\n{row_2}\n{row_3}")


for i in range(10):
    position = input("enter row first then column with a space : ")
    sign = input("enter x or o : ")
    position = position.split()
    print(position)
    row = int(position[0])
    column = int(position[1])
    map[row - 1][column - 1] = sign
    print(f"{row_1}\n{row_2}\n{row_3}")


names = input("enter names separated by commas : ")


names = names.split()
print(names)

winner = random.randint(0, len(names)-1)
print(f"{names[winner]} is paying for the meal")


winner = random.choice(names)
print(f"{winner} is paying for dinner today")

