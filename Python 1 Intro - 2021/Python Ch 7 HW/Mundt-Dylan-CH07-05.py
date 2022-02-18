def main():
  
    #try statement to start program.
    try: 
        #opening the text file to be read within same directory as program.
        nfile = open("5-ChargeAccounts.txt", 'r')
        #read file.
        accounts = nfile.readlines()
        for n in range(len(accounts)):
            #stripping the return lines within the text file.
            accounts[n] = accounts[n].rstrip('\n')
            #close file.
        nfile.close()
        #user input for account number.
        testaccount = input("Please enter your account number: ")
        #if/else statement to determine whether or not the account number is valid or not.
        if testaccount in accounts: 
            print("The account number is valid.")
        else:
            print("The account number is not valid.")
    #exceptions for program to find errors for file/console.
    except IOError:
        print("The file could not be found.")
    
    except:
        print ("There was an error.")
        #end program.
main()