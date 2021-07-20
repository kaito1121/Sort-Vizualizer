import random 

nums = []
for x in range(10):
    nums.append(random.randint(0,30))

def bubblesort(nums,last):
    if last == 0:
        return
    for i in range(0,last):
        if nums[i] > nums[i+1]:
            nums[i], nums[i+1] = nums[i+1], nums[i]

    bubblesort(nums,last-1)

print(nums)
bubblesort(nums,len(nums)-1)
print(nums)