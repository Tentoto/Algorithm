'''
URL : https://www.acmicpc.net/problem/1927
문제 이름 : 최소 힙
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
            print(heapq.heappop(heap))
        except:
            print(0)
    else:
        heapq.heappush(heap,n)