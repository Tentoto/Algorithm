'''
문제 이름 : RBY팡!
문제 내용 : R,B,Y로 이루어진 공들이 있다. 같은 색의 공이 4개 이상 연속적으로 놓여있으면 제거한다. 
           주어진 공의 배열에서 하나의 공을 제거했을 때 남게 되는 공의 최솟값을 반환하는 문제
'''
import sys
input=sys.stdin.readline

stack=[]
size=int(input())
answer=10000

def simulation(i):
    if len(set([stack[i+j] for j in [-1,0,1] if i+j in range(len(stack))]))==1:
        return len(stack)
    else:
        colors=list(set([stack[i+j] for j in [-1,1] if i+j in range(len(stack)) and stack[i]!=stack[i+j]]))
        balls=10000
        for color in colors:
            sim=stack[:i]+[color]+stack[i+1:]

            left=i
            right=i
            nleft=left
            nright=right
            while True:
                if left>1 and sim[left-1]==sim[left]:
                    nleft=left-1

                if right<len(sim)-1 and sim[right]==sim[right+1]:
                    nright=right+1

                if left==nleft and right==nright:
                    if right-left>2:
                        if left==0 or right==len(sim)-1:
                            sim=sim[:left]+sim[right+1:]
                            break
                        elif sim[left-1]!=sim[right+1]:
                            sim=sim[:left]+sim[right+1:]
                            break
                        else:
                            sim=sim[:left]+sim[right+1:]
                            right=left
                            left-=1
                            nleft=left
                            nright=right
                    else:
                        break
                else:
                    left=nleft
                    right=nright

            balls=min(balls,len(sim))
        return balls

for _ in range(size):
    stack.append(int(input()))

for i in range(size):
    answer=min(simulation(i),answer)
            
print(answer)