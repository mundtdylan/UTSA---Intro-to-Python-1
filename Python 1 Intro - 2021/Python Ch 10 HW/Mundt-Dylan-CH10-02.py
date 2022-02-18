from mundtdQuestion import Question

def main():
    score = 0
    
    obj1 = Question("What is the informal language, used by programmers use to create models of programs, that has no syntax rules and is not meant to be compiled or executed?", "1. flowchart", "2. algorithm", "3. source code", "4. pseudocode", "")
    print(obj1.__str__())
    usr_inpt = float(input('Enter your solution (a number between 1 and 4): '))
    if usr_inpt == 4:
        score = score+1
        print ("That is the correct answer" "\n")
    else:
        print ("That is the incorrect answer." "\n")
    
    obj2 = Question("A(n) __________ is a diagram that graphically depicts the steps that take place in a program?", "1. fowchart", "2. algorithm", "3. source code", "4. pseudocode", "")
    print(obj2.__str__())
    usr_inpt = float(input('Enter your solution (a number between 1 and 4): '))
    if usr_inpt == 1:
        score = score+1
        print ("That is the correct answer" "\n")
    else:
        print ("That is the incorrect answer." "\n")
    
    obj3 = Question("The __________ function reads a piece of data that has been entered at the keyboard and returns that piece of data, as a string, back to the program.", "1. input()", "2. output()", "3. eval_input()", "4. str_input()", "")
    print(obj3.__str__())
    usr_inpt = float(input('Enter your solution (a number between 1 and 4): '))
    if usr_inpt == 1:
        score = score+1
        print ("That is the correct answer" "\n")
    else:
        print ("That is the incorrect answer." "\n")
    
    obj4 = Question("The line continuation character is a", "1. #", "2. %", "3. &", "4. \ ", "")
    print(obj4.__str__())
    usr_inpt = float(input('Enter your solution (a number between 1 and 4): '))
    if usr_inpt == 4:
        score = score+1
        print ("That is the correct answer" "\n")
    else:
        print ("That is the incorrect answer." "\n")
    
    obj5 = Question("Which mathematical operator is used to raise 5 to the second power in Python?", "1. /", "2. **", "3. ^", "4. ~", "")
    print(obj5.__str__())
    usr_inpt = float(input('Enter your solution (a number between 1 and 4): '))
    if usr_inpt == 2:
        score = score+1
        print ("That is the correct answer" "\n")
    else:
        print ("That is the incorrect answer." "\n")
    
    obj6 = Question("In a print statement, you can set the __________ argument to a space or empty string to stop the output from advancing to a new line.", "1. stop", "2. end", "3. separator", "4. newLine", "")
    print(obj6.__str__())
    usr_inpt = float(input('Enter your solution (a number between 1 and 4): '))
    if usr_inpt == 2:
        score = score+1
        print ("That is the correct answer" "\n")
    else:
        print ("That is the incorrect answer." "\n")
    
    obj7 = Question("After the execution of the following statement, the variable sold will reference the numeric literal value as (n) __________ data type.\n\n sold = 256.752", "1. int", "2. float", "3. str", "4. currency", "")
    print(obj7.__str__())
    usr_inpt = float(input('Enter your solution (a number between 1 and 4): '))
    if usr_inpt == 2:
        score = score+1
        print ("That is the correct answer" "\n")
    else:
        print ("That is the incorrect answer." "\n")
    
    obj8 = Question("After the execution of the following statement, the variable price will reference the value __________.\n\n price = int(68.549)", "1. 68", "2. 69", "3. 68.55", "4. 68.6", "")
    print(obj8.__str__())
    usr_inpt = float(input('Enter your solution (a number between 1 and 4): '))
    if usr_inpt == 1:
        score = score+1
        print ("That is the correct answer" "\n")
    else:
        print ("That is the incorrect answer." "\n")
    
    obj9 = Question("What is the output of the following statement?\n\n print('I \'m ready to begin')", "1. Im ready to begin", "2. I \'m ready to begin", "3. I'm ready to begin", "4. 'I \'m ready to begin'", "")
    print(obj9.__str__())
    usr_inpt = float(input('Enter your solution (a number between 1 and 4): '))
    if usr_inpt == 3:
        score = score+1
        print ("That is the correct answer" "\n")
    else:
        print ("That is the incorrect answer." "\n")
    
    obj10 = Question("What is the output of the following statement, given that value1 = 2.0 and value2 = 12?\n\n print(value1 * value2)", "1. 24", "2. value1 * value2", "3. 24.0", "4. 2.0 * 12", "")
    print(obj10.__str__())
    usr_inpt = float(input('Enter your solution (a number between 1 and 4): '))
    if usr_inpt == 3:
        score = score+1
        print ("That is the correct answer" "\n")
    else:
        print ("That is the incorrect answer." "\n")
    
    print("Your score is: ", "{:.0%}".format(score/10))
    
main()