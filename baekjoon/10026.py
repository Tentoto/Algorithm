'''
문제 이름 : 적록색맹
문제 내용 : R,G,B로 이루어진 NXN 2차원 배열이 주어진다. 정상인 경우와 적록을 구분하지 못하는 경우에 인접한 동일한 색상을 같은 블럭이라고 봤을 때 각각의 블럭 갯수를 출력
'''
import sys
sys.setrecursionlimit(1000000)

n=int(input())
mat=[[i for i in input()] for _ in range(n)]
visit={}
visit_weak={}
normal=[]
weak=[]

def dfs(x,y,weak):
    if not weak:
        visit[(x,y)]=1
    visit_weak[(x,y)]=1
    mx=[1,0,-1,0]
    my=[0,1,0,-1]
    for i in range(4):
        nx=x+mx[i]
        ny=y+my[i]
        if nx in range(n) and ny in range(n):
            if (nx,ny) not in visit:
                if not weak and mat[x][y]==mat[nx][ny]:
                    dfs(nx,ny,weak)
                elif (nx,ny) not in visit_weak and mat[x][y] in ['R','G'] and mat[nx][ny] in ['R','G']:
                        dfs(nx,ny,1)

    return

for x in range(n):
    for y in range(n):
        if (x,y) not in visit:
            normal.append([])
            if (x,y) not in visit_weak:
                weak.append([])
            dfs(x,y,0)
            
print(len(normal),len(weak))