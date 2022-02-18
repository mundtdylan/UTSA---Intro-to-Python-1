#Attach a variable with the cost of tuition.
currentTuition = 8000
#Set the calculations for tuition.
for currentYear in range(1, 6):
    currentTuition += ( 3 / 100 ) * currentTuition
    print ( currentYear, "\t", currentTuition )