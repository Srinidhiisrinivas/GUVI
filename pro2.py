from itertools import combinations
a,b=map(int,input().split())
c=len(str(a))
lst=list(combinations(str(a),c-b))
lst=sorted(lst)
print(*lst[0],sep='')
