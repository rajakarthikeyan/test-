a=int(input())-1
b=list(map(int,input().split()))
c=1
b.sort()
for i in range(a,-1,-1):
c=c*10+b[i]
print(c)
