'''
문제 이름 : 미친 로봇
문제 내용 : 주어진 횟수만큼 로봇이 주어진 확률로 동서남북으로 이동할 때, simple인 경우의 확률을 구하는 문제.
'''
n,u,d,l,r=map(int,input().split())
probs={'U':u/100,'D':d/100,'L':l/100,'R':r/100}
visited={(0,0):0}
answer=0

def dfs(pos_x,pos_y,prob,depth,max_depth,simple,visited):
    global answer
    depth+=1
    nvisited=visited.copy()
    nvisited[(pos_x,pos_y)]=depth
    if depth == max_depth:
        if simple:
            answer+=prob
        return
    else:
        for direction in ['U','D','L','R']:
            if direction=='U':
                new_pos_x=pos_x
                new_pos_y=pos_y+1
            elif direction=='D':
                new_pos_x=pos_x
                new_pos_y=pos_y-1
            elif direction=='L':
                new_pos_x=pos_x-1
                new_pos_y=pos_y
            elif direction=='R':
                new_pos_x=pos_x+1
                new_pos_y=pos_y
            if (new_pos_x,new_pos_y) in visited:
                pass
            else:
                dfs(new_pos_x,new_pos_y,prob*probs[direction],depth,max_depth,simple,nvisited)

dfs(0,0,1,-1,n,True,visited)
print(answer)



