def descend(val1, val2):
    #This function will determine which value is larger and print the larger value first
    if val1 > val2:
        print("The list in descending order is {0}, {1}".format(val1, val2))
    elif val2 > val1:
        print("The list in descending order is {0}, {1}".format(val2, val1))
    else:
        print("Both numbers are the same")

descend(7,4)
descend(9,5)
descend(6,6)