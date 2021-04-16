'''

Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive.
The string can contain any char.

Examples input/output:

XO("ooxx") => true

Examples input/output:

XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false
'''

def number_of_specific_letters(string,search_char):
    count = 0
    for character in string:
        if character == search_char:
            count = count + 1
    return count


def xo(string):
    x_count = number_of_specific_letters(string,"x") + number_of_specific_letters(string,"X")
    o_count = number_of_specific_letters(string,"o") + number_of_specific_letters(string,"O")
    if x_count == o_count:
        return True
    else:
        return False



'''
another solution:
def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')
'''
print(xo("ooxx"))
print(xo("xooxx"))
print(xo("ooxXm"))
print(xo("zpzpzpp"))
print(xo("zzoo"))

