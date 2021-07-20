import random

def quicksort(list,first,last):
    if first < last:
        split = partition(list,first,last)
        quicksort(list,first,split-1)
        quicksort(list,split+1,last)


def partition(list,first,last):
    pivot = list[last]
    i = first-1
    for j in range(first,last):
        if list[j] < pivot:
            i += 1
            list[i],list[j] = list[j],list[i]
    list[i+1],list[last] = list[last],list[i+1]
    return i+1        

list = []
for x in range(20):
    list.append(random.randint(0,30))
print(list)
quicksort(list,0,len(list)-1)
print(list)    


        
