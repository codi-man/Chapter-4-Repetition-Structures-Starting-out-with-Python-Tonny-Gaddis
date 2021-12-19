#Q12 - Write a program that uses nested loops to draw this pattern:

rows=int(input('Enter number of rows: '))
for x in range(rows,-1,-1):
    print('*'*(x+1))