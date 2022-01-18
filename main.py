import math

fruits = ["apple","pears", "grapes", "melons"]
vegetables = ["carots","potatoes","turnips","onions"]
nums = [7,5,4,2,5,7,88,5,4,2,4,6,7,8,6,5,4,3,2,5,7,8,6,4]

# food = [fruits,vegetables]
# print(food)
#
# for fruit in fruits:
#     print(fruit)
#
# for i in range(len(food)):
#     for j in range(len(food[i])):
#         print(food[i][j])

# print(nums)
# largest = 0
# for num in nums:
#     if num > largest:
#         largest = num
#
# print(largest)
#
# total = 0
# for i in range(1,101):
#     total += i
# print(total)
#

# total = 0
# for i in range(0,101,2):
#     total += i
# print(total)


# count = 0
# for i in range(1,101):
#     str = ""
#     if (i % 3 == 0):
#         str += f"fizz"
#         print(str)
#     if (i % 5 == 0):
#         str += f"buzz"
#         print(str)
#     if (str == ""):
#         str += f"{i} not fizzy"
#         print(str)


# Password Generator Project
#
# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
#
# print("Welcome to the PyPassword Generator!")
# nr_letters= int(input("How many letters would you like in your password?\n"))
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))
#
# newpass = []
# totalChars = nr_numbers+nr_symbols+nr_letters
#
# for i in range(1,nr_letters+1):
#     ranLet = letters[random.randint(0, len(letters)-1)]
#     newpass.append(ranLet)
# for i in range(1,nr_numbers+1):
#     ranNums = random.choice(numbers)
#     newpass += ranNums
# for i in range(1,nr_symbols+1):
#     ranSyms = random.choice(symbols)
#     newpass += ranSyms
#
# random.shuffle(newpass)
#
# shufPasss = ""
# for i in newpass:
#     shufPasss += i
#
# print(shufPasss)

def isPrime(num):
    if num == 1:
        return "less than 1"
    else:
        for i in range(2, int(num/2)):
            if num % i == 0:
                print(i)
                return "this is not a prime number"
        else:
            return "this is a prime number"

print(isPrime(51))

