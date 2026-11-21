class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        pq=[]
        frequency=defaultdict(int)
        for num in nums:
            frequency[num]+=1
        for num,count in frequency.items():
            heapq.heappush(pq,(count,num))
            if len(pq)>k:
                heapq.heappop(pq)
        return [num for count,num in pq]