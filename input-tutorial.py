#input()
# name = input('please enter name') #阻塞式
# print(name)

#Practise
# print('''
# **************
# 澳门赌场上线啦
# **************
# 	''')
# username = input('username:')
# password = input('password:')
# print('%s Please charge!'% username)
# coins= input('Money:')
# coins = int(coins)
# print('%sCharge success! right now you have:%d' %(username,coins))

#发现input来的都是str type, 如果不用format那个方法，就需要添加line 15整形

'''
练习
游戏：英雄联盟
输入角色：xxx
输入拥有装备：xxx
输入想买的装备：xxx
输入付款金额：xxx
xxx有xxx装备，花了xxx
知识点：input，格式化输出print()
'''

# print('''
# ***************
# 	英雄联盟
# ***************
# ''')
# role = input('输入角色:')
# equipment = input('输入拥有装备：')
# upgrade = input('输入想买的装备：')
# equipment = upgrade
# spend = input('输入付款金额：')

# print('{} have {}, have spend {}'.format(role,equipment,spend))

#Operator
name = 'admin'
print(id(name),name)
name1 = name
print(id(name1),name1)
#结果一样的原因是，name= ‘admin’的时候memory里name里存了admin的地址
#然后name1=name的时候相当于也存了admin的地址
# += -= *= /=
num = 9
num += 5 # num = num + 5
a = 'abc'
a += 'def'
print(a) 
# ** //
a=8
b=3
result = a**b
print('**: ',result) #次方
result = a//b
print('//: ',result) #取整数
rsult = a%b
print('%: ',result) #取余数

