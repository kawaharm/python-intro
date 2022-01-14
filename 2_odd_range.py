'''
Write a function oddRange(end) that takes in a number and returns an array 
containing all positive odd numbers up to `end`.

Examples:

oddRange(13); // => [ 1, 3, 5, 7, 9, 11, 13 ]
oddRange(6); // => [ 1, 3, 5 ]
'''


def oddRange(end):
    array = []
    numCount = -(-end//2)   # ceiling division to get end array length

    for i in range(0, numCount):
        array.append(1+2*i)

    return array


print(oddRange(13))
print(oddRange(6))
