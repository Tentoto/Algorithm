"""
URL : https://www.acmicpc.net/problem/1005
제목 : ACM Craft
내용 : 건설 순서와 건설에 필요한 시간이 주어졌을 때, 건설을 완료하기 위한 최소 시간을 구하는 문제
입력 : 첫 줄에는 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 첫 줄에 건물의 개수 N, 건설 순서 규칙의 개수 K가 주어진다.
        둘째 줄에는 건물 당 건설에 걸리는 시간 D_i이 주어지고, 세번째에서 K+2줄까지 건설 순서가 주어진다. 
        마지막으로 최종 건설 목표 건물 번호 W가 주어진다.
출력 : 건물 W를 건설완료 하는데 드는 최소 시간을 출력한다.
제한 : 
    2 ≤ N ≤ 1000
    1 ≤ K ≤ 100,000
    1 ≤ X, Y, W ≤ N
    0 ≤ D_i ≤ 100,000, D_i는 정수
"""
import sys
from collections import deque


def get_min_construct_time():
    N, K = map(int, input().split())
    # Directed Acyclic Graph를 만들기 위해 초기화한다.
    DAG = [[] for _ in range(N)]
    order = [0 for _ in range(N)]
    
    # 시작 위치를 찾기 위한 set
    start = set(range(N))

    D = list(map(int, sys.stdin.readline().split()))
    construct_time = D.copy()

    # 주어진 건설 순서를 읽어서 DAG에 추가한다.
    for _ in range(K):
        prev, post = map(lambda x:int(x)-1, sys.stdin.readline().split())
        DAG[prev].append(post)
        order[post] += 1
        start.remove(post)

    W = int(sys.stdin.readline())-1

    # 위상정렬을 수행한다.
    queue = deque(list(start))
    while queue:
        cur = queue.popleft()
        for next_ in DAG[cur]:
            order[next_] -= 1
            construct_time[next_] = max(construct_time[next_], construct_time[cur]+D[next_])
            if order[next_] == 0:
                if next_ == W:
                    return construct_time[next_]
                queue.append(next_)
                
    return construct_time[W]


if __name__=="__main__":
    T = int(input())
    
    for _ in range(T):
        print(get_min_construct_time())