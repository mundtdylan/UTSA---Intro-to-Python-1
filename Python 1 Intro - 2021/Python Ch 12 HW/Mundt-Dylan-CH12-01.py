def main():
    dirString = ""
    numString = "12-numbers.txt"
    
    try:
        #opening the file.
        readFile = open(dirString + numString, 'r')
        #reading the lines within the file.
        readList = readFile.readlines()
        #stripping the file of return lines.
        for n in range(len(readList)):
            readList[n] = readList[n].rstrip('\n')
            
        for i in range(0, len(readList)):
            readList[i] = int(readList[i])
        #print the number list
        print("List of numbers: ", readList)
        #print the sum of all numbers in the list.
        print('\n' "The sum of all the numbers in the list is: ", sum(readList))
        #exceptions for errors.
    except IOError:
        print("The file could not be found.")
        
    except IndexError:
        print("There was an indexing error.")
        
    except:
        print("There was an error.")
    #end code.    
main()