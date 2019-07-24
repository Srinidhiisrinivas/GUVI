ap=int(input())
bp=0
l=[]
for ap in range(1,ap+1):
  l.append(ap)
for ap in range(len(l)):
  for ap in range(ap+1,len(l)):
    bp+=1
print(bp)
