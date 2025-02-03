def bubble_sort(lst):
    n = len(lst)
    for i in range(n,0,-1):
        for j in range(i-1):
            if lst[j] > lst[j+1]:
                lst[j+1],lst[j] = lst[j], lst[j+1]
    return lst

#example
lst = [6,53,1,34,62,75,35,23,76,53,42,12,43]
print(bubble_sort(lst))
#%%
def binary_search(lst,target):
    left , right = 0, len(lst) - 1
    while left <= right:
        middle = (left + right) // 2
        if lst[middle] < target :
            left = middle + 1
        elif lst[middle] > target:
            right = middle - 1
        else:
            return middle
    return -1

lst = [41,241,320,450,550,600]
target = 241
print(binary_search(lst,target))