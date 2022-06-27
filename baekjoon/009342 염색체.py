'''
URL : https://www.acmicpc.net/problem/9342
문제 이름 : 염색체
문제 내용 : 다음의 규칙을 따르면 Infected! 아니면 Good을 출력하는 문제.
    문자열은 {A, B, C, D, E, F} 중 0개 또는 1개로 시작해야 한다.
    그 다음에는 A가 하나 또는 그 이상 있어야 한다.
    그 다음에는 F가 하나 또는 그 이상 있어야 한다.
    그 다음에는 C가 하나 또는 그 이상 있어야 한다.
    그 다음에는 {A, B, C, D, E, F} 중 0개 또는 1개가 있으며, 더 이상의 문자는 없어야 한다.

'''
import re
for _ in range(int(input())):
    print('Infected!' if re.match('^([A-F]?)A+F+C+([A-F]?)$',input()) else 'Good')