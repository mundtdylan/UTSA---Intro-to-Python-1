#State the sales tax percentage
statesalestaxpercentage = 0.025
#State the county sales tax percentage
countysalestaxpercentage = 0.05
#Get the purchase amount
purchaseAmount = (float(input("Enter the amount of a purchase:")))
#Calculate the state sales tax
statesalestax = purchaseAmount * statesalestaxpercentage
#Calculate the county sales tax
countysalestax = purchaseAmount * countysalestaxpercentage
#Calculate the total of the sales tax
Totalsalestax = statesalestax + countysalestax 
#Calculalte the total of the sale
Totalofthesale = purchaseAmount + Totalsalestax

#Display all required amounts
print("The amount of the purchase:" , purchaseAmount)
print("The state sales tax:" , statesalestax)
print("The county sales tax:", countysalestax)
print("The total sales tax:", Totalsalestax)
print("The total of the sale:", Totalofthesale)