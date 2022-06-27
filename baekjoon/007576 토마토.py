'''
URL : https://www.acmicpc.net/problem/7576
문제 이름 : 토마토
문제 내용 : 인접한 토마토가 익을 때 모든 토마토가 익기까지 걸리는 최소 시간을 구하라
'''
from collections import deque
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
tomato=[]
green={}
answer=-1
queue=deque()

for i in range(m):
    tomato.append([])
    row=input().split()
    for j in range(n):
        tomato[i].append(row[j])
        if row[j]=='1':
            queue.append((i,j))
        elif row[j]=='0':
            green[(i,j)]=1

while queue:
    answer+=1
    for _ in range(len(queue)):
        x,y=queue.popleft()
        for dx,dy in (-1,0),(1,0),(0,-1),(0,1):
            nx,ny=x+dx,y+dy
            if 0<=nx<m and 0<=ny<n:
                if tomato[nx][ny]=='0':
                    tomato[nx][ny]='1'
                    del green[(nx,ny)]
                    queue.append((nx,ny))

if green:
    print(-1)
else:
    print(answer)
