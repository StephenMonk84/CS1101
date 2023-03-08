def hypotenuse(a_side, b_side):
    c = 0
    a = a_side**2
    b = b_side**2
    c = (a+b)**(1/2)
    print("The hypotenuse of a triangle with the sides {0} and {1} is {2}".format(a_side, b_side, c))

hypotenuse(3,4)
hypotenuse(6,8)
hypotenuse(2,7)