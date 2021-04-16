'''
Write a function called that takes a string of parentheses, and determines if the order of the parentheses is valid.
The function should return true if the string is valid, and false if it's invalid.

Examples
"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true
Constraints
0 <= input.length <= 100

Along with opening (() and closing ()) parenthesis, input may contain any valid ASCII characters.
Furthermore, the input string may be empty and/or not contain any parentheses at all.
Do not treat other forms of brackets as parentheses (e.g. [], {}, <>).

Test.assert_equals(valid_parentheses("  ("),False)
Test.assert_equals(valid_parentheses(")test"),False)
Test.assert_equals(valid_parentheses(""),True)
Test.assert_equals(valid_parentheses("hi())("),False)
Test.assert_equals(valid_parentheses("hi(hi)()"),True)


create a blank list
for each letter of input
    if open parenthesis, add to list
    if closed parenthesis
        if the list is empty - fail
        else take the last off the list
            if they don't match, fail
if there is anything left, fail
'''

def valid_parentheses(string):
    stack = []
    for letter in string:
        if letter == "(": stack.append(letter)
        if letter == ")":
            if len(stack)==0: return False  #if stack is empty; ie no matching left parenthesis
            stack.pop()
    if len(stack)>0: return False #unused left parenthesis
    return True

print(valid_parentheses("  (")) #False)
print(valid_parentheses(")test")) #False)
print(valid_parentheses("")) #True)
print(valid_parentheses("hi())(")) #False
print(valid_parentheses("hi(hi)()")) #True)

'''
best practices

def valid_parentheses(string):
    cnt = 0
    for char in string:
        if char == '(': cnt += 1
        if char == ')': cnt -= 1
        if cnt < 0: return False
    return True if cnt == 0 else False
    

'''