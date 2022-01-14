'''
Write a function `adults(people)` that takes in an array of person
objects. The function should return an array containing the names of
those who have an age of 18 or higher.

Example:

const ppl = [
  {name: 'Khalid Robinson', age: 22},
  {name: 'Ariel Winter', age: 20},
  {name: 'Post Malone', age: 25},
  {name: 'Willow Smith', age: 17}
];

adults(ppl); // => [ 'Khalid Robinson', 'Ariel Winter', 'Post Malone' ]
'''


def adults(people):
    youLegal = []
    for i in people:
        if i.get('age') >= 18:
            youLegal.append(i.get('name'))

    return youLegal


ppl = [
    {'name': 'Khalid Robinson', 'age': 22},
    {'name': 'Ariel Winter', 'age': 20},
    {'name': 'Post Malone', 'age': 25},
    {'name': 'Willow Smith', 'age': 17}
]

print(adults(ppl))
