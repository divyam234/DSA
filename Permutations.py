# https://leetcode.com/problems/permutations/

class Solution:
        
    def permute(self, nums):
        
        finalans=[]
        def per(arr,res):
            if not arr:
                finalans.append(res) 
            for i in range(0,len(arr)):
                new_arr=arr[:]
                ans=res[:]
                ans.append(new_arr.pop(i))
                per(new_arr,ans)
                    
        per(nums,[])
        return finalans