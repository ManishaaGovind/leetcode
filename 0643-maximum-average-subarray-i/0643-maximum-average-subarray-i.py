class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        window = sum(nums[:k])

        answer = window

        for i in range(k,len(nums)):

            window=window-nums[i-k]+nums[i]
            
            answer=max(answer,window)
        
        return answer/k
        