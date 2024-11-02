from collections import defaultdict
from collections import deque
graph=defaultdict(list)
v,e=map(int,input().split())
for i in range(e):
    u,v = map(str,input().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs(graph,start,visited,path):
    queue=deque()
    path.append(start)
    queue.append(start)
    visited[start]=True
    while len(queue)!=0:
        tmpnode=queue.popleft()
        for i in graph[tmpnode]:
            if visited[i]==False:
                path.append(i)
                queue.append(i)
                visited[i]=True
    return path

path=[]
start='A'
visited= defaultdict(bool)
traversedpath=bfs(graph,start,visited,path)
print(traversedpath)

'''
5 5
A B
A D
A C
C E
C D
'''
