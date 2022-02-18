def main():
  dirString = "C:/Users/mundt/OneDrive/lines/"
  
  fileString = 'input9a.txt'
  fileString = 'input9b.txt' #exception file
  fileString = 'input.txt' #exception file
  
 #try/except statement to open files and print 
  try:
      with open (dirString + fileString, "r") as f:

        data = [float(line.rstrip()) for line in f]
        print ("Average: ")
        print(sum(data)/9)

#should be exception statement for input.txt          
  except IOError:
    print ("An error occurred while trying to read the file.")
#should be exception statement for input9b.txt         
  except ValueError:
    print ("Non-numeric data found in the file.")

main()