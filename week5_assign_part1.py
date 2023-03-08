def my_sqrt(a):
    x=5
    while True:
        y=(x+a/x)/2.0
        if y==x:
            break
        x=y
    return x

print(my_sqrt(7))