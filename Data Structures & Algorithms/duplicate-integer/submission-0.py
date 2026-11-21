class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dist_nums=set()
        for num in nums:
            if num in  dist_nums:
                return True
            dist_nums.add(num)
        return False