'''
URL : https://www.acmicpc.net/problem/16948
문제 이름 : 데스나이트
문제 내용 : 주어진 크기의 체스판 위에서 시작 좌표와 끝 좌표가 주어질 때 나이트가 끝 좌표에 도달하는 최소 이동 횟수를 반환
'''
from collections import deque

n=int(input())
ri,ci,rf,cf=map(int,input().split())
chess=[[0 for _ in range(n)] for _ in range(n)]
queue=deque([(ri,ci)])
chess[ri][ci]=1
mr=[0,0,2,2,-2,-2]
mc=[2,-2,1,-1,1,-1]
step=0
flag=0
while queue:
    step+=1
    for _ in range(len(queue)):
        rp,cp=queue.popleft()
        for i in range(6):
            rn=rp+mr[i]
            cn=cp+mc[i]
            if rn in range(n) and cn in range(n):
                if rn==rf and cn==cf:
                    flag=1
                    break
                elif not chess[rn][cn]:
                    queue.append((rn,cn))
                    chess[rn][cn]=1
            if flag:
                break
    if flag:
        break

print(step) if flag else print(-1)
    
