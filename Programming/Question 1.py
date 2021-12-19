#Q1 - A bug collector collects bugs every day for five days. Write a program that keeps a running total of the number 
#of bugs collected during the five days. The loop should ask for the number of bugs collected for each day, and when 
#the loop is finished, the program should display the total number of bugs collected.

num = 0.0

nugs_collected = int(input("Enter number of days: "))

for i in range(nugs_collected):
    bugs = int(input("Enter number of bugs collected: "))
    num+=bugs
print("Total bugs collected are",num)
