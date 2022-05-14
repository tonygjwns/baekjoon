num=input()
nums=[*num]
nums.sort(reverse=True)
ret="".join(nums)
print(ret)