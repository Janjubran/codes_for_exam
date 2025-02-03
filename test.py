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


# %%
