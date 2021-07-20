import random 

nums = []
for x in range(10):
    nums.append(random.randint(0,30))

def heapsort(nums):
    n = len(nums)
    for i in range(len(nums)-1,-1,-1):
        print(i)
        heapify(nums,n,i)
    for i in range(len(nums)-1,0,-1):
        nums[0],nums[i] = nums[i],nums[0]
        heapify(nums,i,0)



def heapify(nums,n,i):
    largest = i
    l = 2*i + 1
    r = 2*i + 2
    if l < n and nums[largest] < nums[l]:
        largest = l
    if r < n and nums[largest] < nums[r]:
        largest = r
    if largest != i:
        nums[largest], nums[i] = nums[i], nums[largest]
        heapify(nums, n, largest)



    

print(nums)
heapsort(nums)
print(nums)