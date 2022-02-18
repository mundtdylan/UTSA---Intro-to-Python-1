import random

#random integer calls.
random_addend1= random.randint(100, 300)
random_addend2= random.randint(100, 300)

def main():
    userRandom_addend = adding()
    checker (userRandom_addend)
    
    
def adding():
    global random_addend1
    global random_addend2
    
    #prompt user to input values.
    userRandom_addend = float(input ("What is: " + str(random_addend1) + " + " + str(random_addend2) + "?: "))
    return userRandom_addend
    

def checker(userRandom_addend):
    global random_addend1
    global random_addend2
    
    #if-else statement for user based on sum.
    correctsum = random_addend1 + random_addend2
    if userRandom_addend == correctsum:
        print ("Congratulations, you are correct!")
    else:
        print ("You're wrong, try again.")


main()