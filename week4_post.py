def precond_test(var1, var2):
    return var1 + var2

def postcond_test(x1, x2):
    midpoint_x = (x1+(x2/2))
    return midpoint_x

def return_issue(y1, y2):
    return ((y1+y2)/2)
print("The sum of two numbers is: " + precond_test("This is ", "a test."))
print("The midpoint on the x-axis is {0}.".format(postcond_test(1,2)))
print("The midpoint of the y axis is ".format(return_issue(1,2)))