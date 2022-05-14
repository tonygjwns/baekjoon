lst = ['c=','c-','dz=','d-','lj','nj','s=','z=']

let=input()
for i in lst:
    let=let.replace(i,"*")
print(len(let))