class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num1 = Counter(nums)
        num2 = num1.most_common(k)
        ans = []
        for i in range(len(num2)):
            ans.append(num2[i][0])
        return ans