'''
Write a function `doesKeyExist(obj, key)` that takes in an object and a
key and returns true if the key is inside the object and false if the
key is not inside the object.

Examples:

const obj1 = {company: 'General Assembly', course: 'Software Engineering Immersive'}
doesKeyExist(obj1, 'company'); // => true
doesKeyExist(obj1, 'name'); // => false
'''


def does_key_exist(obj, key):
    keyArray = list(obj.keys())
    for i in range(0, len(keyArray)):
        if keyArray[i] == key:
            return True

    return False


obj1 = {'company': 'General Assembly',
        'course': 'Software Engineering Immersive'}
print(does_key_exist(obj1, 'company'))
print(does_key_exist(obj1, 'name'))
