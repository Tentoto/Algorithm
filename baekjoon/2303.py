'''
문제 이름 : 숫자게임
문제 내용 : 플레이어들에게 주어진 수들에서 3개의 수를 골라 가장 큰 일의 자리를 만든 플레이어 번호를 출력
'''
from itertools import combinations
answer=[0,0]
players=[list(map(int,input().split())) for _ in range(int(input()))]
for player_num in range(len(players)):
    for comb in combinations(players[player_num],3):
        if answer[0]<=sum(comb)%10:
            answer=[sum(comb)%10,player_num+1]

print(answer[1])