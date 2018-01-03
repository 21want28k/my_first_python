# capitalize()
a = 'welcome to China'

print(a.capitalize())  # Welcome to china


# center()
a = 'welcome to China'

print('\'', a.center(25), '\'')  # '      welcome to China     '


# count()
a = "sfsf'fdsa'"

print(a.count('s', 0, 5), end='.')  # 2,print函数，默认输出后带回车，end=以''中的值结尾删去回车
print(a.count('\''))  # 2


# encode() bytes.decode（）
a = '中国'
b = a.encode(encoding='utf-8', errors='strict')

print(b)
print(b.decode('utf-8', errors='strict'))

'''
b'\xe4\xb8\xad\xe5\x9b\xbd'
中国
'''

# endswith()
a = 'books'

print(a.endswith('s', 3))  # True


# expandtabs()
a = '\t'

print(111111111111)
print('\''+a.expandtabs()+'\'')
print('\'', a.expandtabs(), '\'')

'''
自己的新发现：
区分一下上面的这两中输出
111111111111
'        '这是输出一个字符串
'          '这是输出了三个字符串，串与串之间自动用空格隔开了
'''

# find()
a = 'asdcf'

print(a.find('d', 4))


# index()
a = 'abcdefg'

print(a.index('c', 0, 6 ))