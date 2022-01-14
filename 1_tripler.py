'''
Write a function tripler(array) that takes in an array and returns a new array
containing 3 times every element of the original array.

Examples:

tripler([1,2,3]); // => [ 3, 6, 9 ]
tripler([4, 1, 7]); // => [ 12, 3, 21 ]
'''


def tripler(array):
    nArray = []
    for i in array:
        nArray.append(i*3)

    return nArray


print(tripler([1, 2, 3]))
print(tripler([4, 1, 7]))
