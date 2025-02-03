#%%
# Regular Binary search
def binary_search(lst, target):
    left, right = 0, len(lst) -1
    while left <= right:
        middle = (left + right) // 2
        if lst[middle] > target:
            right = middle - 1
        elif lst[middle] < target :
            left = middle + 1
        else:
            return middle
    return -1
        
# example run:
lst = [34,55,64,77,79,88,90,92,93,751]
target = 55
print(binary_search(lst,target))

 



#%%
####חיפוש בינארי לרשימה מסובבת
def findMin(nums):
    left , right = 0, len(nums) -1
    while left < right:
        middle = (left + right) // 2
        if nums[middle] < nums[right]:
            right = middle
        else:
            left = middle + 1
    return nums[left]

#%%
#Binary_Search with SNAKE ORDERD LIST:
def find(matrix, target):
    n = len(matrix)  
    left, right = 0, n ** 2 - 1


    while left <= right:
        middle = (left + right) // 2

        row = middle // n
        col = middle % n 
        if row % 2 == 1:
            col = n - 1 - col
        if matrix[row][col] > target:
            right = middle - 1
        elif matrix[row][col] < target:
            left = middle + 1
        else:
            return True
    return False

# %%
