'''
URL : https://www.acmicpc.net/problem/11053
문제 이름 : 가장 긴 증가하는 부분 수열
문제 내용 : 주어진 수열에서 가장 긴 증가하는 부분 수열을 반환하는 문제.
'''
dp=[1]*int(input())
seq=list(map(int,input().split()))
for x in range(1,len(dp)):     #부분 수열의 우측 끝 index x
    for y in range(x):         #index y로 끝나는 작은 부분 수열
        if seq[x]>seq[y]:      #작은 부분 수열의 끝보다 x번째 원소의 값이 크면
            if dp[x]<dp[y]+1:  #작은 부분 수열의 길이에 1을 더한 값이
                dp[x]=dp[y]+1  #기존 값보다 크면 갱신
print(max(dp))