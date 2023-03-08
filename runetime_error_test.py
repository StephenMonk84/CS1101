def get_some_numbers():
    print("Welcome to the number divider program")
    num_one = int(input("Please input the first number: "))
    num_two = int(input("Please input the second number: "))
    print("The quotient of {0} and {1} is ".format(num_one, num_two) + str(num_one/num_two))

get_some_numbers()