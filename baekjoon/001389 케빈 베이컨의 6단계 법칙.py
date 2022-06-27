'''
URL : https://www.acmicpc.net/problem/1389
문제 이름 : 케빈 베이컨의 6단계 법칙
문제 내용 : 
'''

users, relations = map(int, input().split())
graph=[[] for _ in range(users+1)]
for _ in range(relations):
    a,b=map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dist=[[users]*(users+1) for _ in range(users+1)]
for i in range(1,users+1):
    for j in range(1,users+1):
        if i==j:
            dist[i][j]=0
        elif j in graph[i]:
            dist[i][j]=1

for k in range(1,users+1):
    for i in range(1,users+1):
        for j in range(1,users+1):
            dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j])
            dist[j][i]=min(dist[j][i],dist[i][k]+dist[k][j])

print(sorted(range(1,users+1),key=lambda x:sum(dist[x]))[0])