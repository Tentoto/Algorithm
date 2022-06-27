'''
URL : https://www.acmicpc.net/problem/2579
문제 이름 : 계단 오르기
문제 내용 : 
'''
n=int(input())
dp=[[0,0,0] for _ in range(n+1)]
stairs=[int(input()) for _ in range(n)]

def d(n):
    if n<=0:
        return [0,0,0]
    if sum(dp[n])!=0:
        return dp[n]
    dp[n]=[max(d(n-1)[1:]),d(n-1)[0]+stairs[n-1],d(n-1)[1]+stairs[n-1]]
    return dp[n]

print(max(d(n)[1],d(n)[2]))
