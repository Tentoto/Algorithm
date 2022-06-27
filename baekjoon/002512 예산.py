'''
URL : https://www.acmicpc.net/problem/2512
문제 이름 : 예산
문제 내용 : 주어진 소요 예산들에 상한을 두어 총 예산 내에서 최대한의 예산을 사용하게 할 때 배정된 예산 중 최댓값을 반환하는 문제
'''
import sys
sys.stdin.readline()
budgets=list(map(int, sys.stdin.readline().split()))
total=int(sys.stdin.readline())

left=0
right=max(budgets)+1
pos=0

while pos!=(right+left)//2:
    pos=(right+left)//2
    answer=0
    for i in budgets:
        if i>=pos:
            answer+=pos
        else:
            answer+=i
        if answer>total:
            right=pos
            break
    if answer<=total:
        left=pos

print(pos)