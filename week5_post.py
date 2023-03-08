def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False

def any_lowercase2(s):
    for c in s:
        if c.islower():
            return 'True'
        else:
            return 'False'

def any_lowercase3(s):
    for c in s:
        flag=c.islower()
    return flag

def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True


str1 = 'hello'
str2 = 'Hi'
str3 = 'iT'
str4 = 'ALL'

print(any_lowercase5(str1))
print(any_lowercase5(str2))
print(any_lowercase5(str3))
print(any_lowercase5(str4))
print(any_lowercase5('tEST'))
#print(any_lowercase5(str4))