#字符串的格式化输出
#format 也是一种格式化输出，用{}占位然后 .format调用，不管type
age = 2
s = 'already'
message = ' George said: I am {} years old,{} go to school'.format(age,s)
print(message)

name = 'George'
age = 3
hobby = 'Game'
money = 5.89
message = '{} is {} years old, love {}, and have {} dollars'.format(name, age, hobby, money)
print(message)
