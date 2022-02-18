def main():
    def fileString():
    #opening the file directory, read
        with open ("C:/Users/WXM41270/OneDrive/lines/numbers6.txt", "r") as f:
            data = [float(line.rstrip()) for line in f]
        #for clarity
        print ("Average: ")
        #printing the average of the file containing 9 numbers
        print(sum(data)/9)
    fileString()
main()