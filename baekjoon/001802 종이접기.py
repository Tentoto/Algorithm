'''
URL : https://www.acmicpc.net/problem/1802
문제 이름 : 종이접기
문제 내용 : 접어진 방향이 주어졌을때 규칙에 따라 접을 수 있는지 판단하는 문제
            현재 상태의 중심을 기준으로 반을 접되
            규칙 1: 반시계 방향, 규칙 2: 시계 방향
'''
import sys
sys.setrecursionlimit(10**6)

def invert(folds):
    return ''.join(['0' if i=='1' else '1' for i in folds[::-1]])

def solution(paper):
    if len(paper)==1:
        return True
    if invert(paper[:len(paper)//2])==paper[len(paper)//2+1:]:
        return solution(paper[:len(paper)//2])*solution(paper[len(paper)//2+1:])
    else:
        return False

for i in range(int(input())):
    paper=input()
    if len(paper)%2==0:
        print('NO')
        continue
    if solution(paper):
        print('YES')
    else:
        print('NO')

