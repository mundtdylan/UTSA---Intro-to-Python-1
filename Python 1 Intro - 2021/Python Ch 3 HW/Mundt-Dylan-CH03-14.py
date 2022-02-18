#Input variables for weight and height so users may input them.
userWeight = float( input ( "Please enter your weight: "))
userHeight = float( input ( "Please enter your weight: "))
#Calculate user Body Mass Index.
userBMI = ( userWeight * 703) / (userHeight ** 2 )

print()

#Write an if-else statement that will set height and weight guidelines for overweight, underweight, or optimal health.
if userWeight < 18.5:
    print ("You are considered underweight.")
elif userWeight > 25:
    print ("You are considered overweight.")
else:
    print ("You are considered optimal weight.")