ar,br,cr,d = map(int, input().split())
xii = list(map(int, input().split()))
zzz = []
i = 0
for i in range(0, len(xii)):
    for j in range(i, len(xii)):
        for k in range(j, len(xii)):
            zzz.append(sum((br*xii[i], cr*xii[j], d*xii[k])))
print(max(zzz))
