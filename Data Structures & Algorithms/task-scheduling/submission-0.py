class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasks_freq=defaultdict(int)
        for t in tasks:
            tasks_freq[t]+=1
        priority=[]
        for task,freq in tasks_freq.items():
            heapq.heappush(priority,(-freq,task))
        count=0
        task_schedule=deque()
        while priority or task_schedule:
            if priority:
                f,t=heapq.heappop(priority)
                if -f-1>0:
                    task_schedule.append((-f-1,count+n,t))
            count+=1
            if task_schedule and task_schedule[0][1]<count:
                f,time,t=task_schedule.popleft()
                heapq.heappush(priority,(-f,t))
        return count
            
            