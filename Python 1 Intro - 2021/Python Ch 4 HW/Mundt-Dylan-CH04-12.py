#Define a variable to allow the user to input a number to factor.
userInteger = int( input( "Please enter a number: " ))

#Using while-for to set rules and range for the factorial.
while userInteger < 1:
    userInteger= int( input( "Please enter a positive number: " ))
    
factorial = 1

for currentNumber in range( 1, userInteger + 1 ):
    factorial = factorial * currentNumber
#Print a statement that shows the results. 
print ( "The factorial of", userInteger, "is", factorial )
