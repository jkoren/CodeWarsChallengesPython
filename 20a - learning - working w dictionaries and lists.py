#  the += operation does something special with lists


res2 = []
res2 += [1]
res2 += [2]
res2 += [3]
res2 += []
res2 += [4]
res2 += [5]
res2 += [6]
print(res2)

res = {"peaks": [], "pos": []}
res["peaks"] += [1]
res["peaks"] += [2]
res["peaks"] += [3]
res["peaks"] += []
res["peaks"] += [4]
res["peaks"] += [5]
print(res)

#learned from
def pick_peaks(arr):
    peak, pos = [], []
    res = {"peaks": [], "pos": []}

    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            peak, pos = [arr[i]], [i]

        elif arr[i] < arr[i - 1]:
            res["peaks"] += peak
            res["pos"] += pos
            peak, pos = [], []

    return res
category = "name"
entry = "jeff"
res2 =  {category:[entry]}
print(res2)

res3 = {"count": 0}
res3["count"] += 1
res3["count"] += 1
#res3["unknown"] += 1
print(res3)


# Python3 Program to check whether a
# given key already exists in a dictionary.

# Function to print sum
def checkKey(dict, key):
    if key in dict.keys():
        print("Present, ", end=" ")
        print("value =", dict[key])
    else:
        print("Not present")

    # Driver Code


dict = {'a': 100, 'b': 200, 'c': 300}

key = 'b'
checkKey(dict, key)

key = 'w'
checkKey(dict, key)