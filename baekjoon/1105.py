'''
문제 이름 : 팔
문제 내용 : 주어진 두 수 사이에서 8을 최소로 자릿수로 가지는 숫자의 8의 갯수.
'''
def solution():
    answer=0
    numbers=input().split()
    if len(numbers[0])!=len(numbers[1]):
        return answer
    for i,j in zip(*numbers):
        if i!=j:
            break
        elif i=='8' and j=='8':
            answer+=1
        else:
            continue
    return answer

print(solution())