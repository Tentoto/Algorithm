'''
URL : https://www.acmicpc.net/problem/2805
문제 이름 : 나무 자르기
문제 내용 : 주어진 높이의 나무를 톱으로 잘랐을 때
           목표하는 양의 나무를 얻을 수 있는 톱의 위치를 반환하는 문제
'''
import sys
_,n=map(int, sys.stdin.readline().split())
woods=list(map(int, sys.stdin.readline().split()))
left=0
right=max(woods)
pos=0

while pos!=(right+left)//2:
    pos=(right+left)//2
    answer=0
    for i in woods:
        if i>pos:
            answer+=i-pos
        if answer>=n:
            left=pos
            break
    if answer<n:
        right=pos

print(pos)
    