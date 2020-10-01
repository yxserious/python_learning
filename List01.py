#annoucement

names = ['ironman','spiderman','newthor','blackwidow','hulk']
computer_brands = []

#address

print(id(names))
print(id(computer_brands))

#元素获取使用：下标，索引
print(names[0])
print(names[1])

#获取最后一个元素
print(names[-1])

for name in names: #name = ironman
	if name == 'ironman':
		print('{} exist.'.format(name))
		break
	else:
		print('not exist')

#how to replace list element
for i in range(len(names)):
	#i = 0,1,2,3... pointer
	if 'thor' in names[i]:
		names[i] = 'FatBOY'
		break
print(names) 

#delect del
del names[2]
print(names)

# l=len(names)
# for i in range(l):
# 	if'man'in names[i]:
# 		del names[i]
# 		l -=1
# print(names)

l=len(names)
i = 0
while i <l:
	if 'man' in names[i]:
		del names[i]
		l-=1
	else:
		i+=1
print(names)

'''
输入单词，如果输入单词在列表则删除
最后打印删除后的列表
'''

words = ['hello', 'good', 'apple','world','digit','alpha']
w = input('Please Enter: ')

for word in words: #判断内容有没有在列表中存在
	if w in word: #判断字符串w有没有出现在word
		print('Exist')
		break

