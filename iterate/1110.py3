num=int(input())
count=1
temp=(num%10)*10+((num//10+num%10)%10)
while (temp!=num):
    temp=(temp%10)*10+((temp//10+temp%10)%10)
    count+=1
print(count)