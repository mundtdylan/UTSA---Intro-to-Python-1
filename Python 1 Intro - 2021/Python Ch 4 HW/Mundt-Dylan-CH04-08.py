#Creating a loop to add all numbers together until quit. 
def series():
    sum1 = 0
    while True:
        number = int(input("Choose a number, -1 to quit:"))
        if number >=0:
            sum1+=number
        else:
            return sum1
series()