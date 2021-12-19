#Q2 - Write a program that accepts two numbers by the user, checks if the denominator is zero,
#divides them and then prints their division. If the denominator is zero,
#it should prompt the user “Division is not possible”.

#Answer:

#1 .	Write a program that accepts two numbers by the user
#2 .	It will divide them and then prints their division.
#3 .	If the denominator is zero, it should prompt the user “Division is not possible”.

number_1 = int(input("Enter the first number: "))
number_2 = int(input("Enter the second number: "))

if number_2==0:
    print("Division is not possible")
else:
    division = number_1/number_2
    print(division)