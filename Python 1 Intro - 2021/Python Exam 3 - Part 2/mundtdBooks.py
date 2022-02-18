class bookItem:
    
    def __init__(self, Author, Title, Stock, Price):
        self.__Author = Author
        self.__Title = Title
        self.__Stock = Stock
        self.__Price = Price
    
    def set_Author(self, Author):
        self.__Author = Author
        
    def set_Title(self, Title):
        self.__Title = Title
    
    def set_Stock(self, Stock):
        self.__Stock = Stock
        
    def set_Price(self, Price):
        self.__Price = Price
        
    def __str__(self):
        return  f'Author: {self.__Author}\n' f'Title: {self.__Title}\n' f'Stock: {self.__Stock}\n' f'Price: {self.__Price}\n'