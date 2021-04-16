'''
In this kata, you will write a function that returns the positions and the values of the "peaks" (or local maxima) of a
numeric array.

For example, the array arr = [0, 1, 2, 5, 1, 0] has a peak at position 3 with a value of 5 (since arr[3] equals 5).

The output will be returned as an object with two properties: pos and peaks. Both of these properties should be arrays.
If there is no peak in the given array, then the output should be {pos: [], peaks: []}.

Example: pickPeaks([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3]) should return {pos: [3, 7], peaks: [6, 3]}
(or equivalent in other languages)

All input arrays will be valid integer arrays (although it could still be empty), so you won't need to validate the input.

The first and last elements of the array will not be considered as peaks (in the context of a mathematical function,
we don't know what is after and before and therefore, we don't know if it is a peak or not).

Also, beware of plateaus !!! [1, 2, 2, 2, 1] has a peak while [1, 2, 2, 2, 3] does not. In case of a plateau-peak,
please only return the position and value of the beginning of the plateau. For example: pickPeaks([1, 2, 2, 2, 1])
returns {pos: [1], peaks: [2]} (or equivalent in other languages)

Have fun!


read left number
read middle number

while there is a right number:
   read right number

if middle number > left and > right
  then it is a peak,
        so save it

if middle number = right
    if its the first time middle = right
    you just got on a plateau
       so save the left number as the start of a plateau and its position
    if its not the first time middle = right
        you are on a plateau so keep going
    if you are at the end of a plateau, if middle is greater than right, save and end

if you are not at the end, move to next number
    left = middle
    middle = right_number
    right = next number

if middle is greater than left, middle is a peak, so save
end
'''

def condense_plateaus(array):
    prev_item = array.pop(0)
    return_array = [[0,prev_item]]
    for indx,item in enumerate(array):
        if item != prev_item:
            return_array.append([indx+1,item])
            prev_item = item
    return return_array

def create_dictionary(positions,peaks):
    pos_peak_dictionary = {
        "pos": positions,
        "peaks": peaks
    }
    return pos_peak_dictionary

def pick_peaks(array):
    peaks, positions = [], []

    if len(array) == 0: return create_dictionary(positions,peaks)

    condensed_enumerated_numbers = condense_plateaus(array)

    if len(condensed_enumerated_numbers) <3: return create_dictionary(positions,peaks)

    index = 0  # for readability of code
    number = 1
    left = condensed_enumerated_numbers.pop(0)
    middle = condensed_enumerated_numbers.pop(0)
    for right in condensed_enumerated_numbers:
        if middle[number] > left[number] and middle[number] > right[number]:
            peaks.append(middle[number])
            positions.append(middle[index])
        left = middle
        middle = right
    return(create_dictionary(positions, peaks))


print(pick_peaks([1,2,3,6,4,1,2,3,2,1])) #, {"pos":[3,7], "peaks":[6,3]})
print(pick_peaks([3,2,3,6,4,1,2,3,2,1,2,3])) #, {"pos":[3,7], "peaks":[6,3]})
print(pick_peaks([3,2,3,6,4,1,2,3,2,1,2,2,2,1])) #, {"pos":[3,7,10], "peaks":[6,3,2]})
print(pick_peaks([2,1,3,1,2,2,2,2,1])) #, {"pos":[2,4], "peaks":[3,2]})
print(pick_peaks([2,1,3,1,2,2,2,2])) #, {"pos":[2], "peaks":[3]})
print(pick_peaks([2,1,3,2,2,2,2,5,6])) #, {"pos":[2], "peaks":[3]})
print(pick_peaks([2,1,3,2,2,2,2,1])) #, {"pos":[2], "peaks":[3]})
print(pick_peaks([1,2,5,4,3,2,3,6,4,1,2,3,3,4,5,3,2,1,2,3,5,5,4,3])) #, {"pos":[2,7,14,20], "peaks":[5,6,5,5]})
print(pick_peaks([])) #,{"pos":[],"peaks":[]})
print(pick_peaks([1,1,1,1])) #,{"pos":[],"peaks":[]})

'''
best practices
def pick_peaks(arr):
    pos = []
    prob_peak = False
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            prob_peak = i
        elif arr[i] < arr[i-1] and prob_peak:
            pos.append(prob_peak)
            prob_peak = False
    return {'pos':pos, 'peaks':[arr[i] for i in pos]}
    
def pick_peaks(arr):
    peak, pos = [], []
    res = { "peaks":[], "pos":[] }
    
    for i in range(1, len(arr)) :
        if arr[i]>arr[i-1] :
            peak, pos = [arr[i]], [i]
        
        elif arr[i]<arr[i-1] :
            res["peaks"] += peak
            res["pos"] += pos
            peak, pos = [], []
    
    return res
'''