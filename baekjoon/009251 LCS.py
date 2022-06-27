"""
URL : https://www.acmicpc.net/problem/9251
제목 : LCS
내용 : 두 수열이 주어질 때 두 수열의 부분 수열이면서 그 중 가장 긴 것을 구하는 문제
입력 : 첫째 줄과 둘째 줄에 두 문자열이 주어진다. 문자열은 알파벳 대문자로만 이루어져 있고 최대 1000글자이다.
출력 : 첫째 줄에 입력으로 주어진 두 문자열의 길이를 출력한다.
"""


def LCS(a, b):
    n = len(a)
    m = len(b)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # 두 문자열을 돌면서 LCS의 길이를 구한다.
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # 문자가 같은 경우 이전의 결과에 1을 더하고
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            # 문자가 다른 경우 이전의 결과 중 큰 값을 가져간다.
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[n][m]


if __name__ == "__main__":
    a = input()
    b = input()
    print(LCS(a, b))
