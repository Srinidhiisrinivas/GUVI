amm=int(input())
arr=list(map(int,input().split()))
arr.sort(reverse=True)
s0=0
s1=0
res=[]
for i in range(0,amm,2):
    s0=s0+arr[i]
for j in range(1,amm,2):
    s1=s1+arr[j]
res.append([s0,s1])
for i in res:
    print(i[0] if i[0]>i[1] else i[1])
