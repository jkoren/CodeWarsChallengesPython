
'''
'#Find the missing letter

Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.

You will always get an valid array. And it will be always exactly one letter be missing.
The length of the array will always be at least 2.
The array will always contain letters in only one case.

Example:

['a','b','c','d','f'] -> 'e'
['O','Q','R','S'] -> 'P'

["a","b","c","d","f"] -> "e"
["O","Q","R","S"] -> "P"
(Use the English alphabet with 26 letters!)

Have fun coding it and please don't forget to vote and rank this kata! :-)
'''
def find_the_missing_letter(list_of_letters):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    is_lower = list_of_letters[0].islower() #remember the case of the list of letters

    # lop off the beginning of the alphabet
    starting_index = alphabet.find(list_of_letters[0].lower())
    alphabet = alphabet[starting_index:]

    matching_index = 0

    while list_of_letters[matching_index].lower() == alphabet[matching_index]:
        matching_index += 1

    if not is_lower:
        # list_of_letters[matching_index].upper()
        return alphabet[matching_index].upper()
    if is_lower:
        return alphabet[matching_index]

#str.find(sub,start,end)
#returns the lowest index of the substring if it is found in given string. If it’s not found then it returns -1.

print(find_the_missing_letter(["O","P","Q","S"]))
print(find_the_missing_letter(['a','b','c','d','f']))

'''
best practice - compare the ordinal values

def find_missing_letter(chars):
    n = 0
    while ord(chars[n]) == ord(chars[n+1]) - 1:
        n += 1
    return chr(1+ord(chars[n]))
    
best practice

def find_missing_letter(input):
    alphabet = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    start = alphabet.index(input[0])
    for i in range(len(input)):
        if not input[i] == alphabet[start+i]:
            return alphabet[start+i]
'''