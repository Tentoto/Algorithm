'''
문제 이름 : 앵무새
문제 내용 : 주어진 문장들과 단어 모음이 있을 때 문장을 작성가능한지 여부를 판단하는 프로그램을 작성하시오.
'''
from collections import deque

def solution():
    sent_dict={}

    for _ in range(int(input())):
        sentence=deque(input().split())
        first=sentence.popleft()
        sent_dict[first]=sentence

    word_list=deque(input().split())

    for _ in range(len(word_list)):
        word=word_list.popleft()
        try:
            sentence=sent_dict[word]
            del sent_dict[word]
            if sentence:
                first=sentence.popleft()
                sent_dict[first]=sentence
        except:
            print('Impossible')
            return
    if sent_dict:
        print('Impossible')
    else:
        print('Possible')

solution()