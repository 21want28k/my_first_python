def jiecheng(n):
    if n == 1:
        return 1
    else:
        return n * jiecheng(n-1)


print(jiecheng(4))


result = 1

for i in range(1,10):
    result *= i

print(result)


def Fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return Fib(n-1) + Fib(n-2)


for i in range(1,10):
    print(Fib(i), end=' ')


list_fib = [0, 1]

n = int(input('输入想要的FIB个数：'))

for i in range(n-2):
    list_fib.append(list_fib[-1] + list_fib[-2])

print(list_fib)



result = 1

for i in range(3):
    result *= 2

print(result)

def chengfang(a, n):
    if n == 1:
        return a
    return a*chengfang(a, n-1)


print(chengfang(2,3))

print(1//2)