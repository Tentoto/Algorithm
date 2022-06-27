"""
URL : https://www.acmicpc.net/problem/13413
제목 : 오셀로 재배치
내용 : B와 W로 나타내지는 오셀로 말의 초기 상태를 목표 상태로 바꾸기 위한 최소 행동 수를 구하라.
       행동은 두 개의 말의 위치를 바꾸는 것, 한 개의 말의 색상을 바꾸는 것이다.
입력 : 첫 줄은 테스트 케이스 개수 T, 다음 오셀로 말의 개수 N과 초기 상태, 목표 상태가 각 줄에 T번 주어진다.
출력 : 최소 행동 수를 각 테스트 케이스마다 출력한다.
"""


def change_othello(initial, final):
    diff = 0
    diff_color = 0
    for i, f in zip(initial, final):
        if i != f:
            diff += 1
            diff_color += [1, -1][i == "W"]

    switch_color = abs(diff_color)
    switch_pos = (diff - switch_color) // 2

    return switch_color + switch_pos


if __name__ == "__main__":
    for test_case in range(int(input())):
        N = input()
        initial = input()
        final = input()
        print(change_othello(initial, final))
