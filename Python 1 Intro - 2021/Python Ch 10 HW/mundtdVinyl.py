class vinylItem:
    
    def __init__(self, Artist, Title, Stock, Price):
        self.__Artist = Artist
        self.__Title = Title
        self.__Stock = Stock
        self.__Price = Price
    
    def set_Artist(self, Artist):
        self.__Artist = Artist
        
    def set_Title(self, Title):
        self.__Title = Title
    
    def set_Stock(self, Stock):
        self.__Stock = Stock
        
    def set_Price(self, Price):
        self.__Price = Price
        
    def __str__(self):
        return  f'Artist: {self.__Artist}\n' f'Title: {self.__Title}\n' f'Stock: {self.__Stock}\n' f'Price: {self.__Price}\n'