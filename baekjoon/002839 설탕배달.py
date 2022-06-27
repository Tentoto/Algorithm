"""
URL : https://www.acmicpc.net/problem/2839
제목 : 설탕배달
내용 : 3킬로그램 설탕봉지와 5킬로그램 설탕봉지로 N킬로그램 설탕을 배달할 때 최소 봉지 개수를 구하는 문제
입력 : 첫째 줄에 N이 주어진다. (3 ≤ N ≤ 5000)
출력 : 배달하는 봉지의 최소 개수를 출력한다. 정확하게 N킬로그램을 만들 수 없다면 -1을 출력한다.
"""
minimum_bags = [0 for _ in range(5000)]
minimum_bags[3] = 1
minimum_bags[5] = 1

def get_minimum(N):
    if N<3:
        return -1

    if minimum_bags[N] == 0:
        prev_3 = get_minimum(N-3)+1                # 3킬로 봉지를 추가해서 무게를 맞춘 경우
        prev_5 = get_minimum(N-5)+1                # 5킬로 봉지를 추가해서 맞춘 경우
        if prev_3*prev_5:                          # 위의 두 값이 존재하는 경우
            minimum_bags[N] = min(prev_3, prev_5)
        else:                                      # 둘 중 하나 이상이 불가능한 경우
            minimum_bags[N] = prev_3+prev_5-(prev_3==prev_5)

    return minimum_bags[N]

# DP를 쓰기 싫다면 다음과 같이 풀 수도 있다.
def get_minimum(N):
    """
    5킬로 봉지가 많으면 많을 수록 봉지 수가 적어진다.
    이때 5킬로로 나누어 떨어지면 그 N을 5로 나눈 몫이 답이 되고,
    5로 나눈 나머지에 대해 
    3으로 나눈 나머지가 2일 경우 -2*5+4*3=2이고
    3으로 나눈 나머지가 1일 경우 -1*5+2*3=1이므로
    다음의 식을 세울 수 있다.
    """
    return -1 if N//5-(N%5)%3<0 else N//5+N%5//3+(N%5)%3

if __name__=="__main__":
    assert(get_minimum(18)==4)
    assert(get_minimum(4)==-1)
    assert(get_minimum(6)==2)
    assert(get_minimum(9)==3)
    assert(get_minimum(11)==3)
    N=int(input())
    print(get_minimum(N))
    