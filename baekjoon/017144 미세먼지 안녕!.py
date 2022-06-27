'''
URL : https://www.acmicpc.net/problem/17144
문제 이름 : 미세먼지 안녕!
문제 내용 :
'''
from collections import defaultdict
#from pprint import pprint
import time

rooms=[]
room_items=defaultdict(list)
diffusion=defaultdict(int)
directions=((-1,0),(0,1),(1,0),(0,-1))
cleaners=[]

class Dust:
    def __init__(self,row,col,state):
        self.row=row
        self.col=col
        self.state=state

    def diffuse(self):
        diff_amount=self.state//5
        if not diff_amount:
            return
        for i,j in [(0,1),(0,-1),(1,0),(-1,0)]:
            if 0<=self.row+i<R and 0<=self.col+j<C:
                if isinstance(rooms[self.row+i][self.col+j],Cleaner):
                    continue
                diffusion[(self.row+i,self.col+j)]+=diff_amount
                self.state-=diff_amount

    def clean_up(self,row,direction):
        r,c=directions[direction]
        nr=self.row+r
        nc=self.col+c
        if nr<0 or nr>row or nc<0 or nc==C:
            direction+=1
            r,c=directions[direction]
            nr=self.row+r
            nc=self.col+c
        self.state=rooms[nr][nc].state
        if nr==row and nc==0:
            return
        rooms[nr][nc].clean_up(row,direction)

    def clean_down(self,row,direction):
        r,c=directions[direction]
        nr=self.row-r
        nc=self.col+c
        if nr==R or nr<row or nc<0 or nc==C:
            direction+=1
            r,c=directions[direction]
            nr=self.row-r
            nc=self.col+c
        self.state=rooms[nr][nc].state
        if nr==row and nc==0:
            return
        rooms[nr][nc].clean_down(row,direction)


class Cleaner:
    def __init__(self,row):
        self.row=row
        self.clock=not isinstance(rooms[row-1][0],Cleaner)
        self.state=0
        cleaners.append(row)

    def clean(self):
        if self.clock:
            rooms[self.row-1][0].clean_up(self.row,0)
        else:
            rooms[self.row+1][0].clean_down(self.row,0)
            

    def diffuse(self):
        return

'''def states(rooms):
    states_list=[]
    for row in rooms:
        states_list.append([col.state if isinstance(col,Dust) else -1 for col in row])
    return states_list'''
                
s=time.time()
R,C,T=map(int,input().split())
for row in range(R):
    rooms.append([Dust(row,c,int(state)) if state!="-1" else Cleaner(row) for c,state in enumerate(input().split())])

for _ in range(T):
    for r in range(R):
        for c in range(C):
            rooms[r][c].diffuse()
    for x,y in diffusion:
        rooms[x][y].state+=diffusion[(x,y)]
    diffusion=defaultdict(int)
    #print(cleaners)
    for cleaner in cleaners:
        rooms[cleaner][0].clean()
    #print(_)
    #pprint(states(rooms))

print(sum(map(lambda x: sum([y.state for y in x]),rooms)))
print((time.time()-s))
    

