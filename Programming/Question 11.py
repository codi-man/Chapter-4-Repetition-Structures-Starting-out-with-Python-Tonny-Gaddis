#Q11 – Write a program that predicts the approximate size of a population of organisms.
#The application should use text boxes to allow the user to enter the starting number of organisms,
#the average daily population increase (as a percentage), and the number of days the organisms will be left to multiply.
#For example, assume the user enters the following values:

#Starting number of organisms: 2 Average daily increase: 30% Number of days to multiply: 10

number=int(input('Starting number of organisms: '))
percentage=int(input('Average daily increase: '))
days=int(input('Number of days: '))

print('Days Approximate','\t','Population')
print('-------------------------------------')
 
for x in range(1,days+1):
    a= number*percentage/100
    number=number+a
    print(x, '\t', format(number, ',.1f'))