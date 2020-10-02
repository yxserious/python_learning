# #append append once everytime
# girls = ['Alice']
# while True:
# 	name = input('Girls name:')
# 	if name == 'quit':
# 		break
# 	girls.append(name)
# print(girls)




# #extend 类似列表的合并  符号 + 也可以用于列表合并

# name = ['apple', 'banana']
# girls.extend(name)
# print(girls) 

# #append 末尾追加
# #insert 特定位置添加
# #extend 一次添加多个元素
# girls.insert(1,'Yello')
# print(girls)

#产生10个不同的随机数并保存到列表
import random
number = []
for i in range(10):
	ran = random.randint(0,100)
	if ran in number:
		pass
	else:
		number.append(ran)

print(number)
#max() find the max
#min() find the min
print(max(number))
print(min(number))

new_number = sorted(number)
print(new_number)

new_number = sorted(number, reverse = True)
print(new_number)

#join()
x ='abc'
y = 'def'
z = ['d','e','f']
print(x.join(y)) #dabceabcf
#从letter之间插入之前的内容，a。join(b)就是a 插入b字符中间

print(list(range(10,1,-3)))

s1 = 'hello'
print(s1.encode('utf-8'))




