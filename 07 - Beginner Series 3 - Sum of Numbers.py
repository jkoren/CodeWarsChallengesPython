'''
Given two integers a and b, which can be positive or negative, find the sum of all the numbers between including
them too and return it. If the two numbers are equal return a or b.

Note: a and b are not ordered!

Examples
get_sum(-3,-1) == -3 + -2 + -1 = -6
get_sum(1, 0) == 1   // 1 + 0 = 1
get_sum(1, 2) == 3   // 1 + 2 = 3
get_sum(0, 1) == 1   // 0 + 1 = 1
get_sum(1, 1) == 1   // 1 Since both are same
get_sum(-1, 0) == -1 // -1 + 0 = -1
get_sum(-1, 2) == 2  // -1 + 0 + 1 + 2 = 2

'''

def get_sum(number1, number2):
    if number1 == number2:
        return(number1)
    elif number1 < number2:
        smaller_number = number1
        bigger_number = number2
    else:
        smaller_number = number2
        bigger_number = number1

    sum = 0
    current_number = smaller_number;
    while current_number <= bigger_number:
        sum += current_number
        current_number += 1

    return sum

print(get_sum(-3,-1))
print(get_sum(-1,-3))
print(get_sum(1,0))
print(get_sum(-1,2))
print(get_sum(1,1))

# time 10 minutes 15 seconds

'''
best practice
def get_sum(a,b):
    return sum(xrange(min(a,b), max(a,b)+1))
    
need +1 because the end is exclusive

xrange:
This defines a range of numbers from start(inclusive) to end(exclusive).

Xrange function parameters
The range function can take three parameters:

Start: Specify the starting position of the sequence of numbers.
End: Specify the ending position of the sequence of numbers
Step: The difference between each number in the sequence.

'''