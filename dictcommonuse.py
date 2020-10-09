'''
add element(key:valie)
dict[key] = value
same key will change value
key is uniquq,value can be repeat
wrong:
{money:100, money:200}
correct
{money01:100, money02:100, money03:100}

add element compare:
list1=[]
list1.append(element)

dict1 = ()
dict1[key] = value

change:
list1[index] = newvalue
dict1[key]=newvalue

check:
list1[index] ----> element
dict1[key] ---- > value

find element base on the key
'''

list1 = [3, 5, 7, 9]
print(list1[2])
dict1 = {'1': 'neo', '2': 'leo', '3': 'pink'}
print(dict1['2'])
dict2 = {'neo': 100, 'leo': 100, 'pink': 89}

print(dict2['pink'])

# find the student that score greater than 90
for i in dict2:
    print(i)
# this way can only find the key of dict
# items()values() keys()

print(dict2.items())
# find the student that score greater than 90
# for i in dict2.items():
#     print(i)
for key, value in dict2.items():
    # print(key, value)
    if value > 90:
        print(key)

result = dict2.values()
print(result)

total = 0
num = 0
# find the avg of score
# for score in dict2.values():
#     total += score
#     num += 1

# avg = total/num
# print(avg)
total = sum(dict2.values())
avg = total/len(dict2.values())
print(avg)

# keys() will find all the keys in dict
names = dict2.keys()
print(names)
# find key
for name in names:
    print(name)

# practise: find people neo

print('neo' in dict2)
# print(dict2['neo1'])
# if not correct will return keyerror, so hard to use
# get(key) ----> if cannot find the value will not return error
# get(key,default) ----> if value can be find then return dict value, if not return default
print(dict2.get('neo1'))


# remove
list1 = [3, 7, 9, 0]
del list1[1]
print(list1)

dict3 = {'aa': 100, 'bb': 100, 'cc': 89, 'dd': 99}
del dict3['cc']
print(dict3)

# dict3.remove('bb')
# there is no remove for dict

result = dict3.pop('bb')
print(result)
print(dict3)
result = dict3.pop('aaaa', 'this person is not exist')
print(result)

# popitem()
dict4 = {'aa': 100, 'bb': 100, 'cc': 89, 'dd': 99}
result = dict4.popitem()
print(result)
print(dict4)

# clear()
dict4.clear()
print(dict4)


# update()  合并操作
# fromkeyS(seq)

dict1 = {0: 'gi', 1: 'ti', 2: 'ada'}
dict2 = {0: 'lily', 4: 'ruby'}

dict1.update(dict2)
print(dict1)
'''
#fromkeys(seq,[default]) ---> transfer seq into dict format, if no default return none
                                {'aa':None, 'bb',None,'cc',None}
                        -----> if have default, then use default value 
'''
list1 = ['aa', 'bb', 'cc']
new_dict = dict.fromkeys(list1, 10)
print(new_dict)
