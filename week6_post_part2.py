def mod_list(list1, var1):
    if var1 > sum(list1):
        del list1[0]
    else:
        list1.append(var1)

#This passes a value that is lower than the sum of the list
test_list = [1,4,7]
mod_list(test_list, 9)
print(test_list)
#This passes a value that is greater than the sum of the list
test_list_one = [1,4,7]
mod_list(test_list_one, 15)
print(test_list_one)
