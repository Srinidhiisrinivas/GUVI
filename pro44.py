ar,br,cr,d = map(int, input().split())
x = list(map(int, input().split()))
z = []
i = 0
for i in range(0, len(x)):
    for j in range(i, len(x)):
        for k in range(j, len(x)):
            z.append(sum((br*x[i], cr*x[j], d*x[k])))
print(max(z))
