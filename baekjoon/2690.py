import re

to_lig={
    'ㄱ': '[AE]',
    'ㄴ': '[ae]', 
    'ㄷ': '[OE]', 
    'ㄹ': '[oe]', 
    'ㅁ': '[ct]', 
    'ㅂ': '[ff]', 
    'ㅅ': '[fi]', 
    'ㅇ': '[fl]', 
    'ㅈ': '[ffi]', 
    'ㅊ': '[ffl]', 
    'ㅋ': '[longs]', 
    'ㅌ': '[longsi]', 
    'ㅍ': '[longsh]', 
    'ㅎ': '[longsl]', 
    'ㄲ': '[longss]', 
    'ㄸ': '[longst]', 
    'ㅃ': '[longssi]'
    }
to_rep={
    'AE': 'ㄱ',
    'Ae': 'ㄱ',
    'aE': 'ㄴ',
    'ae': 'ㄴ', 
    'OE': 'ㄷ', 
    'Oe': 'ㄷ',
    'oe': 'ㄹ', 
    'oE': 'ㄹ',
    'ct': 'ㅁ', 
    'ff': 'ㅂ', 
    'fi': 'ㅅ', 
    'fl': 'ㅇ', 
    'ffi': 'ㅈ', 
    'ffl': 'ㅊ', 
    'ſ': 'ㅋ', 
    'ſi': 'ㅌ', 
    'ſh': 'ㅍ', 
    'ſl': 'ㅎ', 
    'ſſ': 'ㄲ', 
    'ſt': 'ㄸ', 
    'ſſi': 'ㅃ'
    }

for _ in range(int(input())):
    text=input()
    processed=[]
    text=re.sub('s','ſ',text)
    text=re.sub('ſſſ','ſsſ',text)
    for match in re.finditer('(ſ([fbk ]|[^a-zA-Z0-9ſ ]))|ſ$',text):
        text=text[:match.start()]+'s'+text[match.start()+1:]
    for key in sorted(to_rep.keys(),key=lambda x :-len(x)):
        while re.search(key,text):
            text=re.sub(key,to_rep[key],text)
    for key in to_lig:
            text=re.sub(key,to_lig[key],text)
    print(text)

