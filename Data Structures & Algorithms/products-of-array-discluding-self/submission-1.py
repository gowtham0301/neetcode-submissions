class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n =len(nums)
        dic = [1] * n
        
        lp = 1
        for i in range(n):
            dic[i] = lp
            lp *= nums[i]

        rp = 1
        for j in range(n-1,-1,-1):
            dic[j] *= rp
            rp *= nums[j]

        return dic
            
        

        
        
        