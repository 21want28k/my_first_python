# 一个小型的数据库

# 用一个字典表示所有的人的资料，第一层key为他们的名字，第二层基于各自的名字，维护各自的key：phone，address
people = {

    'XiaoXin': {
        'phone': '18351980702',
        'address': 'Nanjing'
    },

    'Bob': {
        'phone': '13260908990',
        'address': 'Beijing'

    }
}

labels ={
    'p': 'phone number',
    'a': 'address'
}

# 输入要查找的名字
name = input('name: ')

# 输入要查找的电话号码/地址
request = input('choose: phone number (p) or address (a) ?')

if request == 'p':
    key = 'phone'
if request == 'a':
    key = 'address'

# 名字必须出现在数据库里面才作为有效。
if name in people:
    print("%s's %s is %s" % (name, labels[request], people[name][key]))

'''
本次学习：
1.字符串格式化时，多个字符串格式化用元组表示
2.为什么不直接用键值作为输入的部分？比如输入phone/address，不是更直观吗？
 想法：可能是因为，为了保密数据库中的信息，不直接显示给用户看，通过内部转换成键值来进行查找。
'''