def using_add_symbol(param1, param2):
    return param1 + param2

def print_output(param1, param2):
    print(using_add_symbol(param1, param2))

def call_functions(param1, param2):
    print_output(param1, param2)

call_functions(7,5)
call_functions("This is ", "a string")
call_functions(7.5+9.3, 7.4)