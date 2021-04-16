'''
Your task is to construct a building which will be a pile of n cubes.
The cube at the bottom will have a volume of n^3, the cube above will have volume of (n-1)^3 and so on until
the top which will have a volume of 1^3.

You are given the total volume m of the building. Being given m can you find the number n of cubes you
will have to build?

The parameter of the function findNb (find_nb, find-nb, findNb) will be an integer m and you have to return
the integer n such as n^3 + (n-1)^3 + ... + 1^3 = m if such a n exists or -1 if there is no such n.

Examples:
findNb(1071225) --> 45
findNb(91716553919377) --> -1
mov rdi, 1071225
call find_nb            ; rax <-- 45

mov rdi, 91716553919377
call find_nb            ; rax <-- -1
'''

def findNb(total_volume):
    current_volume = 0
    current_cube = 1
    while current_volume < total_volume:
        current_volume += current_cube ** 3
        current_cube += 1
    if current_volume == total_volume:
        return current_cube-1
    else:
        return -1

'''
best practice
def find_nb(m):
    n = 1
    volume = 0
    while volume < m:
        volume += n**3
        if volume == m:
            return n
        n += 1
    return -1
'''

'''
5**3 125
4**3 64
3**3 27
2**3 8
1**3 1
'''

print(findNb(9))
print(findNb(4183059834009)) # 2022
print(findNb(24723578342962)) #-1)
print(findNb(135440716410000)) # 4824)
print(findNb(40539911473216))# 3568)
print(findNb(26825883955641)) # 3218)

#time: 13 minutes