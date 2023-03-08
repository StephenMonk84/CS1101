def new_line():
    #prints a dot to show a new line
    print('.')

def three_lines():
    #prints three lines using the new_line function its called three times
    new_line()
    new_line()
    new_line()

def nine_lines():
    #prints nine lines by using the three_lines function
    three_lines()
    three_lines()
    three_lines()

def clear_screen():
    #prints twenty five lines by using a combination of the nine_lines, three_lines and new_line functions
    nine_lines()
    nine_lines()
    three_lines()
    three_lines()
    new_line()

print('Printing the first nine lines')
nine_lines()
print('Printing the next 25 lines')
clear_screen()