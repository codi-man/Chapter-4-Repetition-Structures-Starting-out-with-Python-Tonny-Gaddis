#Q7 – Write a program with a loop that asks the user to enter a series of positive numbers.
#The user should enter a negative number to signal the end of the series.
#After all the positive numbers have been entered, the program should display their sum.

#doesnt sum sepearatly
a=int(input('Enter Series of Numbers: '))
total=0
while a!=0:
    for x in range(a):
        s=int(input('Enter value: '))
        total=total+s
    print('Amount:',total)
    
    a=int(input('Enter Series of Numbers or Enter 0 to Exit: '))