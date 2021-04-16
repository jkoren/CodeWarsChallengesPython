'''
How can you tell an extrovert from an introvert at NSA? Va gur ryringbef, gur rkgebireg ybbxf ng gur BGURE thl'f fubrf.

I found this joke on USENET, but the punchline is scrambled. Maybe you can decipher it? According to Wikipedia, ROT13 (http://en.wikipedia.org/wiki/ROT13) is frequently used to obfuscate jokes on USENET.

Hint: For this task you're only supposed to substitue characters. Not spaces, punctuation, numbers etc. Test examples:

rot13("EBG13 rknzcyr.") == "ROT13 example.";
rot13("This is my first ROT13 excercise!" == "Guvf vf zl svefg EBG13 rkprepvfr!"

# list comprehension
# new_list = [expression(i) for i in old_list if filter(i)]
x = [i for i in range(10)]
print(x)

# This will give the output:
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


'''

def rot13char(letter):
    if letter.isupper():
        num_return_char = (ord(letter) - ord("A") + 13) % 26
        return_char = chr(num_return_char + ord("A"))
    elif letter.islower():
        num_return_char = (ord(letter) - ord("a") + 13) % 26
        return_char = chr(num_return_char + ord("a"))
    else: return letter
    # char = chr(ord("E")+13)  #A = 65 Z = 90  a = 97 z = 122
    return return_char

def rot13(phrase):
    return_phrase = [rot13char(letter) for letter in phrase]
    return "".join(return_phrase)

print(rot13("EBG13 rknzcyr.")) #ROT13 example.
print(rot13("This is my first ROT13 excercise!")) #  == "Guvf vf zl svefg EBG13 rkprepvfr!"
print(rot13("Guvf vf zl svefg EBG13 rkprepvfr!")) #  == "Guvf vf zl svefg EBG13 rkprepvfr!"

'''
best practices

def rot13(message):
  return message.encode('rot13')
  
def rot13(message):
    def decode(c):
        if 'a' <= c <= 'z':
            base = 'a'
        elif 'A' <= c <= 'Z':
            base = 'A'
        else:
            return c
        return chr((ord(c) - ord(base) + 13) % 26 + ord(base))
    return "".join(decode(c) for c in message)
    
import string

def rot13(message):
    first = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    trance = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'
    return message.translate(string.maketrans(first, trance))  
'''