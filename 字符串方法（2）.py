# isnumeric() 只包含数字字符
a = '12'

print(a.isnumeric())

# title()
a = 'welcome to china'

print(a.title())  # Welcome To China

# str.join(sequence)指定字符str连接学列seq
str1 = '-'
str2 = ''
seq = ('w', 'e', 'l', 'c', 'o', 'm', 'e')

print(str1.join(seq))  # w-e-l-c-o-m-e
print(str2.join(seq))  # welcome

# str.split(str1, num)join的逆方法，用str1分割str，num指明分割次数
str1 = "It's snowing today"
str2 = ' '

print(str1.split(str2, 1))  # ["It's", 'snowing today']
print(str1.split(str2))  # ["It's", 'snowing', 'today']
print(str1.split('s'))  # ["It'", ' ', 'nowing today']

# center(),ljust(),rjust()居中，左对齐，右对齐(width,[,fillchar])
str1 = 'Welcome to china'

print(str1.center(20, '*'))  # **Welcome to china**
print(str1.ljust(20, '*'))  # Welcome to china****
print(str1.rjust(20, '*'))  # ****Welcome to china

'''
maketrans(),translate(),replace()
maketrans(intab, outtab)
创建一个转换表的字典，第一个参数是需要被转换的
字符串，第二个是转换后的字符串，两者一一对应！！！，长度必须相同。
translate(table)
table里存放的是maketrans转换的表格
replace(old, new[, max])
老字符串替换新字符串
'''
str1 = 'Welcome to China'

print(str1.replace('China','the USA'))  # Welcome to the USA
print(str1.replace(' ', '*'))  # Welcome*to*China

# 转换表
trantab = str1.maketrans('aeiou', '12345')
print(trantab)  # {97: 49, 111: 52, 117: 53, 101: 50, 105: 51}

print(str1.translate(trantab))  # W2lc4m2 t4 Ch3n1