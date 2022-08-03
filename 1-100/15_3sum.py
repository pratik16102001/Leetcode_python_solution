# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for  i in range(len(nums)):
            st = i+1
            sp = len(nums)-1
            while st < sp:
                if nums[st]+nums[sp]+nums[i] < 0:
                    st += 1
                elif nums[st]+nums[sp]+nums[i] > 0:
                    sp -= 1
                else:
                    tp = [nums[i],nums[st],nums[sp]]
                    if tp not in ans:
                        ans.append(tp)
                    st+=1
                    sp-=1
                    
        return ans