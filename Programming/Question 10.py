#Q10 – In mathematics, the notation n! represents the factorial of the nonnegative integer n.
#The factorial of n is the product of all the nonnegative integers from 1 to n.

number=int(input('Enter Number: '))
factorial=1

for x in range(1,number+1):
    factorial*=x
print('The Factorial of',number,'is',factorial)