class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans=0
        for i in range(len(nums)+1):
            ans+=i
        for j in nums:
            ans-=j
        return ans
    
class Solution2:
    def missingNumber(self, nums: List[int]) -> int:
        incompleteHash={i:True for i in range(len(nums)+1)}
        for i in nums:
            if i in incompleteHash: incompleteHash.pop(i)
        return next(iter(incompleteHash))
    
class Solution3:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        ans=int((n)*(n+1)/2)
        for j in nums:
            ans-=j
        return ans