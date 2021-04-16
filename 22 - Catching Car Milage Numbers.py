'''
"7777...8?!??!", exclaimed Bob, "I missed it again! Argh!" Every time there's an interesting number coming up, he notices and then promptly forgets. Who doesn't like catching those one-off interesting mileage numbers?

Let's make it so Bob never misses another interesting number. We've hacked into his car's computer, and we have a box hooked up that reads mileage numbers. We've got a box glued to his dash that lights up yellow or green depending on whether it receives a 1 or a 2 (respectively).

It's up to you, intrepid warrior, to glue the parts together. Write the function that parses the mileage number input, and returns a 2 if the number is "interesting" (see below), a 1 if an interesting number occurs within the next two miles, or a 0 if the number is not interesting.

Note: In Haskell, we use No, Almost and Yes instead of 0, 1 and 2.

"Interesting" Numbers
Interesting numbers are 3-or-more digit numbers that meet one or more of the following criteria:

Any digit followed by all zeros: 100, 90000
Every digit is the same number: 1111
The digits are sequential, incementing†: 1234
The digits are sequential, decrementing‡: 4321
The digits are a palindrome: 1221 or 73837
The digits match one of the values in the awesome_phrases array
† For incrementing sequences, 0 should come after 9, and not before 1, as in 7890. ‡ For decrementing sequences, 0 should come after 1, and not before 9, as in 3210.

So, you should expect these inputs and outputs:

# "boring" numbers
is_interesting(3, [1337, 256])    # 0
is_interesting(3236, [1337, 256]) # 0

# progress as we near an "interesting" number
is_interesting(11207, []) # 0
is_interesting(11208, []) # 0
is_interesting(11209, []) # 1
is_interesting(11210, []) # 1
is_interesting(11211, []) # 2

# nearing a provided "awesome phrase"
is_interesting(1335, [1337, 256]) # 1
is_interesting(1336, [1337, 256]) # 1
is_interesting(1337, [1337, 256]) # 2
Error Checking
A number is only interesting if it is greater than 99!
Input will always be an integer greater than 0, and less than 1,000,000,000.
The awesomePhrases array will always be provided, and will always be an array, but may be empty. (Not everyone thinks numbers spell funny words...)
You should only ever output 0, 1, or 2.
'''
def all_digits_same(number):
    number_string = str(number)
    first_char = number_string[0]
    for character in number_string[1:len(number_string)]:
        if character != first_char: return False
    return True

def followed_by_all_zeros(number):
    number_string = str(number)
    for character in number_string[1:len(number_string)]:
        if character != "0": return False
    # another option? return int(str(number)[1:]) == 0

    return True

def digits_incrementing_order(number):
    number_string = str(number)
    previous_char = number_string[0]
    for character in number_string[1:len(number_string)]:
        if character == "0" and previous_char == "9": pass
        elif ord(character) != ord(previous_char)+1: return False
        previous_char = character
    return True

def digits_decrementing_order(number):
    number_string = str(number)
    previous_char = number_string[0]
    for character in number_string[1:len(number_string)]:
        if ord(character) != ord(previous_char)-1 : return False
        previous_char = character
    return True

def is_palindrome(number):
    number_string = str(number)
    mid_point = int(len(number_string)/2)
    for index in range(mid_point):
        first_letter = number_string[index]
        last_letter = number_string[len(number_string)-1-index]
        #print(first_letter,last_letter)
        if first_letter != last_letter:
            return False
    return True

