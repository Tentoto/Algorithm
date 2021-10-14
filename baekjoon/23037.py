'''
문제 이름 : 5의 수난
문제 내용 : 주어진 숫자의 각 자릿수를 다섯 제곱한 수를 합한 결과를 출력하는 문제
'''
answer=0
for i in input():
    answer+=int(i)**5
print(answer)