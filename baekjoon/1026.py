'''
문제 이름 : 보물
문제 내용 : 주어진 정수 배열을 최소가 되게 만들어 출력하는 문제
'''
n=int(input())
A=sorted(list(map(int,input().split())))
B=sorted(list(map(int,input().split())),key=lambda x : -x)
print(sum(A[i]*B[i] for i in range(n)))