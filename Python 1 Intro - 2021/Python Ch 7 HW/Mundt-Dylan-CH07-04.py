def main():
    #variables being called for assignment later.
    
    numlist = []
    low = 0.0
    high = 0.0
    total = 0.0
    average = 0.0
    #file location and name being assigned to program.
    dirString = "C:/Users/mundt/OneDrive/"
    fileString = '4-Numbers1.txt'
    #open and read the files.
    numlist = readfile(dirString + fileString)
    #printing the 4-numbers1.txt file.
    print (numlist)
    
    
    #variables assigned to calculate the low/high/total/average of the integers in file.
    low = min(numlist)
    high = max(numlist)
    total = sum(numlist)
    average = total/len(numlist)
    
    print("Low: ", low)
    print("High: ", high)
    print("Total: ", total)
    print("Average: ", average)
    #defining readfile.
def readfile(of):
    #open file.
    nfile = open (of, 'r')
    #reading all integers inside of file.
    nlist = nfile.readlines()
    #close the file.
    nfile.close()
    #stripping the return lines within the text file.
    for n in range(len(nlist)):
        nlist[n] = int(nlist[n].rstrip('\n'))
        
    return nlist
  
    #end program.
main()

