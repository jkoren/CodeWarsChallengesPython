'''
Welcome. In this kata, you are asked to square every digit of a number.

For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.

Note: The function accepts an integer and returns an integer

time: 35 minutes

'''

def square_digits(number):
    number_as_char = str(number)
    new_number_string = ""
    for character in number_as_char:
        new_characters = str(int(character)**2)
        new_number_string = new_number_string + new_characters

    return(int(new_number_string))

print(square_digits(9119))
print(square_digits(0))
print(square_digits(7227))
print(square_digits(14))

'''
best practice from CodeWars
def square_digits(num):
    ret = ""
    for x in str(num):
        ret += str(int(x)**2)
    return int(ret)

clever use of code, but probably not to put into production
def square_digits(num):
    return int(''.join(str(int(d)**2) for d in str(num)))
'''

