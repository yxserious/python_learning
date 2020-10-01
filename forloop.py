#用户只能登陆三次，三次之后锁定
#如何使用break

# for i in range(3):
# 	username = input('请输入账户：')
# 	password = input('请输入密码：')

# 	if username == 'DIO' and password == '123':
# 		print('Welcome {}'.format(username))
# 		print('Enjoy!')
# 		break #跳出循环结构
# 	else:
# 		print('Try Again~')
# else: #这个else属于循环整体，所以break跳过他了
# 	print('Account has been locked')

'''
range(n) ~range(0,n)
range(m,n) ~range(start,end)
range(m,n,step) ~range(start,end,step) step是每次跳多少个,步长
'''

#while loop
# n=3
# while n<=30:
# 	if n%3==0 
# 		print('------',n)
# 	n+=1

#用while计算1-20的累加和
# Sum = 0
# i=1
# while i<=20:
# 	Sum += i
# 	i += 1
# print(Sum)

'''
嵌入式循环
打印三角形
*
**
***
****
*****
'''

# ceng = 1
# while ceng <=5:
# 	print('*'*ceng)
# 	ceng+=1

#写一个99乘法表
'''
1*1=1
1*2 = 2 2*2 = 4
1*3 = 3 2*3 = 6 3*3 = 9
'''
# ceng = 1
# while ceng<=9:
# 	count=1
# 	while count<=ceng:
# 		result = count * ceng
# 		print('{}*{}={} '.format(count, ceng, result),end = '')
# 		count += 1
# 	ceng+=1
# 	print()


'''
1.欢迎进入澳门皇家赌场
2.输入用户名，默认用户没币
3.提示用户充值（100块30币，充值100的倍数，充值不成功再次充值）
4.玩一局扣2个币，猜大小（系统随机模拟骰子）
5.猜对了奖励1个币，可以继续（想不想继续，也可以没有金币自动退出）
'''
import random
print('*'*5)
print('澳门皇家赌场上线啦')
print('*'*5)

coins= 0
for i in range (3):
	username = input('请输入用户名：')
	password = input('请输入密码：')
	if username == 'DIO' and password == '1024':
		while coins<2:
			charge = int(input('100块10币，充值100的倍数:'))
			if charge%100 == 0 and charge >0:
				coins += (charge//100)*10

		print('你有游戏币:{}，每局扣2个'.format(charge))
		print('Entering Game')
		wile True:

			t1 = random.randint(1,6)
			t2 = ramdom.randint(1,6)
			result = t1+t2
			charge -= 2
			#猜大小，大于6还是小于6
			guess = input('greater or less(g/l'):
			if (guess == 'g' and result > 6) or (guess == 'l'and result < 6):
				coins += 1
			else:
				pass
			answer = input('还来不？（y/n)')
			if answer!= 'y' or money <2:
				break

	else:
		print('wrong enter again')
else:
	print('Account has been locked')


