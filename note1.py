
myList = [4, 1, 7, 0]
length = len(myList)


for i in range(length-1):
    for j in range(0, length-1-i):
        if myList[j] > myList[j+1]:
            myList[j], myList[j+1] = myList[j+1], myList[j]
            # tmp = myList[j]
            # myList[j] = myList[j+1]
            # myList[j+1] = tmp
print(myList)


'''
1.list:
l = []
l = ['aaa']

2.symbol
+ ---> []+[]
* ---->[]* n
in ------> a in [] true false
not in
is ----> compare id equal
not is

3.system varianle
len(list) ---->int
sorted(list)---> small to large
max()
min()
list() ---->change to list type
enumerate(list) -----> index value

4.what list have:
add element:
append()----> add at the end
extend()----->add one set of element
insert()------>specific location add

remove:
del list[index]
list.remove(obj) ----->remove obj
pop() ----->FIFO
clear() clean element

Other:
count() 
sort()
reverse()

'''
# tuple
# just like read only container, you cant modify
t1 = ()
print(type(t1))  # <class 'tuple'>

t2 = ('hello')
print(type(t2))  # <class 'str'>

t3 = ('aa', 'bb')  # <class 'tuple'>
print(type(t3))

t5 = (1, 2, 3, 4, 4)
print(len(t5))

print(t5.count(4))
print(t5.index(4))

t6 = (4, 7, 3)

# a,b = t1  #valueError: too many value to unpack
# x,y,z = (6,) #valueError: not enough value to unpacl
a, b, c = t6
print(a, b, c)

t1 = (2, 5, 8, 9, 7)
a, *_, c = t1
print(a, c, _)  # 2 7 [5, 8, 9]
a, *b, c = t1
print(a, c, b)  # 2 7 [5, 8, 9]
# * in here will set as unknown and grad whatever left in the element

t2 = (4, 5)+(6, 7)
print(t2)
t3 = (3, 2) * 2
print(t3)

print(t2 is t3)
print(3 in t3)
