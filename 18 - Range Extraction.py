'''

Range Extraction
A format for expressing an ordered list of integers is to use a comma separated list of either individual integers
or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'.

The range includes all integers in the interval including both endpoints.
It is not considered a range unless it spans at least 3 numbers. For example ("12, 13, 15-17")
Complete the solution so that it takes a list of integers in increasing order and returns
a correctly formatted string in the range format.

Example:

solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
# returns "-6,-3-1,3-5,7-11,14,15,17-20"
Courtesy of rosettacode.org

'''
def collapse_consecutive_list(consecutive_list):
    if len(consecutive_list) > 0 and len(consecutive_list) <= 2:
        return consecutive_list
    if len(consecutive_list) >= 3:
        return_list = []
        return_list.append(str(consecutive_list[0]) + "-" + str(consecutive_list[-1]))
        return return_list

def solution(list):
    consecutive_list = []
    return_string = ""
    for count, item in enumerate(list):
        if count < len(list)-1: #not the last item
            if item+1 != list[count+1]: #next item is not consecutive
                if consecutive_list == []: #this is not a consecutive number
                    return_string += str(item)+","
                if consecutive_list != []: # this IS a consecutive number
                    consecutive_list.append(item)
                    consecutive_list = collapse_consecutive_list(consecutive_list)
                    for item2 in consecutive_list:
                        return_string += str(item2)+","
                    consecutive_list = [];
            if item+1 == list[count+1]: # next item is consecutive
                consecutive_list.append(item)
        if count == len(list)-1: # the last item
            if consecutive_list != []: #this IS a consecutive number
                consecutive_list.append(item)
                consecutive_list = collapse_consecutive_list(consecutive_list)
                for item2 in consecutive_list:
                    return_string += str(item2)
    return return_string


print(solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]))
print(solution([-80,-79,-77,-74,-72,-71,-69,-67,-65,-62,-61,-59,-56,-54,-53,-51,-48,-45,-42,-40-39])

'''
Random Tests
1st 4 seem to be backwards

It should work for random inputs too: '-80,-79,-77,-74,-72,-71,-69,-67,-65,-62,-61,-59,-56,-54,-53,-51,-48,-45,-42,-40-39' should equal '-80,-79,-77,-74,-72,-71,-69,-67,-65,-62,-61,-59,-56,-54,-53,-51,-48,-45,-42,-40,-39'
It should work for random inputs too: '-86--83,-81,-78,-75,-73,-71--69,-67,-64,-61,-59,-56,-53,-52,-50,-48,-45,-42-41' should equal '-86--83,-81,-78,-75,-73,-71--69,-67,-64,-61,-59,-56,-53,-52,-50,-48,-45,-42,-41'
It should work for random inputs too: '-85,-83,-82,-79,-78,-75,-72,-69,-66,-63,-60-59' should equal '-85,-83,-82,-79,-78,-75,-72,-69,-66,-63,-60,-59'
It should work for random inputs too: '-92,-90--88,-85,-83--80,-78,-76,-73,-71,-69,-66--62,-59,-57,-54,-51,-48--46,' should equal '-92,-90--88,-85,-83--80,-78,-76,-73,-71,-69,-66--62,-59,-57,-54,-51,-48--46,-43'


It should work for random inputs too: '-56,-53,-52,-49,-47,-44,-43,-41,-39,-38,' should equal '-56,-53,-52,-49,-47,-44,-43,-41,-39,-38,-36'
It should work for random inputs too: '-51,-48,-46,-44--42,-39,-37--35,-33,-30,-29,-27,-25,-23,-20,-18,-16,-15,-12,-11,-8,-7,-5,-2,1-3,' should equal '-51,-48,-46,-44--42,-39,-37--35,-33,-30,-29,-27,-25,-23,-20,-18,-16,-15,-12,-11,-8,-7,-5,-2,1-3,5'
It should work for random inputs too: '-97,-94--91,-88,-86,-85,-82,-80,-78--76,-73,-71,-69--67,-65,-63,-60,-57--55,-53,-52,-50--48,' should equal '-97,-94--91,-88,-86,-85,-82,-80,-78--76,-73,-71,-69--67,-65,-63,-60,-57--55,-53,-52,-50--48,-46'
It should work for random inputs too: '-51,-49,-46,-44,-41,-40,-37,-36,-34,-31,-28,-27,-24,-23,-20,-17,-16,-13,-11,-10,-8,-7,-4,-3,-1,' should equal '-51,-49,-46,-44,-41,-40,-37,-36,-34,-31,-28,-27,-24,-23,-20,-17,-16,-13,-11,-10,-8,-7,-4,-3,-1,1'
It should work for random inputs too: '-62,-61,-58,-57,-54,-52,-50,-48,-45,-42,-39,-37,-34,-31,-30,-27,-26,-24,-23,-21,-20,-17,-15,-12,-9,-8,-6,-5,-2,12' should equal '-62,-61,-58,-57,-54,-52,-50,-48,-45,-42,-39,-37,-34,-31,-30,-27,-26,-24,-23,-21,-20,-17,-15,-12,-9,-8,-6,-5,-2,1,2'
It should work for random inputs too: '-54,-53,-51,-50,-47,-44,-41,-38,-35,-32,-29,-26,-23--21,-19,-17,-15--10,' should equal '-54,-53,-51,-50,-47,-44,-41,-38,-35,-32,-29,-26,-23--21,-19,-17,-15--10,-7'
It should work for random inputs too: '-55,-52,-51,-49,-47,-46,-43,-42,-40,-38,-35,-33,-30,-28,-27,-24,-21,-20,-18-17' should equal '-55,-52,-51,-49,-47,-46,-43,-42,-40,-38,-35,-33,-30,-28,-27,-24,-21,-20,-18,-17'
Test Passed
It should work for random inputs too: '-59,-57,-55,-54,-51,-48,-46,-44,-43,-40,-38--35,-32,-29,-26,-24,-22,-20--18,-16,-15,-13,-10-9' should equal '-59,-57,-55,-54,-51,-48,-46,-44,-43,-40,-38--35,-32,-29,-26,-24,-22,-20--18,-16,-15,-13,-10,-9'
It should work for random inputs too: '-88,-86,-83,-80,-77,-76,-74,-72--70,-68,-66,-64--62,-59,-57,-55,-53,-51,' should equal '-88,-86,-83,-80,-77,-76,-74,-72--70,-68,-66,-64--62,-59,-57,-55,-53,-51,-48'
Test Passed
It should work for random inputs too: '-68,-65,-64,-61,-59,-57,-54--52,-49,-48,-46,-44,-41,-39,-37,-35,-34,-32,-29,-27,-24,-21,-19,-18,-16,-13-12' should equal '-68,-65,-64,-61,-59,-57,-54--52,-49,-48,-46,-44,-41,-39,-37,-35,-34,-32,-29,-27,-24,-21,-19,-18,-16,-13,-12'
It should work for random inputs too: '-84--82,-79,-78,-75,-73,-71,-68--64,-62,-61,-59,-56,-53,-51,-48,' should equal '-84--82,-79,-78,-75,-73,-71,-68--64,-62,-61,-59,-56,-53,-51,-48,-45'
Test Passed
Test Passed
It should work for random inputs too: '-100,-97,-95,-93,-91--88,-86,-85,-83--81,-79,-77--75,-72,-69,-67,-64,-62,-59,-57,-55,-53,-50,-48,-46-45' should equal '-100,-97,-95,-93,-91--88,-86,-85,-83--81,-79,-77--75,-72,-69,-67,-64,-62,-59,-57,-55,-53
'''