'''
문제 이름 : 선물
문제 내용 : 주어진 큰 박스(l,w,h)에 n개를 넣을 수 있는 정육면체 모양 선물상자의 변의 최대길이를 반환하는 문제
'''
import sys
n,l,w,h=map(int, sys.stdin.readline().split())
left=0
right=min(l,w,h)+1
pos=0

while abs(pos-(right+left)/2)>1e-9:
    pos=(right+left)/2
    answer=0
    if (l//pos)*(w//pos)*(h//pos)>=n:
        left=pos
    else:
        right=pos

print(pos)
    