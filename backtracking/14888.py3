num=int(input())
nums=list(map(int,input().split(" ")))
opps=list(map(int,input().split(" ")))
max_num=-1e9
min_num=1e9

def dps(temp, count,plus,minus,mul,div):
    global min_num
    global max_num
    if(count>=len(nums)):
        max_num=max(temp,max_num)
        min_num=min(temp,min_num)
        return
    if(plus):
        dps(temp+nums[count],count+1,plus-1,minus,mul,div)      
    if(minus):
        dps(temp-nums[count],count+1,plus,minus-1,mul,div) 
    if(mul):
        dps(temp*nums[count],count+1,plus,minus,mul-1,div) 
    if(div):
        dps(int(temp/nums[count]),count+1,plus,minus,mul,div-1)  

dps(nums[0],1,opps[0],opps[1],opps[2],opps[3])
print(max_num)
print(min_num)