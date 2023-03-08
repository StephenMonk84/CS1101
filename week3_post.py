def calc_decimal(param1):
    if param1 >= 1:
        print("The value is greater that one")
    else:
        if param1 < 1 and param1 >= 0.5:
            print("The value rounds up to 1 so its basically one")
        else:
            if param1 < 0.5 and param1 >= 0:
                print("Hey atleast it's positive")
            else:
                print("Tough luck the number is negative")

calc_decimal(7)
calc_decimal(0.7)
calc_decimal(0)
calc_decimal(-7)