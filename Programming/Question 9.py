#Q9 – At one college, the tuition for a full-time student is $8,000 per semester.
#It has been announced that the tuition will increase by 3 percent each year for the next 5 years.
#Write a program with a loop that displays the projected semester tuition amount for the next 5 years.

tution=8000
number_of_years = int(input("Enter of years: "))
print('YEAR','\t','TUTION')
print('-----------------')
    
for x in range(1,number_of_years+1):
    percent_increase = tution*0.03
    total = tution+percent_increase
    print(x,'\t',total)