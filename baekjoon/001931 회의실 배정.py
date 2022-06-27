'''
URL : https://www.acmicpc.net/problem/1931
문제 이름 : 회의실 배정
문제 내용 : 한 회의실에서 주어진 회의 계획들로 진행할 수 있는 최대 회의 수를 구하는 문제
'''
import heapq
answer = 0
time=0
seminars=[]
for _ in range(int(input())):
    n,m=map(int,input().split())
    heapq.heappush(seminars,(m,n))

while seminars:
    if seminars[0][1]>=time:
        end,start=heapq.heappop(seminars)
        time=end
        answer+=1
    else:
        heapq.heappop(seminars)

print(answer)