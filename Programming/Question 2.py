#Q2 - Write a program that asks the user to enter the amount that he or she has budgeted for a month.
#A loop should then prompt the user to enter each of his or her expenses for the month and keep a running total.
#When the loop finishes, the program should display the amount that the user is over or under budget.

budget=int(input('Enter your Budget($):'))
total=0
Number_of_items=int(input('Enter Number of Items purchased this month:'))
for x in range(Number_of_items):
    item=int(input('Price of Item:'))
    total+=item
print('The total Budget For The Month is',total,'$')
if total>budget:
    print('You are Over Budget')
else:
    print('You are Under Budget')