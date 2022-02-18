#Define the variable day that asks for a number for day of the week.
day = int(input('Enter a number (1-7) for the day of the week: '))

#Define the days of the week with the attached numbers that display each.
if day == 1:
    print('Monday')
elif day == 2:
    print('Tuesday')
elif day == 3:
    print('Wednesday')
elif day == 4:
    print('Thursday')
elif day == 5:
    print('Friday')
elif day == 6:
    print('Saturday')
elif day == 7:
    print('Sunday')
#Print an error if any number is entered outside of the range 1-7.
else:
    print('Error: Please enter a number in the range 1-7.')