import random 

nums = []
for x in range(10):
    nums.append(random.randint(0,30))

def insertionsort(nums):
    for num in range(1,len(nums)):
        i = num
        while nums[i-1] >= nums[num] and i >0:
            i -= 1
            print(i,nums[i],nums[num])
        nums.insert(i,nums[num])
        nums.pop(num+1)

print(nums)
insertionsort(nums)
print(nums)