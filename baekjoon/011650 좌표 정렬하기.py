'''
URL : https://www.acmicpc.net/problem/11650
문제 이름 : 좌표 정렬하기
문제 내용 : 주어진 좌표들을 오름차순으로 정렬하는 문제
'''
import heapq
coordinates=[]
for _ in range(int(input())):
    x,y = map(int,input().split())
    heapq.heappush(coordinates,(x,y))

while coordinates:
    print(*heapq.heappop(coordinates))