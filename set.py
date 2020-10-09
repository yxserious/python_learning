# list1 = [3, 4, 5, 6, 7, 8, 5, 43, 25, 6, 7,
#          7, 8, 8, 2, 2, 1, 5, 2, 6, 6, 2, 7, 7]
# s1 = set()  # to create empty set, can only use set
# s2 = {1, 3, 7}

# print(type(s2))


# # Apply,the quickest way to clear repeat value set()
# s3 = set(list1)
# print(s3)

# # add
# s1.add('hello')
# s1.add('world')
# s1.add('lucy')
# print(s1)
# # {'hello', 'lucy', 'world'}  set has no order, not depending on the time you put in

# t1 = ('oh', 'yes')
# s1.update(t1)
# print(s1)
# #{'yes', 'oh', 'lucy', 'world', 'hello'}
# # if using add, it will make it as an element
# s1.add(t1)
# print(s1)
# #{'yes', ('oh', 'yes'), 'lucy', 'oh', 'hello', 'world'}
# # pop random remove, but usually the first element
# s1.remove('oh')
# print(s1)
# s1.pop()
# print(s1)
# s1.pop()
# print(s1)

# s1.clear()
# print(s1)

# discard(), same as remove, but if remove not exist element will not be error

# practise
# create 1~20 random number, clear the repeat one
# input a number to delete
import random
list1 = []
set1 = set()

for i in range(10):
    ran = random.randint(1, 20)
    list1.append(ran)
# set1.update(list1)
set1 = set(list1)
print(list1)
print(set1)

num = int(input('please input a number:'))
set1.discard(num)
print('result: ', set1)


#intersection, union
'''
s1:12345
s2:4567
-: s1 - s2 the different in s1  #123
&: s1 & s2 the same between s1 and s2 #45
|: s1 | s2 the total of s1 and s2 #1234567 

^: s1 ^ s2 the different number in s1 and s2 #12367
symetric difference()

find different
find same
'''
l1 = [5, 1, 2, 9, 0, 3]
l2 = [7, 2, 5, 7, 9]

s1 = set(l1)
s2 = set(l2)


result = (s1 | s2) - (s1 & s2)
print(result)

result = s1 ^ s2
print(result)


'''
different_update()
interesection_update()
union_update()
symeetric-different_update()
'''

s1.difference_update(s2)
print(s1)
