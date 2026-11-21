class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result=[0]*len(temperatures)
        stack=[]
        for i,num in enumerate(temperatures):
            while stack and temperatures[stack[-1]]<num:
                index=stack.pop()
                result[index]=i-index
            stack.append(i)
        return result