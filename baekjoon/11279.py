'''
문제 이름 : 최대 힙
문제 내용 : 
'''
import heapq
import sys
input=sys.stdin.readline
heap=[]
for _ in range(int(input())):
    n=int(input())
    if n==0:
        try:
            print(-heapq.heappop(heap))
        except:
            print(0)
    else:
        heapq.heappush(heap,-n)