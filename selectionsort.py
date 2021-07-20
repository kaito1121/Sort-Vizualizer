import random 

nums = []
for x in range(10):
    nums.append(random.randint(0,30))

def selctionsort(nums):
    for i in range(0,len(nums)):
        min = nums[i]
        index = i
        for j in range(i,len(nums)):
            if nums[j] < min:
                min = nums[j]
                index = j
        
        nums[i], nums[index] = nums[index], nums[i]
        print(nums)


print(nums)
selctionsort(nums)
print(nums)