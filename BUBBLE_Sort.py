#%% Bubble-Sort O(n*2)
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

#%% Merge-Sort O(n log n)
def merge_sort(lst):
    n = len(lst)
    if n == 1:
        return lst
    left = merge_sort(lst[:n//2])
    right = merge_sort(lst[n//2:])

    return merge(left ,right)

def merge(lst1,lst2):
    merged_list = []
    lst1_idx, lst2_idx = 0, 0
    while lst1_idx < len(lst1) and lst2_idx < len(lst2):
        if lst1[lst1_idx] < lst2[lst2_idx]:
            merged_list.append(lst1[lst1_idx])
            lst1_idx += 1
        else:
            merged_list.append(lst2[lst2_idx])
            lst2_idx += 1
    merged_list += lst1[lst1_idx:] + lst2[lst2_idx:]
    return merge_sort



#%% Bucket-Sort O(n)
def bucket_sort(lst,max):
    buckets = [0] * (max + 1)
    for item in lst:
        buckets[item] += 1
    lst[:] = []
    for num, count in enumerate(buckets):
        lst.extend(count * [num])

