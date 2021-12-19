#Q5 – Write a program that accepts a number entered by the user and validates if it is odd or even.
#If it is even, print a series up to 4 using range() and if it’s odd print a series up to 7.

#Answer:

# 1.	Program will accept a number entered by the user and validates if it is odd or even.
# 2.	If it is even, it will print a series up to 4 using range() function
# 3.	If it’s odd, it will print a series up to 7.

number = int(input("Enter a number: "))

if number%2 == 0:
    for i in range(4):
        print(number)
        number+=2
else:
    for i in range(7):
        print(number)
        number+=2