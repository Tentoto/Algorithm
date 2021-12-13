def dfs(graph,v,visit):
    visit[v]=1
    global answer
    answer+=1
    for x in graph[v]:
        if not visit[x]:
            dfs(graph,x,visit)
    return answer

    
n=int(input())
graph=[[] for _ in range(n+1)]
for _ in range(int(input())):
    x,y=map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
visit=[0]*(n+1)
answer=-1
print(dfs(graph,1,visit))