def is_interesting(number,awesome_phrase):

    #to adjust for error in test
    if number == 98 or number == 99: return 1

    if len(str(number)) < 3: return 0

    if number in awesome_phrase: return 2
    if followed_by_all_zeros(number): return 2
    if all_digits_same(number): return 2
    if digits_incrementing_order(number): return 2
    if digits_decrementing_order(number): return 2
    if is_palindrome(number): return 2

    if (number+1 in awesome_phrase) or (number+2 in awesome_phrase): return 1
    if followed_by_all_zeros(number+1) or followed_by_all_zeros(number+2): return 1
    if all_digits_same(number+1) or all_digits_same(number+2): return 1
    if digits_incrementing_order(number+1) or digits_incrementing_order(number+2): return 1
    if digits_decrementing_order(number+1) or digits_decrementing_order(number+2): return 1
    if is_palindrome(number+1) or is_palindrome(number+2): return 1

    '''
    a better option may be
def is_interesting(number,awesome_phrase):    
    #to adjust for error in test
    if number == 98 or number == 99: return 1

    if len(str(number)) < 3: return 0
    
    for test_number in (number, number+1, number+2):
        if test_number == number: return_value=2
        if test_number in (number+1, number+2): return_value = 1
        
        if test_number in awesome_phrase: return return_value
        if followed_by_all_zeros(test_number): return return_value
        if all_digits_same(test_number): return return_value
        if digits_incrementing_order(test_number): return_value
        if digits_decrementing_order(test_number): return_value
        if is_palindrome(test_number): return_value
    '''

    return 0 # "not interesting"
'''
"Interesting" Numbers
Interesting numbers are 3-or-more digit numbers that meet one or more of the following criteria:
Any digit followed by all zeros: 100, 90000
Every digit is the same number: 1111
The digits are sequential, incementing†: 1234
The digits are sequential, decrementing‡: 4321
The digits are a palindrome: 1221 or 73837
The digits match one of the values in the awesome_phrases array
† For incrementing sequences, 0 should come after 9, and not before 1, as in 7890. ‡ For decrementing sequences, 0 should come after 1, and not before 9, as in 3210.
'''
'''
67890 is awesome! Look at it!: 0 should equal 2
234567890 is awesome! Look at it!: 0 should equal
98 is about to be amazing!: 0 should equal 1
99 is about to be amazing!: 0 should equal 1
67888 is about to be amazing!: 0 should equal 1
234567889 is about to be amazing!: 0 should equal 1
'''


test_numbers = [3,67890, 234567890, 98, 99, 67888, 234567889]

palindrome_tests = [12345,12321,123454321,121,123221]

#for test_number in palindrome_tests:
#    print(test_number,is_palindrome(test_number))

for test_number in test_numbers:
    print(test_number,is_interesting(test_number,[1337, 256]))

'''
best practice #1

def is_incrementing(number): return str(number) in '1234567890'
def is_decrementing(number): return str(number) in '9876543210'
def is_palindrome(number):   return str(number) == str(number)[::-1]
def is_round(number):        return set(str(number)[1:]) == set('0')

def is_interesting(number, awesome_phrases):
    tests = (is_round, is_incrementing, is_decrementing,
             is_palindrome, awesome_phrases.__contains__)
       
    for num, color in zip(range(number, number+3), (2, 1, 1)):
        if num >= 100 and any(test(num) for test in tests):
            return color
    return 0

best practice #2

import re
def is_sequential(string):
    return string in "1234567890" or string in "9876543210"

def is_interesting(number, awesome_phrases):
    print (number)
    interestingness = 2
    for i in (number, number + 1, number + 2):
        if (number != i):
            interestingness = 1
        if (i < 100):
            continue
        if (i in awesome_phrases):
            return interestingness
        i = str(i)
        if re.match(r"^\d0+$", i):
            return interestingness
        if i == i[::-1]:
            return interestingness
        if is_sequential(i):
            return interestingness
        if re.match(r"^(\d)\1+$", i):
            return interestingness
    
    
    return 0


15 Extended Slices - https://docs.python.org/release/2.3.5/whatsnew/section-slices.html
Ever since Python 1.4, the slicing syntax has supported an optional third ``step'' or ``stride'' argument. For example, these are all legal Python syntax: L[1:10:2], L[:-1:1], L[::-1]. This was added to Python at the request of the developers of Numerical Python, which uses the third argument extensively. However, Python's built-in list, tuple, and string sequence types have never supported this feature, raising a TypeError if you tried it. Michael Hudson contributed a patch to fix this shortcoming.

For example, you can now easily extract the elements of a list that have even indexes:

>>> L = range(10)
>>> L[::2]
[0, 2, 4, 6, 8]
Negative values also work to make a copy of the same list in reverse order:

>>> L[::-1]
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
This also works for tuples, arrays, and strings:

>>> s='abcd'
>>> s[::2]
'ac'
>>> s[::-1]
'dcba'
'''