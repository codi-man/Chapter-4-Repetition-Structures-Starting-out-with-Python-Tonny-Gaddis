#Q7 - Running on a particular treadmill you burn 4.2 calories per minute.
#Write a program that uses a loop to display the number of calories burned after 10, 15, 20, 25, and 30 minutes.

calories = 4.2
start_value = int(input("Enter starting value: "))
stop_value = int(input("Enter stopping value: "))
step_value = int(input("Enter stepping value: "))

for i in range(start_value,stop_value+1,step_value):
    calories_burned = i*calories
    print("Total calories burned:",calories_burned)