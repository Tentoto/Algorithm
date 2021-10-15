'''
문제 이름 : 최고의 팀 만들기
문제 내용 : 선수들의 백팀 능력치, 흑팀 능력치 쌍이 주어진다. 백팀, 흑팀을 각각 15명씩 뽑을 때 최대 능력치를 반환하는 문제.
'''
import sys
players=[]
answer=0
for idx,line in enumerate(sys.stdin.readlines()):
    try:
        white,black=map(int,line.split())
        players.append((white,black))
    except:
        pass
dp=[[[0 for _ in range(16)] for _ in range(16)] for i in range(len(players)+1)]
for n in range(1,len(players)+1):
    for w in range(min(n+1,16)):
        for b in range(min(n-w+1,16)):
            if n==1:
                dp[1][1][0]=players[n-1][0]
                dp[1][0][1]=players[n-1][1]
            elif w==0 and b==0:
                dp[n][0][0]=0
            elif w==0:
                dp[n][w][b]=max(max([dp[n-i][w][b-1] for i in range(1,n+1)])+players[n-1][1],dp[n-1][w][b])
            elif b==0:
                dp[n][w][b]=max(max([dp[n-i][w-1][b] for i in range(1,n+1)])+players[n-1][0],dp[n-1][w][b])
            else:
                dp[n][w][b]=max(max([dp[n-i][w-1][b] for i in range(1,n+1)])+players[n-1][0],max([dp[n-i][w][b-1] for i in range(1,n+1)])+players[n-1][1],dp[n-1][w][b])
print(max([dp[i][15][15] for i in range(len(players)+1)]))