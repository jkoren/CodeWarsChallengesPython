# didn't pass all tests - didn't know about NONE

'''
Given two arrays a and b write a function comp(a, b) (compSame(a, b) in Clojure) that checks whether the two arrays
have the "same" elements, with the same multiplicities. "Same" means, here, that the elements in b are the elements
in a squared, regardless of the order.

Examples
Valid arrays
a = [121, 144, 19, 161, 19, 144, 19, 11]
b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
comp(a, b) returns true because in b 121 is the square of 11, 14641 is the square of 121, 20736 the square
of 144, 361 the square of 19, 25921 the square of 161, and so on. It gets obvious if we write b's
elements in terms of squares:

a = [121, 144, 19, 161, 19, 144, 19, 11]
b = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
Invalid arrays

If we change the first number to something else, comp may not return true anymore:

a = [121, 144, 19, 161, 19, 144, 19, 11]
b = [132, 14641, 20736, 361, 25921, 361, 20736, 361]
comp(a,b) returns false because in b 132 is not the square of any number of a.

a = [121, 144, 19, 161, 19, 144, 19, 11]
b = [121, 14641, 20736, 36100, 25921, 361, 20736, 361]
comp(a,b) returns false because in b 36100 is not the square of any number of a.

Remarks
a or b might be [] (all languages except R, Shell).
a or b might be nil or null or None or nothing (except in Haskell, Elixir, C++, Rust, R, Shell, PureScript).
If a or b are nil (or null or None), the problem doesn't make sense so return false.

Note for C
The two arrays have the same size (> 0) given as parameter in function comp.

needed further clarification: no: {2, 2, 3} => {2x2, 2x2, 3x3} => {4, 4, 9} != {4, 9, 9}
'''

import math

def comp(array1, array2):
    if len(array1) != len(array2):  # if arrays not the same length
        return False
    else:
        array_lengths = len(array1)

    if array_lengths == 0:  # if arrays are both empty
        return False

    array1.sort()
    array2.sort()

    for index in range(array_lengths):
        if array1[index]**2 != array2[index]:
            return False

    return True

'''
best practice:
def comp(xs, ys):
    if xs is None or ys is None:
        return False
    return sorted(x * x for x in xs) == sorted(ys)
    
# passed all of these
a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
print(comp(a1, a2)) # should be True

a1 = []
a2 = []
print(comp(a1, a2)) # should be False

a1 = [2,2,3]
a2 = [4,9,9]
print(comp(a1, a2)) # should be False

a = [121, 144, 19, 161, 19, 144, 19, 11]
b = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
print(comp(a1, a2)) # should be False

a = [121, 144, 19, 161, 19, 144, 19, 11]
b = [132, 14641, 20736, 361, 25921, 361, 20736, 361]
print(comp(a1, a2)) # should be False

a = [121, 144, 19, 161, 19, 144, 19, 11]
b = [121, 14641, 20736, 36100, 25921, 361, 20736, 361]
print(comp(a1, a2)) # should be False
'''


Test.describe("Basic tests")
a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
test.assert_equals(comp(a1, a2), True)
a1 = [4, 4]
a2 = [1, 31]
test.assert_equals(comp(a1, a2), False)
a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11*21, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
test.assert_equals(comp(a1, a2), False)
a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11*11, 121*121, 144*144, 190*190, 161*161, 19*19, 144*144, 19*19]
test.assert_equals(comp(a1, a2), False)
a1 = []
a2 = []
test.assert_equals(comp(a1, a2), True)
a1 = []
a2 = None
test.assert_equals(comp(a1, a2), False)
a1 = [121, 144, 19, 161, 19, 144, 19, 11, 1008]
a2 = [11*11, 121*121, 144*144, 190*190, 161*161, 19*19, 144*144, 19*19]
test.assert_equals(comp(a1, a2), False)
a1 = [10000000, 100000000]
a2 = [10000000 * 10000000, 100000000 * 100000000]
test.assert_equals(comp(a1, a2), True)
a1 = [10000001, 100000000]
a2 = [10000000 * 10000000, 100000000 * 100000000]
test.assert_equals(comp(a1, a2), False)
a1 = [2, 2, 3]
a2 = [4, 9, 9]
test.assert_equals(comp(a1, a2), False)
a1 = [2, 2, 3]
a2 = [4, 4, 9]
test.assert_equals(comp(a1, a2), True)
a1 = None
a2 = []
test.assert_equals(comp(a1, a2), False)
test.assert_equals(comp([], [1]), False)
a1 = [-121, -144, 19, -161, 19, -144, 19, -11]
a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
test.assert_equals(comp(a1, a2), True)


# 50 minutes
'''
originally:
import math

def comp(array1, array2):

    if len(array1) == 0 or len(array2) == 0:
        return False

    if len(array1) != len(array2):
        return False

    for item1 in array1:
        if not(item1**2 in array2):
            return False

    for item2 in array2:
        if not(math.sqrt(item2) in array1):
            return False
    return True


'''
