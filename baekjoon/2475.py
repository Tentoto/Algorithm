'''
문제 이름 : 검증수
문제 내용 : 고유번호 각 자릿수 제곱합을 10으로 나눈 나머지를 반환하는 문제
'''
print(sum([i**2 for i in map(int,input().split())])%10)
