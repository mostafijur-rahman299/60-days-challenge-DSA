from collections import defaultdict, deque
from typing import List

class Solution:
    def canFinish(self,numCourses:int,prerequisites:List[List[int]])->bool:
        graph=defaultdict(list)
        for course,prereq in prerequisites:
            graph[prereq].append(course)


        indegrees=[0]*numCourses
        for prereq,_ in prerequisites:
            indegrees[prereq]+=1


        queue=deque()
        for courses in range(numCourses):
            if indegrees[courses]==0:
                queue.append(courses)

        while queue:
            courses=queue.popleft()
            for prereq in graph[courses]:
                indegrees[prereq]-=1
                if indegrees[prereq]==0:
                    queue.append(prereq)


        return all(indegree==0 for indegree in indegrees)                                      
    