'''
문제 이름 : 카탄의 개척자
문제 내용 : 1~5로 표현되는 육각형 타일을 인접한 타일과 겹치는 수 없이 배열할 때 주어진 숫자에 해당하는 순서의 타일 번호를 출력하는 문제
'''
tiles=[[1,]]
counter={1:1,2:0,3:0,4:0,5:0}

def make_tiles(tiles,i,counter):
    line=[]
    vertex=set([n+(n+1)*i for n in range(6)])
    
    for n in range((i+1)*6):
        v=n//(i+1)
        if n==0:
            avoid=set([tiles[i][-1],tiles[i][0]])
        elif n in vertex:
            avoid=set([line[-1],tiles[i][(v+1)*i-1]]) if n<(i+1)*6-1 else set([line[-1],line[0],tiles[i][(v+1)*i-1]])
        else:
            e=i-n%(i+1)
            avoid=set([line[-1],tiles[i][(v+1)*i-1-e],tiles[i][(v+1)*i-e]])
        for j in sorted(counter.keys(),key=lambda x:(counter[x],x)):
            if j not in avoid:
                line.append(j)
                counter[j]+=1
                break
    return line

for i in range(58):
    tiles+=[make_tiles(tiles,i,counter)]

flat_tiles=[]
for line in tiles:
    flat_tiles+=line

for _ in range(int(input())):
    k=int(input())
    print(flat_tiles[k-1])