class Question:
    
    def __init__(self, questionText, Answer1, Answer2, Answer3, Answer4, correctAnswer):
        self.__questionText = questionText
        self.__Answer1 = Answer1
        self.__Answer2 = Answer2
        self.__Answer3 = Answer3
        self.__Answer4 = Answer4
        self.__correctAnswer = correctAnswer
    
    def questionText(self, questionText):
        self.__questionText = questionText
        
    def Answer1(self, Answer1):
        self.__Answer1 = Answer1
        
    def Answer2(self, Answer2):
        self.__Answer2 = Answer2
        
    def Answer3(self, Answer3):
        self.__Answer3 = Answer3
        
    def Answer4(self, Answer4):
        self.__Answer4 = Answer4
        
    def correctAnswer(self, correctAnswer):
        self.__correctAnswer = correctAnswer
        
    def __str__(self):
        return  f'{self.__questionText}\n\n' f'{self.__Answer1}\n' f'{self.__Answer2}\n' f'{self.__Answer3}\n' f'{self.__Answer4}\n' f'{self.__correctAnswer}\n'