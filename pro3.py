wt,pot=input().split()
r1=abs(len(pot)-len(wt))
for k1 in range(len(wt)):
  if(len(pot)==1 and pot[k1] in wt):
    break
  if(wt[k1]!=pot[k1]):
    r1=r1+1
print(r1)
