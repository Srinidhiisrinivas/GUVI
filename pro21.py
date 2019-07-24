a11 = int(input())
a22 = list(map(int, input().split()))
a33 = int(len(a22)/2)
if sum(a22[:a33])//len(a22[:a33]) == sum(a22[a33:])//len(a22[a33:]):
    print('yes')
else:
    print('no')
