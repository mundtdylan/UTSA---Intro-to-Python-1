#The average temperature constatnt.
AVG_TEMP=95.2
#Allow the user to enter the number of dates to be averaged.
numofDates = int(input(" Please enter the number of dates to average: " ))
#This allows the user to enter the temperature readings.
print(" Please enter the temperature readings (in F): ")
#Assign a value to the variable total, and start a for statement that will calculate the average temperature. 
total=0
for x in range (0, numofDates):
    temperature = float(input())
    total += temperature
avg_convert_temp = (total / numofDates) 

#Calculate the 30-year average and fahrenheit to celsisus conversions. 
celsius_convert = float((5/9) * (avg_convert_temp - 32))
year_AVG_convert = float((5/9) * (AVG_TEMP - 32))

#Show results.
print ("The temperature results in Fahrenheit and Celsius are: ", avg_convert_temp, celsius_convert)

#Design an if-else statement that will compare the 30-year average to the temperature in Celsius. 
if year_AVG_convert > celsius_convert:
    temp = year_AVG_convert - celsius_convert
    print (" The new average is: ", format(temp), "degrees Celsius colder than the 30-year average. ")
elif year_AVG_convert < celsius_convert:
    temp = celsius_convert - year_AVG_convert
    print (" The new average is: ", format(temp), "degrees Celsius warmer than the 30-year average. ")
else:
    print (" The new average is: ", format(temp), "degrees Celsius equal to the 30-year average. ")
    
#Dylan Mundt, onf721, @01612413