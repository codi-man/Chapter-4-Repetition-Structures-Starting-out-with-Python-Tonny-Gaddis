#Q6 – Write a program that calculates the amount of money a person would earn over a period of time if his or her salary is
#one penny the first day, two pennies the second day, and continues to double each day.
#The program should ask the user for the number of days. Display a table showing what the salary was for each day,
#and then show the total pay at the end of the period. The output should be displayed in a dollar amount,
#not the number of pennies.

days=int(input('Enter Days:'))
total=0
for num in range(days):
    salary=2**num
    total=total+salary
    print(num+1,salary)
    dollars=total/100
print('Total Amount',dollars,'$')