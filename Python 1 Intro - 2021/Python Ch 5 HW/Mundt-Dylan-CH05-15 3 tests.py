def main ():

  # Prompting user input for each grade
  user_test_score1 = float (input ("Please enter your score for Test 1: "))
  user_test_score2 = float (input ("Please enter your score for Test 2: "))
  user_test_score3 = float (input ("Please enter your score for Test 3: "))
  
  test_final_results(user_test_score1, user_test_score2, user_test_score3)


def calc_average (user_test_score1, user_test_score2, user_test_score3):

  # Sum of grades / how many grades
  # IE: 75 + 80 + 85 + 90 + 95 / 5 = 85
  average = (user_test_score1 + user_test_score2  + user_test_score3) / 3
  return average

def grade_scale (grade_scale_score):
    if (grade_scale_score < 60):
        return "F"
    elif (grade_scale_score < 70):
        return "D"
    elif (grade_scale_score < 80):
        return "C"
    elif (grade_scale_score < 90):
        return "B"
    elif (grade_scale_score < 101):
        return "A"

def test_final_results (user_test_score1, user_test_score2, user_test_score3):
  average = calc_average(user_test_score1, user_test_score2, user_test_score3)

  print ("Score \t\t Numeric Grade \t Letter Grade")
  print ("-----------------------------------------------")
  print ("score 1: \t " + str(user_test_score1) + "\t\t " + grade_scale(user_test_score1))
  print ("score 2: \t " + str(user_test_score2) + "\t\t " + grade_scale(user_test_score2))
  print ("score 3: \t " + str(user_test_score3) + "\t\t " + grade_scale(user_test_score3))
  print ("Average score: \t " + str(average) + "\t\t " + grade_scale(average))


main ()