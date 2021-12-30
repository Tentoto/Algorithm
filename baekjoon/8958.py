'''
문제 이름 : OX문제
문제 내용 : O,X로 이루어진 문자열이 주어졌을 때 연속된 O에 부가 점수가 더해진다.
           총점을 출력하는 문제
'''
for _ in range(int(input())):
    s = input()
    total = 0
    score = 1
    for i in range(len(s)):
        if s[i] == 'O':
            total+=score
            score+=1
        else:
            score=1
    print(total)