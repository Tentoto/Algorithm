'''
문제 이름 : 벽 부수고 이동하기
문제 내용 :
'''
from collections import deque
n,m = map(int,input().split())
maps = [input() for _ in range(n)]
queue = deque()
answer = 0
queue.append((0,0,True))
visit=[[(False,True)]*(m+1) for _ in range(n+1)]
visit[0][0]=(True,True)

if n==1 and m==1:
    print(1)
    exit()

while queue:
    answer+=1
    for _ in range(len(queue)):
        x,y,breakable = queue.popleft()
        for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            nx,ny = x+dx,y+dy
            if nx==n-1 and ny==m-1:
                print(answer+1)
                exit()
            elif 0<=nx<n and 0<=ny<m:
                if maps[nx][ny]=='0':
                    if not visit[nx][ny][0] or (visit[nx][ny][1]==False and breakable):
                        visit[nx][ny]=(True,breakable)
                        queue.append((nx,ny,breakable))
                elif not visit[nx][ny][0] and breakable:
                    visit[nx][ny]=(True,False)
                    queue.append((nx,ny,False))

print(-1)


