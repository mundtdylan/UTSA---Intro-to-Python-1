def main():
    #directory string + file string
    dirString = ""
    fileString = "ch8-text.txt"
    #strings to tie into code later.
    upper = 0
    lower = 0
    digit = 0
    whitespace = 0
    
    #opening the file + directory, reading.
    f = open(dirString + fileString, "r")
    lines = f.readlines()
    
    #for if elif statement for uppercase/lowercase letters, digits, and whitespace.
    for line in lines:
        for char in line:
            if char.isupper():
                upper += 1
            elif char.islower():
                lower += 1
            elif char.isdigit():
                digit += 1
            elif char.isspace():
                whitespace += 1
               
    #print statements for code/results.
    print("Upper case letters:", upper)
    print("Lower case letters:", lower)
    print("Digits:", digit)
    print("Whitespace:", whitespace)
    
    #end program.
main()