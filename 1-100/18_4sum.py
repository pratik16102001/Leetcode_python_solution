# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = set()
        nums.sort()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                k , l= j+1 , len(nums)-1
                while k < l:
                    if(nums[i]+nums[j]+nums[k]+nums[l] == target):
                        result.add((nums[i],nums[j],nums[k],nums[l]))
                    if(nums[i]+nums[j]+nums[k]+nums[l] > target):
                        l-=1 
                    else:
                        k+=1 

        return list(result)
        