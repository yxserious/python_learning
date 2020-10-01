#print variable
print('hello world')
name = '小白'
print (name)

age = 18
gender = 'male'

print(name, age, gender)#sep default is space
print(name, age, gender, sep='-')#sep='-'can change it to any symbol

#symbol:\n next line
print ('hello\nkitty')

#end default \n , but if we reset it
print('AAA', end= '')
print('BBB',end= '')
print()
#practise
print('Dear xxx:\n', '\tPlease press the link to activate')

#symbol: \n nextline \t tab(4space) \'  \"  \r enter \\
print('george said:\'I wanna eat ice cream \' ')
#'''' is not valid, but " '' " or '""' is okay
#if want to use same, add \, ex:'\'\''  "\"\""
print("george said:'I wanna eat ice cream' ")
#/r print to the front
print('hello\rworld')

#''' will gurantee the same format and print
message = '''
jiushi 
kankna
foool
'''
print(message)
'''
也可以拿来当多行注释
Oh
yeah
'''
print('hello\py\\thon')  #//变成了一个/
print(r'hello\py\thon') #r''raw 原样输出字符，不转义

person = 'zoker'
address = 'temple city'
phone = 10503
print('customer is'+person+'address is'+address+'phone:'+str(phone))
#too long and easy to mistake
# 格式化输出可以无视data type
# %s string similar to str()
print('customer is:%s,address:%s,phone:%s'%(person,address,phone))
# %d digit similar to int()
print('phone:%d' %phone)
# %f float type 小数点后页面的位数而且四舍五入
salary = 8899.32895
print('my salary is:%.1f' %salary)

#practise
movie = 'pikachu'
ticket = 45.9
count = 35
total = ticket * count
message='''
电影：%s
人数：%d
单价：%f
总票价：%.1f
''' % (movie,count,ticket,total)
print(message)