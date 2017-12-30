#append:在列表的末尾追加新的对象
lista=[1,2,3]

lista.append(4)

print(lista)#[1, 2, 3, 4]


#count：统计某个元素在列表中出现的次数
listb=[1,2,2,[1,2],[1,2,[1,2,3]]]

print(listb.count([1,2]))#1
print(listb.count(2))#2


#extend：在一个列表的末尾一次性追加另一个序列中的多个值
listc=[1,2,3]
listd=('a','b')


listc.extend(listd)

print(listc)#[1, 2, 3, 'a', 'b']，可以发现元组也是可以加进列表里面的


#index：用于找到列表里面第一个匹配的元素的索引位置
print(listb.index(2))#1 如果列表里面就没有想要搜索的元素，则会产生异常


#insert:将一个对象插入列表中
listc.insert(2,9)

print(listc)#[1, 2, 9, 3, 'a', 'b']


#pop:移除列表中的一个元素：默认是最后一个，并且返回该元素的值
print(listc.pop())#b
print(listc.pop(2))#9
print(listc)#[1, 2, 3, 'a']
print(listc.pop())#a
print(listc)#[1,2,3]


#remove：移除列表中某个值的第一个匹配项
listc.remove(2)

print(listc)#[1, 3],同样如果列表里面不存在想要移除的某个值，则产生异常


#reverse：将列表反向存放
print(lista)#[1, 2, 3, 4]

lista.reverse()

print(lista)#[4, 3, 2, 1]


#sort:将列表在原位置进行排序
liste=[2,5,2,4,5,7,9]

liste.sort()

print(liste)#[2, 2, 4, 5, 5, 7, 9]

liste.sort(reverse=True)

print(liste)#[2, 2, 4, 5, 5, 7, 9]

#sort的高级排序通过key
listf=['asdf','as','dsgsg','gsdagas']

listf.sort(key=len)

print(listf)#['as', 'asdf', 'dsgsg', 'gsdagas']