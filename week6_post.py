def identical_vals(var1, var2):
    return var1 is var2


str1 = "Is this string identical"
str2 = "Is this string identical"
list1 = ["Is", "this", "string", "identical"]
list2 = ["Is", "this", "string", "identical"]

print("Printing the comparison between two strings")
print(identical_vals(str1, str2))
print()
print("Printing the comparison between two lists")
print(identical_vals(list1, list2))
