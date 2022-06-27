'''
URL : https://www.acmicpc.net/problem/4179
문제 이름 : 불!
문제 내용 : 주어진 지도 상에서 불이 났다. 지훈이가 탈출할 수 있다면 탈출에 걸리는 시간을 없다면 IMPOSSIBLE을 출력하는 문제.
'''
from collections import deque
n,m=map(int,input().split())
maps=[]
fire_queue=deque()
moves=[1,1,-1,-1]
step=0
burnt={}

for i in range(n):
    line=list(input())
    maps.append(line)
    for j in range(m):
        if line[j]=='J':
            start=(i,j)
            jihoon=deque([start])
            path={start:1}
        elif line[j]=='F':
            fire=(i,j)
            burnt[fire]=1
            fire_queue.append(fire)
        
def burn(queue):
    for _ in range(len(queue)):
        pos_r,pos_c=queue.popleft()
        for i in range(4):
            if i%2==0:
                npos_r=pos_r+moves[i]
                npos_c=pos_c
            else:
                npos_r=pos_r
                npos_c=pos_c+moves[i]
            if 0<=npos_r<n and 0<=npos_c<m:
                if (npos_r,npos_c) not in burnt and maps[npos_r][npos_c] in ['.','J']:
                    burnt[(npos_r,npos_c)]=1
                    queue.append((npos_r,npos_c))

def escaping(queue):
    for _ in range(len(queue)):
        pos_r,pos_c=queue.popleft()
        for i in range(4):
            if i%2==0:
                npos_r=pos_r+moves[i]
                npos_c=pos_c
            else:
                npos_r=pos_r
                npos_c=pos_c+moves[i]
            if npos_r<0 or n<=npos_r or npos_c<0 or m<=npos_c:
                return 1
            elif (npos_r,npos_c) not in burnt and (npos_r,npos_c) not in path and maps[npos_r][npos_c]=='.':
                path[(npos_r,npos_c)]=1
                queue.append((npos_r,npos_c))
    return 0

while jihoon:
    step+=1
    burn(fire_queue)
    flag=escaping(jihoon)
    if flag:
        print(step)
        break
        
if not flag:
    print('IMPOSSIBLE')