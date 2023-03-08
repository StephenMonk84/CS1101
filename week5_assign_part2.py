import math
def my_sqrt(a):
    x=5
    while True:
        y=(x+a/x)/2.0
        if y==x:
            break
        x=y
    return x
def test_sqrt():
    inp = 1
    while inp <= 25:
        str_out = "a = {0} | my_sqrt(a) = " + str(my_sqrt(inp)) + " | math.sqrt(a) = "+ str(math.sqrt(inp)) + " | diff = " + str(abs(my_sqrt(inp)-math.sqrt(inp)))
        print(str_out.format(inp))
        inp += 1

test_sqrt()