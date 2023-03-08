def is_even():
    num =0
    while num != 'e':
        num = input("Enter a number: ")
        
        if num.isnumeric():
            num = int(num)
            if num %2 ==0:
                print("{0} is Even".format(num))
            else:
                print("{0} is Odd".format(num))
            

is_even()