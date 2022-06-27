"""
URL : https://www.acmicpc.net/problem/2075
제목 : N번째 큰 수
내용 : NXN 크기의 아래의 숫자가 위의 숫자보다 큰 규칙을 가진 표에 채워진 수가 있을 때 N번째 큰 수를 구하라.
입력 : 첫 줄에 N과 다음 N줄에 숫자들이 공백으로 구분되어 주어진다.
출력 : N번째 큰 수를 출력한다.
"""
import heapq


def N_greatest(N):
    heap = []
    for _ in range(N):
        for num in input().split():
            heapq.heappush(heap, int(num))
            if len(heap) > N:
                heapq.heappop(heap)

    Nth_num = heap[0]

    return Nth_num


if __name__ == "__main__":
    print(N_greatest(int(input())))
