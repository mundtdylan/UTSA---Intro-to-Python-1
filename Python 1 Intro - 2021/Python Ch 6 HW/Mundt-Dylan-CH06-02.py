def main():
#first limit to read and open lines2a
    def flimit (limit = 5):
        f1 = open("C:/Users/mundt/OneDrive/lines/lines2a.txt", "r")
        #print statement for lines2a for clarity
        print ("Lines2a.txt:" + "\n")
    
        linecount = 0
        #for/if statement for linecounter
        for line in f1:
            if linecount < limit:
                print (line, end = "")
                linecount += 1
        print ("\n")
    flimit()
    #same limit statement done without a linecount since it's printing the entire file.
    def flimit2():
        f2 = open("C:/Users/mundt/OneDrive/lines/lines2b.txt", "r")
        
        print ("Lines2b.txt:" + "\n")
        
        for line in f2:
            print (line, end="")
            
    flimit2()
main()