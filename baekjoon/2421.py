'''
문제 이름 : 저금통
문제 내용 : 두 개의 저금통이 있다. 두 저금통 중 하나에 매일 동전 하나씩 넣어 각각 n개에 다다르게 할 때,
           두 저금통의 숫자를 이어붙인 수가 소수가 되는 최대의 경우의 수를 출력하는 문제
'''
prime={}
for i in range(2,1000000):
    prime[i]=1
    
for i in prime:
    for j in range(2,999999//i+1):
        prime[i*j]=0

dp=[[0 for _ in range(1000)] for _ in range(1000)]
n=int(input())

for i in range(1,n+1):
    for j in range(1,n+1):
        dp[i][j]=max(dp[i-1][j],dp[i][j-1])+prime[int(str(i)+str(j))]

print(dp[n][n]-1)