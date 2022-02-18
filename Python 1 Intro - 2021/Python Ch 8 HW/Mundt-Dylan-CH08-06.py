def main():
    #defining variable total to use later.
    total = 0
    
    #directory + file name
    
    dirString = ""
    fileString = "ch8-text.txt"
    
    #opening file and reading.
    f = open(dirString + fileString, "r")
    lines = f.readlines()

#for statement to read the length of the file.
    for line in lines:
        words = line.split()
        total += len(words)
    #finding the average of the total divided by the length of the file.
    avg = total / len(lines)
    
    #printing the average.
    print("The average number of words per line is:", avg)
    #end program.
main()