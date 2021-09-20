'''
문제 이름 : 팔
문제 내용 : 주어진 두 수 사이에서 8을 최소로 자릿수로 가지는 숫자의 8의 갯수.
'''
def solution():
    answer=0
    numbers=input().split() #공백으로 구분된 두 숫자 입력.
    if len(numbers[0])!=len(numbers[1]): #두 숫자의 자릿수가 다르면 무조건 8을 자릿수로 가지지 않는 수가 있으니 0을 반환
        return answer
    for i,j in zip(*numbers): #두 숫자의 자릿수를 추출하여 비교
        if i!=j: #다른 숫자가 나오면 정지
            break
        elif i=='8' and j=='8': #자릿수가 8이면 정답을 1만큼 증가시킨다. i=='8' 하나만 써도 충분.
            answer+=1
        else: #자릿수가 같으나 8이 아닐 때는 계속 진행
            continue 
    return answer

print(solution())