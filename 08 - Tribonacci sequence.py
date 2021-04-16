'''

Well met with Fibonacci bigger brother, AKA Tribonacci.

As the name may already reveal, it works basically like a Fibonacci, but summing the last 3 (instead of 2) numbers of the sequence to generate the next.

So, if we are to start our Tribonacci sequence with [1, 1, 1] as a starting input (AKA signature), we have this sequence:

[1, 1 ,1, 3, 5, 9, 17, 31, ...]
But what if we started with [0, 0, 1] as a signature? As starting with [0, 1] instead of [1, 1] basically shifts the common Fibonacci sequence by once place, you may be tempted to think that we would get the same sequence shifted by 2 places, but that is not the case and we would get:

[0, 0, 1, 1, 2, 4, 7, 13, 24, ...]
Well, you may have guessed it by now, but to be clear: you need to create a fibonacci function that given a signature array/list, returns the first n elements - signature included of the so seeded sequence.

Signature will always contain 3 numbers; n will always be a non-negative number; if n == 0, then return an empty array (except in C return NULL) and be ready for anything else which is not clearly specified ;)

If you enjoyed this kata more advanced and generalized version of it can be found in the Xbonacci kata

[Personal thanks to Professor Jim Fowler on Coursera for his awesome classes that I really recommend to any math enthusiast and for showing me this mathematical curiosity too with his usual contagious passion :)]

Test.describe("Basic tests")
Test.assert_equals(tribonacci([1, 1, 1], 10), [1, 1, 1, 3, 5, 9, 17, 31, 57, 105])
Test.assert_equals(tribonacci([0, 0, 1], 10), [0, 0, 1, 1, 2, 4, 7, 13, 24, 44])
Test.assert_equals(tribonacci([0, 1, 1], 10), [0, 1, 1, 2, 4, 7, 13, 24, 44, 81])
Test.assert_equals(tribonacci([1, 0, 0], 10), [1, 0, 0, 1, 1, 2, 4, 7, 13, 24])
Test.assert_equals(tribonacci([0, 0, 0], 10), [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
Test.assert_equals(tribonacci([1, 2, 3], 10), [1, 2, 3, 6, 11, 20, 37, 68, 125, 230])
Test.assert_equals(tribonacci([3, 2, 1], 10), [3, 2, 1, 6, 9, 16, 31, 56, 103, 190])
Test.assert_equals(tribonacci([1, 1, 1], 1), [1])
Test.assert_equals(tribonacci([300, 200, 100], 0), [])
Test.assert_equals(tribonacci([0.5, 0.5, 0.5], 30), [0.5, 0.5, 0.5, 1.5, 2.5, 4.5, 8.5, 15.5, 28.5, 52.5, 96.5, 177.5, 326.5, 600.5, 1104.5, 2031.5, 3736.5, 6872.5, 12640.5, 23249.5, 42762.5, 78652.5, 144664.5, 266079.5, 489396.5, 900140.5, 1655616.5, 3045153.5, 5600910.5, 10301680.5])

'''

def tribonacci(signature,number_of_elements):
    sequence = signature
    if number_of_elements < 3:
        sequence = signature[0:number_of_elements]
    else:
        sum = signature[0] + signature[1] + signature[2]
        for index in range(3,number_of_elements):
            sequence.append(sum)
            sum = sequence[index-2] + sequence[index-1] + sequence[index]
    return sequence

print(tribonacci([1, 1, 1], 10)) # [1, 1, 1, 3, 5, 9, 17, 31, 57, 105]
print(tribonacci([0, 0, 1], 10)) # [0, 0, 1, 1, 2, 4, 7, 13, 24, 44])
print(tribonacci([0, 1, 1], 10)) # [0, 1, 1, 2, 4, 7, 13, 24, 44, 81])
print(tribonacci([1, 0, 0], 10)) # [1, 0, 0, 1, 1, 2, 4, 7, 13, 24])
print(tribonacci([0, 0, 0], 10)) # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
print(tribonacci([1, 2, 3], 10)) # [1, 2, 3, 6, 11, 20, 37, 68, 125, 230])
print(tribonacci([3, 2, 1], 10)) #  [3, 2, 1, 6, 9, 16, 31, 56, 103, 190])
print(tribonacci([1, 1, 1], 1)) # [1])
print(tribonacci([300, 200, 100], 0)) # [])
print(tribonacci([0.5, 0.5, 0.5], 30))# [0.5, 0.5, 0.5, 1.5, 2.5, 4.5, 8.5, 15.5, 28.5, 52.5, 96.5, 177.5, 326.5,
# 600.5, 1104.5, 2031.5, 3736.5, 6872.5, 12640.5, 23249.5, 42762.5, 78652.5, 144664.5, 266079.5, 489396.5, 900140.5,
# 1655616.5, 3045153.5, 5600910.5, 10301680.5])

# 32 minutes including time playing with Find/Replace in PyCharm
'''
best practice
def tribonacci(signature, n):
  res = signature[:n]
  for i in range(n - 3): res.append(sum(res[-3:]))
  return res
'''