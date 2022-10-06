# Snail Sort
# Given an n x n array, return the array elements arranged from outermost elements to the middle
# element, traveling clockwise.
#
# array = [[1,2,3],
#          [4,5,6],
#          [7,8,9]]
# snail(array) #=> [1,2,3,6,9,8,7,4,5]
# For better understanding, please follow the numbers of the next array consecutively:
#
# array = [[1,2,3],
#          [8,9,4],
#          [7,6,5]]
# snail(array) #=> [1,2,3,4,5,6,7,8,9]
# This image will illustrate things more clearly:
#
#
# NOTE: The idea is not sort the elements from the lowest value to the highest; the idea is to
# traverse the 2-d array in a clockwise snailshell pattern.
#
# NOTE 2: The 0x0 (empty matrix) is represented as en empty array inside an array [[]].

result = []

def snail(snail_map):

    temp = snail_map.copy()

    for items in snail_map[0][:-1]:
        result.append(items)

    for i in range(len(snail_map)-1):
        result.append(snail_map[i][-1])

    for items in snail_map[-1][::-1]:
        result.append(items)

    for i in reversed(range(1, len(snail_map)-1)):
        result.append(snail_map[i][0])

    # Creating our new array
    for x in result:
        for i in range(len(temp)):
            if x in temp[i]:
                temp[i].remove(x)

    for idx, values in enumerate(temp):
        if not values:
            temp.remove(values)

    if temp:
        return snail(temp)
        # If i use return snail(temp, result) and def snail(snail_map,[])then works but not allowed

    return result

snail_map = [
    [1,2,3,4,5],
    [16,17,18,19,6],
    [15,24,25,20,7],
    [14,23,22,21,8],
    [13,12,11,10,9]]

array2 = [[1,2,3],
         [8,9,4],
         [7,6,5]]

print(snail(array2))
print(snail(snail_map))
