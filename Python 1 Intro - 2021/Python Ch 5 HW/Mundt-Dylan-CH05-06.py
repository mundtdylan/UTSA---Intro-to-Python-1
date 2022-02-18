#Define main code for user inputs of fat/carb grams consumed. Also define print statements.
def main():
    fat_grams = float (input ("Enter the number of grams of fat consumed: "))
    calories_from_fat = calc_calories_from_fat(fat_grams)
    
    carb_grams = float (input ("Enter the number of grams of carbs consumed: "))
    calories_from_carbs = calc_calories_from_carbs(carb_grams)

    print ("The calories from fat are: " , format(calories_from_fat))
    print ("The calories from carbs are: ", format(calories_from_carbs)) 

#Calculate fat calories.
def calc_calories_from_fat (fat_grams):
    calories_from_fat = fat_grams * 9
    return calories_from_fat

#Calculate carb calories.
def calc_calories_from_carbs (carb_grams):
    calories_from_carbs = carb_grams * 4
    return calories_from_carbs

#Close main code.
main()