from collections import Counter
import sys
a=int(sys.stdin.readline())
b=[]
for i in range(a):
    b.append(int(sys.stdin.readline()))
print(int(round(sum(b)/a)))
b.sort()
print(int(b[int((len(b)-1)/2)]))

if(a>1):
    cnt=Counter(b).most_common(2)
    if(cnt[0][1]==cnt[1][1]):
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(b[0])
print(max(b)-min(b))