'''
URL : https://www.acmicpc.net/problem/1541
문제 이름 : 잃어버린 괄호
문제 내용 : 주어진 수식에 적절히 괄호를 넣어 최소를 만드는 문제
'''
expression = input().split('-')
answer=0
open=False

for i in range(len(expression)):
    answer+=(-1)**open*sum(map(int,expression[i].split('+')))
    open=True

print(answer)