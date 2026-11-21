class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency=defaultdict(int)
        for num in nums:
            frequency[num]+=1
        bucket=[[] for _ in range(len(nums)+1)]
        for num,count in frequency.items():
            bucket[count].append(num)
        res=[]
        for i in range(len(bucket)-1,0,-1):
            for num in bucket[i]:
                res.append(num)
                if len(res)==k:
                    return res            
        