"""
URL : https://www.acmicpc.net/problem/12865
제목 : 평범한 배낭
내용 : 무게 W_i와 가치 V_i를 가지는 물건이 N개 있을 때, K의 무게 한도를 가지는 배낭에 넣을 수 있는 물건의 최대 가치를 구하는 문제
입력 : 첫 줄에 물품의 수 N(1 ≤ N ≤ 100)와 무게 한도 K(1 ≤ N ≤ 100,000), N개의 줄에 각 물건의 무게 W(1 ≤ W ≤ 100,000), 가치 V(1 ≤ V ≤ 1000)가 주어진다.
출력 : 한 줄에 배낭에 넣을 수 있는 물건들의 가치합의 최댓값을 출력한다.
"""
import sys


def get_max_value(N, K, W, V):
    # 물건을 새로 넣을 때 고려하게 되는 부분은 물건들과 가방의 무게 한도이다.
    bag = [[0 for _ in range(K + 1)] for _ in range(N)]

    # 사용할 무게 한도 k내에서 i번째 물건을 고려할 때, 두 가지 경우가 있다.
    # 1. i번째 물건을 넣지 않는 경우, i-1번째에서 무게 한도 k일 때의 가치
    # 2. i번째 물건을 넣는 경우, i-1번째에서 무게 한도 k-W[i]일 때의 가치+V[i] 중 큰 값이다.
    for i in range(N):
        for k in range(1, K + 1):
            if k - W[i] >= 0:
                bag[i][k] = max(bag[i - 1][k], bag[i - 1][k - W[i]] + V[i])
            else:
                bag[i][k] = bag[i - 1][k]

    return bag[N - 1][K]


if __name__ == "__main__":
    N, K = map(int, input().split())
    W, V = [], []

    for line in sys.stdin.readlines():
        w, v = map(int, line.split())
        W.append(w)
        V.append(v)

    print(get_max_value(N, K, W, V))
