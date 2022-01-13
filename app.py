# this is a comment
# TODO built this function

def add(num, num2):
    ''' multi-line comment
    this is suppose to add 2 numbers
    '''


name = "Johnny"
print(name)

nothing = None
print(nothing)

is_working = True
car_off = True

print(is_working)

if is_working or car_off:
    print("this is true")   # this will print
    num = 7
    print("car is off")
elif car_off:
    print("this is the second condition")
else:
    print("this is not true")

if is_working:
    if car_off:
        print("this is working and car off")

# Math
print(15/6)     # 2.5 (decimal division)

print(15//6)    # 2 (integer division)

complex = 1 + 5j + 6 + 2j
print(complex)

print("ace of spades".split(" "))
# => ["ace", "of", "spades"]

print("ace-of-spades".split("-"))
# => ["ace", "of", "spades"]

print("qqxXxqq".index("X"))

print("my code rules"[1:])

if(7 != 7):
    print("these are equal duh")

# Arrays are called "Lists" in Python

a = [1, 23, 6, 17]
a.sort()    # This will mutate list
print(a)

a = a[::-1]  # reverse a string
print(a)

result = a.pop()    # pops last index
print(result)

if 23 in a:
    print("yes 23 is in a")

if 77 in a:
    if 100 in a:
        print("77 and 100 in a")

else:
    print("77 and 100 not in a")

# Dictionaries
# Like objects in Javascript
cat = {
    "name": "Garfield",
    "breed": "orange-fat",
    "fav_food": "lasagna"
}

# no dot notation!
cat["name"]     # "Garfield"
cat["name"] = "Trixie"
print(cat["name"])


print('ITEMS OF CAT', cat.items())
# ITEMS OF CAT dict_items([('name', 'Trixie'), ('breed', 'orange-fat'), ('fav_food', 'lasagna')])
print('KEYS OF CAT', cat.keys())
# KEYS OF CAT dict_keys(['name', 'breed', 'fav_food'])

print('KEYS IN ARRAY', list(cat.keys()))
# KEYS IN ARRAY ['name', 'breed', 'fav_food']
print('VALUES IN ARRAY', list(cat.values()))

# String interpolation
# f in front of string => formatted string
state = "Washington State"
year = 1889
n = 42
my_message = f"{state} was the {n}th state to join the union in {year}."

# using format() method
template = "My name is {} and I like {}"
template.format("Steve", "Cheese")
'My name is Steve and I like Cheese'

player = "Shohei Ohtani"
legend = "Babe Ruth"
message = f"{player} is a better baseball player than {legend}"

warning = "Please wear your {} inside the {}"
warning.format("mask", "nightclub")

vip = True
food_place = "22"
if (food_place == "full" and not vip):
    print("Sorry, we have no room tonight.")
elif (food_place == 22 and not vip):
    print("Please wait 10 minutes for a table.")
else:
    print("Welcome! Come sit down right away.")

# LOOPS
for i in range(0, 10):
    if i % 2 == 0:
        print("{} is even".format(i))
    elif i % 2 == 1:
        print("{} is odd".format(i))

rappers = ["Ye", "Drake", "Eminem"]
for rapper in rappers:
    print(rapper,  "is goated")


def finder(name, city="Honolulu", shop="CVS"):
    if name == "Masa":
        print(f"Hey thats {name}!")
    elif city == "Honolulu":
        print(name, "is from", city)
    elif shop == "Gamestop":
        print("{} frequents {} all the time in {}".format(name, shop, city))


finder("Masa", "Honolulu", "Gamestop")
finder("Marina", "Honolulu", "Gamestop")
finder("Marina", "Kaneohe", "Gamestop")

students = [
    {
        "name": "Kimmie",
        "city": "Atlanta"
    },
    {
        "name": "Chris",
        "city": "Salt Lake City"
    },
    {
        "name": "Zack",
        "city": "Los Angeles"
    }
]


def get_names(students):

    names = []
    for k in students:
        if k.get('name'):
            names.append(k.get('name'))

    return names


print("Students list: ", get_names(students))
