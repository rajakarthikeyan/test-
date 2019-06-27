from collections import Counter
x = int(input())
y = list(map(int,input().split()))
z = Counter(y)
list = []
for i in z.items():
  if(i[1] != 1):
    print(i[0],end = " ")
for j in z.items():
  list.append(j[1])
if(max(list) == 1):
  print("unique")
