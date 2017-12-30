#浅拷贝
import copy
lista=[1,2,3,[4,5,6,[7,8,9]]]
listb=copy.copy(lista)

print(listb)#[1, 2, 3, [4, 5, 6, [7, 8, 9]]]

print(id(lista))#140519219542152
print(id(listb))#140519249372744
#指向的内存地址已经发生了变化

print(id(lista[0]))#10919424
print(id(listb[0]))#10919424
#指向了同一片内存地址，是不是证明了number不可变类型？

print(id(lista[3]))#140585326668744
print(id(listb[3]))#140585326668744

#深拷贝

listb=copy.deepcopy(lista)

print(id(lista))#140519219542152
print(id(listb))#139760068305672

print(id(lista[0]))#10919424
print(id(listb[0]))#10919424
#指向了同一片内存地址，是不是证明了number不可变类型？

print(id(lista[3]))#140585326668744
print(id(listb[3]))#140585297678920