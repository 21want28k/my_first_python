# 字符串的更新
var1 = 'Hello world！'

print('更新字符串：', var1[:6]+'2018')

'''
输出：更新字符串： Hello 2018
简单的复习一下，分片通过两个冒号隔开的两个索引实现，第一个索引是提取的第一个元素的
编号，而后一个索引则是分片之后剩余部分的第一个元素的编号
'''

# 字符串运算符：
a = 'Hello'
b = 'python'

print('a+b的结果是：', a+b)
print('a*2的结果是：', a*2)
print('a[1]的结果是：', a[1])
print('a[1:4]的结果是：', a[1:4])

if 'H' in a:
    print('H在变量a中')
else:
    print('H不在变量a中')

if 'M' not in a:
    print('M not in variable a')

print(r'\n')

# 输出结果：
'''
a+b的结果是： Hellopython
a*2的结果是： HelloHello
a[1]的结果是： e
a[1:4]的结果是： ell
H在变量a中
M not in variable a
\n
'''

# 字符串格式化操作
format_宽为5 = "'%5d'"
format_0填充 = "'%05d'"
format_左对齐 = "'%-5d'"
format_正数前显示加号 = "'%-+5d'"
format_正数前显示空格 = "'% 5d'"
format_最小宽度和小数点位数 = "'%8.3f'"


print(format_宽为5 % 15)
print(format_0填充 % 15)
print(format_左对齐 % 15)
print(format_正数前显示加号 % 15)
print(format_正数前显示加号 % -15)
print(format_正数前显示空格 % 15)
print(format_正数前显示空格 % -15)
print(format_最小宽度和小数点位数 % 4.33333)

'''
结果：
'   15'
'00015'
'15   '
'+15  '
'-15  '
'   15'
'  -15'
'   4.333'
'''



























