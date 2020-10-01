name = 'steven'
result ='eve' in name 
print(result)

#not in 

result = 'tv' not in name
print(result)

#r 保留原格式 有r就不转义，没有r则转义
name = 'jason'
print(r'%s: \'hahaha!\''%name)

filename = 'picture.png'
print(filename[5]) #通共【】结合位置获取字母，只能一个
#包前不包后
print(filename[0:7])#0123456
print(filename[3:])#省略后面就一直到结尾
print(filename[:7])#省略前面就是从0开始取
#f i l e n a m e . p n g
#0 1 2 3 4 5 6 7 8 9 10 11
print(filename[8:-1])
#一直到n，把倒数第二位
print(filename[:-2])
#一直到倒数第二位

