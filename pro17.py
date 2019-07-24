com,dom=map(int,input().split())
l=list(map(int,input().split()))
p=0
for i in range(0,com):
    for j in range(1,com):
        if l[i]+l[j]==dom and i!=j:
            p=1
            break
print("yes" if p else "no")
