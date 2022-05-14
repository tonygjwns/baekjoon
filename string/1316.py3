num=int(input())
count=0
import string
for i in range(num):
    let=input()
    for j in let:
        let=let.replace(j+j,j)
    if len(set(list(let))) == len(list(let)):
        count+=1
print(count)
