def countdown(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n-1)

def countup(n):
    if n >= 0:
        print('Blastoff!')
    else:
        print(n)
        countup(n+1)

def select_up_or_down():
    num = int(input("Please enter a positive or negative number to start the launch sequence: "))
    if(num > 0):
        countdown(num)
    elif(num < 0):
        countup(num)
    else:
        countup(num)

select_up_or_down()
select_up_or_down()
select_up_or_down()