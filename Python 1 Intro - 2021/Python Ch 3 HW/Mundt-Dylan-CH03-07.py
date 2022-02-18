#Define variables 1 and 2 to allow the user to input the colors to mix.
primaryColor1 = input("Please enter primary color 1: ")
primaryColor2 = input("Please enter primary color 2: ")

#If statement that will print mixed color results.
if ( primaryColor1 == "red" and primaryColor2 == "blue" ) or ( primaryColor1 == "blue" and primaryColor2 == "red" ):
    print(primaryColor1 + " mixed with " + primaryColor2 + " is purple" )
elif ( primaryColor1 == "red" and primaryColor2 == "yellow" ) or ( primaryColor1 == "red" and primaryColor2 == "blue" ):
    print(primaryColor1 + " mixed with " + primaryColor2 + " is orange" )
elif (primaryColor1 == "blue" and primaryColor2 == "yellow" ) or ( primaryColor1 == "yellow" and primaryColor2 == "blue"):
    print(primaryColor1 + " mixed with " + primaryColor2 + " is green" )
#else statement that will display an error if one of the three primary colors are not inputted.
else:
    print( "At least one of your colors, " + primaryColor1 + " and " + primaryColor2 + " is not a primaryColor")