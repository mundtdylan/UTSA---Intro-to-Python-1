def main():
    #input for user to enter date in format.
    input_date = input('Enter a date in the format dd/mm/yyyy: ')
    #months for index to choose from.
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    date_list = input_date.split('/')
    #index for date list
    month = months [int (date_list[0]) - 1]
    #printing the correct format for dates to compile.
    print(month + ' ' + date_list[0] + ', ' + date_list[2])
    #end program.
main()