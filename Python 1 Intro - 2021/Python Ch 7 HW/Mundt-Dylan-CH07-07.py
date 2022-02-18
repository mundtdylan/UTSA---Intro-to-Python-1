def main():
    #all variables to be used // file implementations. 
    dirString = ""
    keyString = "7-SolutionKey.txt"
    subString = "7-ExamSubmission2.txt" #there is a 7-ExamSubmission1.txt file as well.
    corCT = 0
    incCT = 0
    incQ = []
    #try statement
    try:
        #opening the key to the test as well as exam submissions.
        keyIn = open(dirString + keyString, 'r')
        subIn = open(dirString + subString, 'r')
        #reading the lines within the file.
        keyList = keyIn.readlines()
        subList = subIn.readlines()
        #stripping the file of return lines.
        for n in range(len(keyList)):
            keyList[n] = keyList[n].rstrip('\n')
            subList[n] = subList[n].rstrip('\n')
            #if/else statement for exam check to tally right/wrong answers.
        for i in range(len(keyList)):
            if keyList[i] == subList[i]:
                corCT +=1
            else:
                incCT +=1
                incQ.append(i+1)
        #If else statement for right/wrong answer scores to determine final outcome.
        if corCT >= 15:
            print("The student passed the exam")
        else:
            print("The student did not pass the exam.")
            
                   #print statements for correct/incorrect answers.
        print("Questions answered correctly: ", corCT)
        print("Questions answered incorrectly: ", incCT)
        #print statement if student answered all questions correctly.
        if incCT > 0:
            print("Questions answered incorrectly: ", incQ)
                
        #exceptions for program errors.
    except IOError:
        print("The file could not be found.")
        
    except IndexError:
        print("There was an indexing error.")
        
    except:
        print("There was an error.")
    
    #end program.
main()