from collections import defaultdict,deque
class Solution:
    def canFinish(self,numCourses:int,prerequisites)->bool:
        graph = {}
        indegrees = {}
        queue = []

        # make a graph from list
        for preq, course in prerequisites:
            if preq in graph:
                graph[preq].append(course)
            else:
                graph[preq] = [course]

        # Find indegree from adjancency list
        for edge in prerequisites:
            from_node, to_node = edge
            indegrees[from_node] = 0
            indegrees[to_node] = 0
            
        for edge in prerequisites:
            _, to_node = edge
            indegrees[to_node] += 1
            
        for key, value in indegrees.items():
            if value == 0:
                queue.append(key)
                
        while queue:
            node = queue.pop(0)
            
            if graph.get(node):
                for neighbor in graph[node]:
                    indegrees[neighbor] -= 1
                    if indegrees[neighbor] == 0:
                        queue.append(neighbor)


        return all(val==0 for key, val in indegrees.items())                                      