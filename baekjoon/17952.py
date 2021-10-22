'''
문제 이름 : 과제는 끝나지 않아!
문제 내용 : 주어진 시간동안 최근에 주어지는 과제를 우선적으로 처리할 때 얻게 되는 점수를 반환하는 문제
'''
import sys
from collections import deque

input=sys.stdin.readline

def solve():
    stack=[]
    semester=int(input())
    total=0

    for _ in range(semester):
        try:
            _,score,time=map(int,input().split())
            stack.append([score,time])
        except:
            pass
        
        try:
            stack[-1][1]-=1
            if not stack[-1][1]:
                total+=stack.pop()[0]
        except:
            pass

    return total

print(solve())