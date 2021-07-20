import random 

nums = []
for x in range(10):
    nums.append(random.randint(0,30))

def mergesort(nums):
    if len(nums) > 1:
        center = int(len(nums)/2)
        l = nums[:center]
        r = nums[center:]
        mergesort(l)
        mergesort(r)
        i = j = n = 0
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                nums[n] = l[i]
                i += 1 
            else:
                nums[n] = r[j]
                j += 1
            n += 1
        while i < len(l):
            nums[n] = l[i]
            i += 1
            n += 1
        while j < len(r):
            print(n)
            nums[n] = r[j]
            j += 1
            n += 1

print(nums)
mergesort(nums)
print(nums)