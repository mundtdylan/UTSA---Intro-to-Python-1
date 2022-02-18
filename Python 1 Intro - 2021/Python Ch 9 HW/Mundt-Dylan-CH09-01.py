def main():
    #dictionary of all course information from sections, instructors, and meeting times.
    dictSect = {36694: "001", 36695: "002", 36696: "003", 38273: "004", 38274: "005", 38275: "006", 
                38276: "007", 36698: "ON1", 38277: "ON2"}
    dictInst = {36694: "Shepherd, Linda", 36695: "Shepherd, Linda", 36696: "Shepherd, Linda", 38273: "Shepherd, Linda", 
                38274: "Castaneda, Robert", 38275: "Akanfe, Oluwafemi", 38276: "Staff", 36698: "Staff", 38277: "Staff"}
    dictMeet = {36694: "Tu-Th 11:00am", 36695: "Tu-Th 1:00 PM", 36696: "Tu-Th 2:30 PM", 38273: "Tu-Th 6:00 PM ", 
                38274: "Mo-We-Fr 11:00 AM", 38275: "Online Only", 38276: "Mo-We 7:30 PM", 36698: "Online Only", 
                38277: "Online Only"}
    #user input of CRN number.
    userCRN =int(input("Enter a CRN number: "))
    
    #if-else statement if: if the CRN is invalid it will print an error.
    if userCRN not in dictSect.keys():
        print ("\n"+str(userCRN)+ " is an invalid course number.")
    #else: print the details of course number.
    else:
        print("\nThe details for CRN #" + str(userCRN) + " are: ")
        print("\nIS 2063 - Programming Language II with Java: ")
        print("\nSection: \t" + dictSect[userCRN])
        print("Instructor:\t" + dictInst[userCRN])
        print("Time: \t\t" + dictMeet[userCRN])
    
main()