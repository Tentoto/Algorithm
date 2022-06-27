"""
URL : https://www.acmicpc.net/problem/2293
제목 : 동전 1
내용 : 가치가 각각 다른 n개의 동전을 이용해서 k원을 만드는 경우의 수를 구하는 문제.
입력 : 첫째 줄에 n, k가 주어진다. (1 ≤ n ≤ 100, 1 ≤ k ≤ 10,000), 다음 n개의 줄에 동전의 가치가 주어진다. 
출력 : 첫째 줄에 경우의 수를 출력한다. 경우의 수는 2^31보다 작다.
"""
import sys


def get_number_of_ways(n, k, coins):
    number_of_ways = [0 for _ in range(k + 1)]
    number_of_ways[0] = 1
    # 1. i번째 안 더하는 경우, i-1번째에 k원일 경우의 수
    # 2. i번째 더하는 경우 i-1번째에 k-coins[i]원일 경우의 수를 더하면 된다.
    for i in range(1, n + 1):
        for value in range(k + 1):
            if value >= coins[i]:
                number_of_ways[value] += number_of_ways[value - coins[i]]

    return number_of_ways[k]


if __name__ == "__main__":
    n, k = map(int, input().split())
    coins = [0] + list(map(int, sys.stdin.readlines()))

    print(get_number_of_ways(n, k, coins))
