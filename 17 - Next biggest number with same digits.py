'''
Next bigger number with the same digits
Create a function that takes a positive integer and returns the next bigger number that can be formed by rearranging its digits. For example:

12 ==> 21
513 ==> 531
2017 ==> 2071
nextBigger(num: 12)   // returns 21
nextBigger(num: 513)  // returns 531
nextBigger(num: 2017) // returns 2071
If the digits can't be rearranged to form a bigger number, return -1 (or nil in Swift):

9 ==> -1
111 ==> -1
531 ==> -1
nextBigger(num: 9)   // returns nil
nextBigger(num: 111) // returns nil
nextBigger(num: 531) // returns nil

Jeff's approach
create a list of all the integers with the digits of the original number
order the list
find the number after the original number


original number = 12
original number = 54321

original number = 12345 => 12354
original number = 12354 => 12435
original number = 12435 => 12453

original number = 54321 - no bigger number
original number = 54312 - find last digit that is bigger than previous, switch last 2 digits
original number = 54213 - switch last 2 digits
original number = 51234 - switch last 2 numbers
original number = 45213 - switch last 2 numbers
41253 - 41325 - replace 3rd digit with next higher, then rest small to big

start from end - if digit 4 (2nd to last) is smaller than digit 5 (last), switch last 2 numbers


num_digits = len(str(number))
num_of_combinations = num_digits factorial
'''

def nextBigger(number):
    # if the digits are all high to low, this is the biggest number with these digits
    if str(number).sort(reverse=true) == str(number):
        return -1


        for digit in str(original_number):
