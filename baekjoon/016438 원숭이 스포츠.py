'''
URL : https://www.acmicpc.net/problem/16438
문제 이름 : 원숭이 스포츠
문제 내용 :
'''
from collections import deque

n=int(input())
team_list=deque()
team_list.append('A'*n)

def invert(team):
    return ''.join(['A' if i=='B' else 'B' for i in team])

def divide_team(team):
    team_list.append(team[:len(team)//2])
    team_list.append(invert(team[len(team)//2:]))
    return

for i in range(7):
    for _ in range(len(team_list)):
        team=team_list.popleft()
        if len(team)>1:
            divide_team(team)
        else:
            team_list.append(team)
    print(''.join(team_list))