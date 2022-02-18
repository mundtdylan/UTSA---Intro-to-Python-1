from mundtdBooks import bookItem

def main():
    print("Record Store Item 1: ")
    obj2 = bookItem("The Lumineers", "Brightside", "12.99", "$22.99")
    print(obj2.__str__())
    
    print ("Record Store Item 2: ")
    obj2 = bookItem("Shakira", "Laundry Service", "40", "$34.98")
    print(obj2.__str__())
    
    print ("Record Store Item 3: ")
    obj2 = bookItem("Adele", "30", "20", "$39.97")
    print(obj2.__str__())
    
    print ("Record Store Item 4: ")
    obj2 = bookItem("Tom Petty & the Heartbreakers", "Greatest Hits", "26", "$24.64")
    print(obj2.__str__())
    
    print ("Record Store Item 5: ")
    obj2 = bookItem("Nirvana", "Nevermind 30th Anniversary Edition", "5", "$31.99")
    print(obj2.__str__())
    
main()