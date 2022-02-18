#module/class imports
from mundtdBooks import bookItem
#main function
def main(build_items, inventory, check_stock):
    def build_items():
        items = []
        #all book information list
        obj1 = bookItem.Item("Diana Gabaldon", "Go Tell the Bees That I am Gone", "12", "$23.71")
        obj2 = bookItem.Item("Nora Roberts", "The Becoming", "40", "$19.42")
        obj3 = bookItem.Item("John Grisham", "The Judge’s List", "20", "$14.97")
        obj4 = bookItem.Item("James Patterson", "Fear No Evil", "0", "$14.50")
        obj5 = bookItem.Item("Nicholas Sparks", "The Wish", "5", "$14.05")
        obj6 = bookItem.Item("Mitch Albom", "The Stranger in the Lifeboat", "6", "$11.99")
        obj7 = bookItem.Item("Richard Paul Evans", "The Christmas Promise", "3", "$12.73")
        obj8 = bookItem.Item("Danielle Steel", "Flying Angels", "18", "$14.49")
        obj9 = bookItem.Item("Amor Towles", "The Lincoln Highway", "4", "$18.84")
        obj10 = bookItem.Item("David Baldacci", "Mercy", "1", "$22.68")
        #appending each item
        items.append(obj1, obj2, obj3, obj4, obj5, obj6, obj7, obj8, obj9, obj10)
        #printing all items
        print(obj1.__str__())
        print(obj2.__str__())
        print(obj3.__str__())
        print(obj4.__str__())
        print(obj5.__str__())
        print(obj6.__str__())
        print(obj7.__str__())
        print(obj8.__str__())
        print(obj9.__str__())
        print(obj10.__str__())
        #returning the book info
        return items
    #inventory function    
    def inventory(build_items):
        #printing the inventory list
        print ("Inventory Menu" "\n")
        print ("=====================================================================")
        list = ("1. Diana Gabaldon / Go Tell the Bees That I am Gone", 
                "2. Nora Roberts / The Becoming", 
                "3. John Grisham / The Judge’s List",
                "4. James Patterson / Fear No Evil",
                "5. Nicholas Sparks / The Wish",
                "6. Mitch Albom / The Stranger in the Lifeboat",
                "7. Richard Paul Evans / The Christmas Promise",
                "8. Danielle Steel / Flying Angels",
                "9. Amor Towles / The Lincoln Highway",
                "10. David Baldacci / Mercy")
        for x in list:
            print (x)
        #user input for the inventory menu.
        menuInp = int(input("Enter the menu number for inventory detail: "))
        #if menu input is less than 1, it will loop and ask the user to try again.
        while menuInp < 1:
            print("You entered", menuInp, "which is less than the minimum value of 1.", "\n" "Please try again.")
            menuInp = int(input("Enter the menu number for inventory detail: "))
            
        #if menu input is more than 10, it will loop and ask the user to try again.
        while menuInp > 10:
            print("You entered", menuInp, "which is greater than the maximum value of 10.", "\n" "Please try again.")
            menuInp = int(input("Enter the menu number for inventory detail: "))
        #if the menu input is correct between 1-10, it will return.
        else:
            return menuInp
        #check stock function
    def check_stock(build_items):
        #asking the user to input copy amounts for the inventory.
        copyInp = int(input("How many copies of {self.__Title} do you need?"))
        #if else statement for user input.
        if copyInp == bookItem.__Stock:
            print ("We have {self.__Stock} copies of {self.__Title} by {self.__Author} in stock.")
        elif copyInp > bookItem.__Stock:
            print ("Sorry, you requested", copyInp, "copies of {self.__Title}, but we only have {self.__Stock} available.")
        else:
            print ("Sorry, {self.__Title} is out of stock.")
            
main(build_items, inventory, check_stock)

#yes, it won't output. I keep getting a "runfile" output on this code. Not sure what else to do as I feel like I ran through all I could!