
'''
문제 이름 : 숫자놀이
문제 내용 : 주어진 수 n에 대해 각 자릿수의 곱이 n이 되는 최소의 정수의 자릿수를 찾는 문제
'''
def factorize(n):
    if n==1:
        return 1
    else:
        for i in range(9,1,-1):
            if n%i==0:
                a=factorize(n//i)
                if n//i==1:
                    return 1
                elif a>0:
                    return factorize(n//i)+1
                else:
                    return -1
        else:
            return -1

for _ in range(int(input())):
    print(factorize(int(input())))