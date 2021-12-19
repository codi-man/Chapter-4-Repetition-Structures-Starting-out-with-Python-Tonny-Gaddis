#Q1 - Write a while loop that lets the user enter a number.
#The number should be multiplied by 10, and the result assigned to a variable named product.
#The loop should iterate as long as product is less than 100.

#Answer:

# 1.	Write a program that ask the number from the user.

# 2 	The number will be multiplied by 10 as long as the product of the number is less than 100

number = int(input("Enter a number: "))
product = number*10

while product<=100:
    print(product)
    product*=10