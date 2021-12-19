#Q4 – Write a loop that asks the user to enter a number.
#The loop should iterate 10 times and keep a running total of the numbers entered.

# 1.	Write a loop that asks the user to enter a number.
# 2.	The loop will add the number and print the total of it 10 times.

total = 0

number_range = int(input("Enter number range: "))

for number in range(1,number_range+1):
    number = int(input("Enter a number: "))
    total+=number
print("Total is",total)