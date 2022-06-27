'''
URL : https://www.acmicpc.net/problem/7562
문제 이름 : 나이트의 이동 
문제 내용 :
'''
from collections import deque

def knight(n,pos_i,pos_f):
    visit=set()
    queue=deque()
    queue.append(pos_i)
    visit.add(pos_i)
    answer=0
    while queue:
        for _ in range(len(queue)):
            x,y=queue.popleft()
            if (x,y)==pos_f:
                return answer
            for dx,dy in [(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]:
                nx,ny=x+dx,y+dy
                if 0<=nx<n and 0<=ny<n and (nx,ny) not in visit:
                    queue.append((nx,ny))
                    visit.add((nx,ny))
        answer+=1

for _ in range(int(input())):
    n=int(input())
    pos_i=tuple(map(int,input().split()))
    pos_f=tuple(map(int,input().split()))
    print(knight(n,pos_i,pos_f))