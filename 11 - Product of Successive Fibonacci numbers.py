'''
The Fibonacci numbers are the numbers in the following integer sequence (Fn):
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, ...
such as
F(n) = F(n-1) + F(n-2) with F(0) = 0 and F(1) = 1.

Given a number, say prod (for product), we search two Fibonacci numbers F(n) and F(n+1) verifying

F(n) * F(n+1) = prod.

Your function productFib takes an integer (prod) and returns an array:

[F(n), F(n+1), true] or {F(n), F(n+1), 1} or (F(n), F(n+1), True)
depending on the language if F(n) * F(n+1) = prod.

If you don't find two consecutive F(m) verifying F(m) * F(m+1) = prod you will return

[F(m), F(m+1), false] or {F(n), F(n+1), 0} or (F(n), F(n+1), False)
F(m) being the smallest one such as F(m) * F(m+1) > prod.

Some Examples of Return:
(depend on the language)

productFib(714) # should return (21, 34, true),
                # since F(8) = 21, F(9) = 34 and 714 = 21 * 34

productFib(800) # should return (34, 55, false),
                # since F(8) = 21, F(9) = 34, F(10) = 55 and 21 * 34 < 800 < 34 * 55

'''
def create_fibonacci_sequence(product):
    # create a fibonacci sequence. stop when last number exceeds product
    fibonacci_sequence = [0,1]
    i = 0;
    new_fibonacci_number = 0
    while new_fibonacci_number < product:
        if i != 0 and i!= 1:
            new_fibonacci_number = fibonacci_sequence[i-1]+fibonacci_sequence[i-2]
            fibonacci_sequence.append(new_fibonacci_number)
        i += 1
    return fibonacci_sequence


def productFib(product):
    # create a fibonacci sequence and work through it in pairs until the product of pair of numbers exceeds the
    # target product passed
    fibonacci_sequence = create_fibonacci_sequence(product) # create a fibonacci sequence to work on
    index = 0
    while fibonacci_sequence[index]*fibonacci_sequence[index+1] < product:
        index +=1
    if fibonacci_sequence[index]*fibonacci_sequence[index+1] == product:  # if product met
        return [fibonacci_sequence[index], fibonacci_sequence[index + 1], True]
    else: #if product exceeded
        return [fibonacci_sequence[index], fibonacci_sequence[index + 1], False]


print(productFib(714)) #should return (21, 34, true),
                # since F(8) = 21, F(9) = 34 and 714 = 21 * 34
print(productFib(800)) # should return (34, 55, false),
                # since F(8) = 21, F(9) = 34, F(10) = 55 and 21 * 34 < 800 < 34 * 55
'''
best practices:

def productFib(prod):
  a, b = 0, 1
  while prod > a * b:
    a, b = b, a + b
  return [a, b, prod == a * b]
  
def productFib(prod):
    a, b = 0, 1
    rez = 0
    while rez < prod:
        a, b = b, a + b
        rez = a*b
    return [a, b, rez == prod]
'''
