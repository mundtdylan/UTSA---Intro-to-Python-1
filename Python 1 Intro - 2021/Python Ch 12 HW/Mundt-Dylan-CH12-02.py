#function of numbers
def sumNums(num):
    if num == 1:
        return num
    #returns the formula.
    else:
        return sumNums (num-1) + num

def main():
    #user input to enter a whole number that's positive.
    num = int (input("Please enter a positive, whole number: "))
    #while loop that will error out and ask the user to input again.
    while num < 0:
        print("You entered", num, "which is negative." "\n" "Please try again.")
        num = int (input("Please enter a positive, whole number: "))
    #if the user inputs a positive number, it will print the sum.
    else:
        print("The sum of 1 -", num, " is ", sumNums(num))
    #end program.
main() 