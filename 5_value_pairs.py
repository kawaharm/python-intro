'''
Write a function `valuePair(obj1, obj2, key)` that takes in two objects
and a key (string). The function should return an array containing the
corresponding values of the objects for the given key.

Examples:

const object1 = {name: 'One', location: 'Remote', age: 1};
const object2 = {name: 'Two', location: 'San Francisco'};

valuePair(object1, object2, 'location'); // => [ 'Remote', 'San Francisco' ]
valuePair(object1, object2, 'name'); // => [ 'One', 'Two' ]
'''


def value_pair(obj1, obj2, key):
    newArray = {
        "val1": obj1[key],
        "val2": obj2[key]
    }

    return list(newArray.values())


object1 = {'name': 'One', 'location': 'Remote', 'age': 1}
object2 = {'name': 'Two', 'location': 'San Francisco'}

print(value_pair(object1, object2, 'location'))
print(value_pair(object1, object2, 'name'))
