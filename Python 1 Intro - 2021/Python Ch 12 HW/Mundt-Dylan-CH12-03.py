#power function for base and exponent.
def power(base,exp):
    if exp == 0:
        return 1
    #else returns the power formula.
    else:
        return base * power(base, exp -1)
    
def main():
    #print instructions.
    print("This program will ask you for a base number and an exponent, and it will calculate the base raised to the power of the exponent.")
    #user input for a pos. base number.
    baseinp = int(input("Please enter a positive base number: "))
    #while loop for negative input base number, forcing the user to input again.
    while baseinp < 0:
        print("You entered", baseinp, "which is negative.", "\n" "Please try again.")
    #input exponent.
    expinp = int(input("Please enter an exponent between 1 and 100: "))
    #while loop statements between 1 and 100, otherwise, forcing the user to input again.
    while expinp < 1:
        print("You entered", expinp, "which is less than the minimum value of 1.", "\n" "Please try again.")
        expinp = int(input("Please enter an exponent between 1 and 100: "))
        
    
    while expinp > 100:
        print("You entered", expinp, "which is greater than the maximum value of 100.", "\n" "Please try again.")
        expinp = int(input("Please enter an exponent between 1 and 100: "))
        
    #printing the solution of the base raised to the exponent totaling the sum.
    else:
        print(baseinp, "raised to the power of", expinp, "is: ", power(baseinp, expinp))
#end program.
main()