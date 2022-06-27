'''
URL : https://www.acmicpc.net/problem/1463
문제 이름 : 1로 만들기
문제 내용 :
'''
'''import sys
sys.setrecursionlimit(1000000)

def make_one(n):
    if n<2:
        return 0
    return min(n%3+make_one(n//3),n%2+make_one(n//2))+1

print(make_one(int(input())))'''

dp=[0]*1000001
n=int(input())
for i in range(1,n+1):
    if 3*i<=1000000:
        dp[3*i]=min(dp[i]+1,dp[3*i] if dp[3*i]!=0 else 1000000)
    if 2*i<=1000000:
        dp[2*i]=min(dp[i]+1,dp[2*i] if dp[2*i]!=0 else 1000000)
    if i+1<=1000000:
        dp[i+1]=min(dp[i]+1,dp[i+1] if dp[i+1]!=0 else 1000000)
print(dp[n])
