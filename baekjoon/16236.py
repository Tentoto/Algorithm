'''
문제 이름 : 아기상어
문제 내용 : 
'''
import heapq
from collections import deque

queue = deque()
area=[]
shark=2
total=0
time=0
eat=0
visit={}

for i in range(int(input())):
    area.append(list(map(int, input().split())))
    for j,sector in enumerate(area[-1]):
        if sector==9:
            area[i][j]=0
            queue.append((i,j))
            shark_pos=(i,j)

visit[(shark_pos[0],shark_pos[1])]=1

while queue:
    fish=[]
    time+=1
    for _ in range(len(queue)):
        x,y=queue.popleft()
        for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            nx,ny=x+dx,y+dy
            if 0<=nx<len(area) and 0<=ny<len(area[0]):
                if (nx,ny) not in visit:
                    if area[nx][ny]==shark or area[nx][ny]==0:
                        queue.append((nx,ny))
                        visit[(nx,ny)]=1
                    elif 0<area[nx][ny]<shark:
                        heapq.heappush(fish,(nx,ny))
    if fish:
        x,y=heapq.heappop(fish)
        area[x][y]=0
        total+=time
        time=0
        shark_pos=(x,y)
        eat+=1
        if eat==shark:
            shark+=1
            eat=0
        visit={(x,y):1}
        queue=deque([(x,y)])

print(total)