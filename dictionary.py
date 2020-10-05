'''
dict
symbol:{}
save element: key:value

list    tuple   dict
[]      ()      {}
ele     ele     key:value

[].append(8)
'''

# dict1 = {}  # empty dictionary
# dict2 = dict()  # not common list1 =list() tuple1 = tuple()

# dict3 = {'ID': '93003000010', 'name': 'lucky', 'age': 18}

# dict4 = dict([('name', 'lucky'), ('age', 18)])
# # 'name':'lucky','age':18
# # dict([(1,2),(3,4)]) will take 1, 2 become 1:2, 3,4 becocme 3:4 dict has to be two element
# # list can transfer to dict, but it has to be two element in same tuple

# # dictionary add remove change search
# dict6 = {}
# # dict6[key]=value

# # add
# dict6['brand'] = 'huawei'
# print(dict6)
# dict6['brand'] = 'iphone'
# print(dict6)
# # same key will change the value
# dict6['type'] = 'p30_pro'
# dict6['price'] = 9000
# dict6['color'] = 'dark'
# print(dict6)

# example:
# register system
# username password email phone

print('welcome')

database = []
while True:
    username = input('Please enter username: ')
    password = input('Please enter password: ')
    repassword = input('Please re-enter password: ')
    email = input('please enter email: ')
    phone = input('what is your phone number: ')
    # for example, user01 define a dict
    user = {}
    user['username'] = username
    if password == repassword:
        user['password'] = password
    else:
        print('The two password you enter is not the same, re-enter: ')
        continue

    user['email'] = email
    user['phone'] = phone
    database.append(user)

    answer = input('continue?(y/n)')
    if answer != 'y':
        break
print(database)
