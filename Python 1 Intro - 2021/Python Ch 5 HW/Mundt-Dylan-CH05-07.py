def main():
    #Prompt user to enter number of tickets sold.
    classATix = float(input ("Please enter the number of Class A tickets sold: "))
    classBTix = float(input ("Please enter the number of Class B tickets sold: "))
    classCTix = float(input ("Please enter the number of Class C tickets sold: "))
    
    classASales = calcClassASales(classATix)
    classBSales = calcClassBSales(classBTix)
    classCSales = calcClassCSales(classCTix)
    
    income (classASales, classBSales, classCSales)
    #Print statements to output proper format for ticket sales.
    print ("Class A sales: $ ", format (calcClassASales(classATix)))
    print ("Class B sales: $ ", format (calcClassBSales(classBTix)))
    print ("Class C sales: $ ", format (calcClassCSales(classCTix)))
    print ("The total amount of tickets sold for each class: $", format(income(classASales, classBSales, classCSales)))
 
    #Calculate class sales.
def calcClassASales (classATix):
    classASales = classATix * 20
    return classASales

def calcClassBSales (classBTix):
    classBSales = classBTix * 15
    return classBSales

def calcClassCSales (classCTix):
    classCSales = classCTix * 10
    return classCSales

#Calculate total class sale income.
def income (classASales, classBSales, classCSales):
    totalClassSales = (classASales + classBSales + classCSales)
    return totalClassSales

main ()