'''
문제 이름 : 거스름돈
문제 내용 : 1000엔 지폐 하나를 사용하여 물건을 구매할 때 거스름돈의 수를 구하는 문제
'''
change =1000-int(input())
cash=[500,100,50,10,5]

def count_change(change):
    counter = 0
    for c in cash:
        counter += change // c
        change %= c
    return counter+change

print(count_change(change))
    