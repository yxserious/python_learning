#注意string type没法比较，需要转换int type
# n1 = int(input('The first number:'))
# n2 = int(input('The second number:'))
# result = n1 > n2
# print('n1>n2',result)

# result = n1 == n2
# print('n1 == n2',result)
# m1 = 'hello'
# m2 = 'hello'
# result = m1 == m2
# print('m1=m2',result)

# username = input('Enter username:')
# uname = 'admin123'
# result = username == uname
# # result = username != uname #如果不等return true
# print('Your username entered is: ',result)

# is 用户对象比较
age = 20
age2 = 20
print(id(age))
print(id(age2))
print(age is age2)

money = 6000
salary = 10000
print(id(money))
print(id(salary))
print(money is salary)

#上面一样的原因是因为python源文件从上到下运行，当发现赋值20再次出现的时候，他重复使用了之前开辟出来的这个20
#交互式的时候不一样的原因是小整数复用【-5，256】，但大整数不复用 

#Oporator Logic
# and or not 
# True and True ---> True 其他结果都是False
#直接搜logic table比较直观

'''
And: 
True And True --- >True
True And False ---> False
False And True ----> False
False And False ----> False

Or:
True or Ture ----> True
True or False ---> True
False or True ----> True
False or False ----> False