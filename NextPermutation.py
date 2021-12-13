# https://leetcode.com/problems/next-permutation/

from bisect import bisect_right
class Solution:
    def nextPermutation(self, nums) -> None:
        i=len(nums)-1
        while i>=0 and nums[i-1] >= nums[i]:
            i-=1
            
        if i<=0:
            nums.reverse()
        else:
            sub=nums[i:][::-1]                            
            y = bisect_right(sub,nums[i-1])           
            sub[y],nums[i-1],=nums[i-1],sub[y]
            nums[i:]=sub