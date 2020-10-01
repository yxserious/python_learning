# capitalize() title() upper() lower() istitle()  upper case or lower case
#find and replace
#find() rfind() lfind() index() rindex() lindex() replace()

s1 = 'index lucy lucky good'
result = 'x' in s1  #bool
print (result) 

position = s1.find('R') #return -1 means not find
print(position)


position = s1.find('l') #return the first find position, in here is 6
print(position)

#find('letter need to find, start, end')
p = s1.find('o', position+1, len(s1)-5)
print(p)

#rfind(() find from right 
#lfind()) find from left, same as find()
url = "https://www.baidu.com/img/bd_logo1.png"
p2 = url.rfind('/')
print(p2)
kz= url[p2+1:]
print(kz)

s2 = s1.replace(' ', '#')  #replace('old','new', max how many times)
print(s2)


#startswith() endswith() use to check upload format
filename = 'dt.doc'
result = filename.endswith('txt')
print(result) #false doc != txt

# #file upload
# path = input('upload:') #c:\foo\bar\desk.jpg
# p=path.rfind('\\')
# filename = path[p+1:]
# print(p,filename)

#isalpha() isdigit()

#join() will return a string
new_str = '-'.join('abc') # first is use to connect the second 
print(new_str) #a-b-c
#use it on list
list1 = ['a','b','c','d']
result = ''.join(list1)
print(result)

#lstrip() rstrip() remove left space and right space
#split() cut the string and save to list

str3 = 'hello world haha hihi'
new_list = str3.split()









