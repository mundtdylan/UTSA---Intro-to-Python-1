#Define the variable mass and ask for user to input the mass of object.
mass = float(input('Enter an object\'s mass: '))
#Calculate weight
weight = mass * 9.8
message = "\nThe object"

#Write an if statement for weight inputs that displays a message for each result.
if weight < 100:
    message += ' is too light at ' + format(weight, ',.2f') + ' newtons.'
elif weight >= 100 and weight <= 500:
    message += '\'s weight at ' + format(weight, ',.2f') + ' is just right.'
elif weight > 500:
    message += 'is too heavy at ' + format(weight, ',.2f') + ' newtons.'
#Print the end result.
print(message, end="\n\n")