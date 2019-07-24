m=int(input())
q=[]
for i in range(0,m):
  r1=input()
  q.append(r1)
s=[]
for i in zip(*q):
  if(i.count(i[0])==len(i)):
    s.append(i[0])
  else:
    break
print(''.join(s))
