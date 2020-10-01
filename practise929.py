#1.the first three letter of name backward output

name = 'Joseph'
print(name[2::-1])

#2.sensity word replace to ***
# sensity = 'sexy'
# message = input('Enter message: ')
# if message.find(sensity):
# 	message2 = message.replace(sensity,'*****')
# print(message2)


#delect decond string from first string
str1 = 'they are student'
str2 = 'aeiou'
for i in str1:
	position = str2.find(i)

	if position >= 0:
		str1 = str1.replace(i,'')
print(str1)

#Tony likes word that all upper, word dont continue 

word = input()
#find continue
for i in word:
	pos = word.find(i)
	if pos<len(word)-1 and i == word[pos+1]:
		guess = False
	else:
		guess = True
if (word.isupper()) and guess:
	print('Tony like it')
else:
	print('Tony hate it') 

#循环提示用户输入用户名，密码，邮箱，如果超过20字符只打印前20，输入q或Q表示停止
while True:
	username = input('username: ')
	password = input('password: ')
	email = input('email: ')

	username = username[0:20]
	password = password[0:20]
	email = email[0:20]

	msg = '{}\t{}\t{}\n'.format(username,password,email)
	msg = msg.expandtabs(20)

	s+=msg
	if username=='q' or username=='Q' or password =='q' or password=='Q' or email == 'q' or email == 'Q':
		break
print(s)









