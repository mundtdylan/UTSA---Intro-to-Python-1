def main():
    #file directory located within the same path of this .py file.
    dirString = "C:/Users/mundt/OneDrive/lines/"
    #file string containing the name of the text/html file.
    fileString = 'ex_11.txt'
    #defining a variable name for input name statement
    user_name = float(input("Enter your name: "))
    #defining a variable name for input description statement
    user_desc = float(input("Describe yourself: "))
    #defining a variable to open and write the file string/directory
    htmlFile = open(dirString + fileString, 'w')
    #writing out the html code necessary to save to the directory
    htmlFile1 ="<html> \n"+\
        "<head>\n"+\
        "<title>My Personal Web Page</title>\n"+\
        "</head> \n" +\
        "<body> \n" +\
            "<center> \n" +\
                "<h1>" + user_name + "</h1>\n" +\
            "<center> \n" +\
            "<hr /> \n" +\
            user_desc + "\n"\
            "<hr /> \n" +\
        "</body> \n" +\
        "</html> \n"  
    #save and close html file.
    htmlFile.write(htmlFile1)
    htmlFile.close()
main()
        
        