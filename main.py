import math

print("Welcome to the tip calculator")
total = float(input("What was the total bill? "))
people = int(input("How many people to split the bill? "))
tip = float(input("how much would you like to tip? "))
cost = ((total * (1 + (tip/100)))/people)
cost = "{:.2f}".format(cost)
print(cost)


number = input("enter your number : ")
firstNumber = int(number[0])
secNumber = int(number[1])
total = firstNumber + secNumber
print("the total is " + str(total))

print("BMI Calculator")
weight = input("enter your weight in kilos : ")
height = input("enter your height in metres : ")

bmi = (float(weight)/(float(height) ** 2))
print(int(bmi))

print(f"your score is {int(bmi)}")

print("Your life in weeks")
age = int(input("how old are you? "))
timeLeft = 90 -age

days = timeLeft * 365
weeks = timeLeft * 52
months = timeLeft * 12

print(f"you have {days} days or {weeks} weeks or {months} months to live")