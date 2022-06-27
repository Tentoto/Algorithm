"""
URL : https://www.acmicpc.net/problem/1655
제목 : 가운데를 말해요
내용 : 백준이가 정수를 외칠 때마다 동생은 백준이 외친 수들 중 중간 값을 말해야한다. 만약 짝수 개를 외쳤다면 중간의 두 수 중 작은 수를 말해야 한다.
입력 : 첫 줄에 백준이 외치는 정수의 개수 N이 주어진다. 그 다음 N줄에 걸쳐서 백준이 외치는 정수가 주어진다.
출력 : 한 줄에 하나씩 N줄에 걸쳐 백준이의 동생이 말해야 하는 수를 출력한다.
"""
import sys
import heapq

# 그냥 input을 사용하면 시간초과가 난다;;
input = sys.stdin.readline


def get_median():
    N = int(input())

    # 두 개의 힙을 사용해서 max_heap <= median < min_heap 구조가 유지되게 하면 풀 수 있다.
    min_heap = []
    max_heap = []

    for _ in range(N):
        number = int(input())

        if not max_heap:
            heapq.heappush(max_heap, -number)
        elif number >= -max_heap[0]:
            heapq.heappush(min_heap, number)
        elif number < -max_heap[0]:
            heapq.heappush(max_heap, -number)

        if len(max_heap) > len(min_heap) + 1:
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
        elif len(min_heap) > len(max_heap):
            heapq.heappush(max_heap, -heapq.heappop(min_heap))

        print(-max_heap[0])


if __name__ == "__main__":
    get_median()
