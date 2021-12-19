#Q5 - Write a program that displays a table of the Celsius temperatures 0 through 20 and their Fahrenheit equivalents.

ranges = int(input("Enter the final temperature: "))
print('CELCIUS','\t','FAHRENHEIT')
print('---------------------------')

for celcius in range(1,ranges+1):
    f=(9/5)*celcius+32
    print(celcius,'\t\t',round(f,2))