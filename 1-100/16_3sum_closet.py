# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

# Return the sum of the three integers.

# You may assume that each input would have exactly one solution.

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans=0
        min1=1111111111111
     
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            low=i+1
            high=len(nums)-1
       
            while(low<high):
                sum1=nums[low]+nums[high]+nums[i]
                if abs(target-sum1)<min1:
                    min1=abs(target-sum1)
                    ans=sum1
                if sum1<target:
                    low+=1
                elif sum1>target:
                    high-=1    
                else:
                    return target
        return ans