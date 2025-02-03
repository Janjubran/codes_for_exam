#%%
def rotate(nums, k):
    n = len(nums)
    k = k % n  
    nums[:] = nums[-k:] + nums[:-k]
    return nums

#
nums = [1,2,3,4,5,6]
k = 2
print(rotate(nums, k)) 


#%%
lst = [1,2,3,4,5]
n = len(lst)
for i in range(n,0,-1):
    print(i)
print('##############')
for i in range(0,n):
    print(i)
# %%
def return_factorial(n):
    if n ==1:
        return n
    return n * (return_factorial(n-1))
n = 5
print(return_factorial(n))
# %%
def fun(A,k):
    max_avg = 0
    current_avg = 0

    if max_avg< current_avg:
        max_avg = current_avg
    current_sum = 0
    for i in range(k):
        current_sum += A[]
        current_avg = current_sum / k
    for i in range(k,n, 1):
        current_sum = current_sum - A[k-i] + A[k]
#%%%%%%%%%%%%%%%
def binary_search(lst,target):
    left, right = 0, len(lst) - 1
    while left<= right:
        middle = (left + right) //2
        if lst[middle] < target :
            left = middle + 1
        elif lst[middle] > target:
            right = middle - 1
        else:
            return middle
    return -1
#%%
def bubble_sort(lst):
    n = len(lst)
    for i in range(n,0,-1):
        for j in range(i-1):
            if lst[j] > lst[j+1]:
                lst[j+1],lst[j] = lst[j],lst[j+1]
    return lst
print(bubble_sort(lst=[2,4,1,3,6,9,7]))

# %%
def remove_from_list(lst, id):
    curr = lst
    prev = lst
    while curr:
        if curr.id == id:
            if prev is lst :
                lst = curr.next
            else:
                prev.next = curr.next
            prev = curr
            curr = curr.next
    return lst
if