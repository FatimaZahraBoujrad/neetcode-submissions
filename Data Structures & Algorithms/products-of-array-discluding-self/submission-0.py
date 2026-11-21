from math import prod
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref_prod=[1]*len(nums)
        sufx_prod=[1]*len(nums)
        for i in range(1,len(nums)):
            pref_prod[i]= pref_prod[i-1]*nums[i-1]
        for i in range(len(nums)-2,-1,-1):
            sufx_prod[i]=sufx_prod[i+1]*nums[i+1]
        return [pref_prod[i]*sufx_prod[i] for i in range(len(nums))]