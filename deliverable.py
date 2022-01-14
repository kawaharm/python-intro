# All README material get tested here

# Task 1
True and False  # False
True and not (False or False)  # True
not True and not (False or False)  # False
"cat"+"dog"  # catdog
number = 2
food = "pizza"
combine = f"{number}{food}"
# 2pizza
food = "fish"
# food*2.5
# ValueError
5 >= 11  # False
'new york'[0]   # n
'san francisco'[2*3]  # a
# 'engineering'.index('G')   # ValueError
'engineering'.index('neer')  # 4
'engineering'.index('r') > -1    # True
# print('science'.index('x') == -1)   # ValueError

# TASK 2
# 1
# idx = 'abcde'.index('D')
# idx = idx + 11
# print(idx)  # ValueError
# idx * 2
# print(idx)  # ValueError

# 2
num = 33
isEven = num % 2 == 0
print(isEven)   # False
print(not isEven)   # True

# 3
str1 = 'marker'
num = len('whiteboard') - len(str1)
print(num)  # 4
str2 = 'bootcamp'
print(str2[num].upper())    # C
