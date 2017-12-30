n=int(input())
cnt = 0
if n<0:
    n=n&0xff
    print(bin(n))
while n:
    cnt+=1
    n = (n-1) & n
print(cnt)
