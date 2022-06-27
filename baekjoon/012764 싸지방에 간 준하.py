'''
URL : https://www.acmicpc.net/problem/12764
문제 이름 : 싸지방에 간 준하
문제 내용 : 싸지방을 이용하고자 하는 사람들의 사용 시작 시간과 종료 시간이 주어질 때,
            컴퓨터를 대기 없이 사용하기 위한 최소 대수와 자리 별로 이용한 인원수를 출력하는 문제
'''
import heapq

computers=0
seats=[]
uses=[]
counts=[]
users=[]

for _ in range(int(input())):
    #시작 시간이 빠른 순으로 이용자 정렬
    start, end = map(int, input().split())
    heapq.heappush(users,(start,end))

while users:
    start,end=heapq.heappop(users)
    while uses:
        # 이용 종료한 사람이 있으면 자리 반환
        if start>=uses[0][0]:
            seat=heapq.heappop(uses)[1]
            heapq.heappush(seats,seat)
            #print(f'{seat}번 자리를 반납했습니다.')
        else:
            break
    try:
        #가용한 자리가 있으면 사용
        seat=heapq.heappop(seats)
        counts[seat]+=1
        #print(f'{seat}번 자리를 {counts[seat]}번째 이용합니다.')
    except:
        #가용한 자리가 없으면 컴퓨터 구매
        seat=computers
        counts.append(1)
        computers+=1
        #print(f'{seat}번 컴퓨터를 구매합니다.')
    heapq.heappush(uses, (end,seat))

print(computers)
print(*counts)

'''
input
5
20 50
10 100
30 120
60 110
80 90

output
4
1 2 1 1
'''
    
        

