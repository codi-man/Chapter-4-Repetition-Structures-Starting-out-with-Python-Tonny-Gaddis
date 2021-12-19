#Q8 - Assuming the ocean’s level is currently rising at about 1.6 millimeters per year, create an application
#that displays the number of millimeters that the ocean will have risen each year for the next 25 years.

number_of_years = int(input("Enter number of years: "))
print('Year','\t','Rise')
print('-----------------')
for year in range(1,number_of_years+1):
    rise=year*1.6
    print(year,'\t',format(rise, ',.1f'))