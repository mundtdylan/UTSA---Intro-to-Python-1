import random

def main():
    #dictionary of san antonio counties.
    dictCnty = {'Atascosa': 'Jourdanton', 'Bandera': 'Bandera', 'Bastrop': 'Bastrop', 'Bexar': 'San Antonio', 'Caldwell': 'Lockhart', 'Comal': 'New Braunfels', 'Guadalupe': 'Seguin', 'Hays': 'San Marcos', 'Kendall': 'Boerne', 'Medina': 'Hondo', 'Travis': 'Austin', 'Williamson': 'Georgetown', 'Wilson': 'Floresville'}
    
    #variables to use later
    correct = 0
    wrong = 0
    next_question = True
    index = 0
    userInput = ''
    
    #while-if-else statements
    while next_question:
        cntyIter = iter(dictCnty)
        #index for the random county selection.
        index = (random.randint(1, len(dictCnty)) - 1)
        
        for i in range (index-1):
            temp = cntyIter.__next__()
        cntyCurr = str(cntyIter.__next__())
        
        #user input of county seat
        userInput = input(f'\nWhat is the county seat of {cntyCurr} County? (Or enter 0 to quit): ')
        
        #if statement for quit
        if userInput == '0':
            next_question = False
            print (f'\nYou had {correct} correct {plurals(correct)} and {wrong} incorrect {plurals(wrong)}\n')
            
        #elif statement for correct score
        elif userInput == dictCnty[cntyCurr]:
            correct += 1
            print ("That is correct. ")
        
        #else statement for incorrect score.
        else:
            wrong += 1
            print("That is incorrect.")

#plurals for formatting purposes.
def plurals(count):
    if count > 1 or count == 0:
        return 'responses'
    else:
        return 'response'

#closing if statement
if __name__ == '__main__':
    main()