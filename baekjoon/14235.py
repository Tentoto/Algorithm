'''
문제 이름 : 크리스마스 선물
문제 내용 : 주어진 아이들과 거점지 방문 정보를 통해 아이들에게 준 선물의 가치를 출력하는 문제
'''
import heapq
gifts=[]
for _ in range(int(input())):
    visit=list(map(int,input().split()))
    if len(visit)==1:
        try:
            print(-heapq.heappop(gifts))
        except:
            print(-1)
    else:
        for i in visit[1:]:
            heapq.heappush(gifts,-i)

'''
input
5
0
3 3 3 2
0
0
0

output
-1
3
2
-1
'''
