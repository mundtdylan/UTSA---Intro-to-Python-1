#State the sales tax percentage
salestax = 0.07
#Display the input price for items 1-5
item1=float(input("Enter the price of the first item:"))
item2=float(input("Enter the price of the second item:"))
item3=float(input("Enter the price of the third item:"))
item4=float(input("Enter the price of the fourth item:"))
item5=float(input("Enter the price of the fifth item:"))
#Get the subtotal for items 1-5
subtotal = item1+item2+item3+item4+item5
#Print the subtotal of the sale
print("The subtotal of the sale:" , subtotal)
#Calculate the sales tax amount
amountofsalestax = subtotal * salestax
#Print the sales tax amount
print("The amount of sales tax:", amountofsalestax)
#Calculate the total
Total = subtotal + amountofsalestax
#Print the total
print("Total:" , Total)