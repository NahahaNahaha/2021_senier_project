'''
단어 풀 연결 관련 함수들

0. 이슈: 숫자가 들어간 클래스/함수명은?
0.1. 숫자를 중심으로 끊을 것.
0.1.1. 끊어진 숫자가 '123'이라고 하면 one two three, 백이십삼, 일이삼, one hundred twenty three를 인정

영어
1. soundex LCS
2. lcs

한국어
1. 모음끼리
2. 자음끼리
'''

EXC='aehiouwy'
ALPHA=(0,1,2,3,0,1,2,0,0,2,2,4,5,5,0,1,2,6,2,3,0,1,0,2,0,2)
smallA=ord('a')

BASEORDER=ord('가')
HD=( 'ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ',
       'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ' )
MD=('ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ',
     'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ' )
ED=( '', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ',
      'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ',
      'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ')

DM={
    'ㅑ': 'ㅣㅏ',
    'ㅒ': 'ㅣㅐ',
    'ㅕ': 'ㅣㅓ',
    'ㅖ': 'ㅣㅔ',
    'ㅘ': 'ㅗㅏ',
    'ㅙ': 'ㅗㅐ',
    'ㅚ': 'ㅗㅔ',
    'ㅛ': 'ㅣㅗ',
    'ㅝ': 'ㅜㅓ',
    'ㅟ': 'ㅜㅣ',
    'ㅠ': 'ㅣㅜ',
    'ㅢ': 'ㅡㅣ',
    'ㄳ': 'ㄱㅅ',
    'ㄵ': 'ㄴㅈ',
    'ㄶ': 'ㄴㅎ',
    'ㄺ': 'ㄹㄱ',
    'ㄻ': 'ㄹㅁ',
    'ㄼ': 'ㄹㅂ',
    'ㄽ': 'ㄹㅅ',
    'ㄾ': 'ㄹㅌ',
    'ㄿ': 'ㄹㅍ',
    'ㅄ': 'ㅂㅅ',
    }

def subHead(inp, word): # arrange에 사용하게 될 수 있음
    length=min(len(inp), len(word))
    for i in range(length):
        if inp[i] != word[i]:
            return i
    return i


def arrange(inp, words): #일반 기준. keyword는 입력된 음성, words는 함수/클래스 풀
    ar=[]
    basis=soundEx(inp)
    for w in words:
        val=lcs(soundEx(w),basis)
        val2=lcs(inp, w)
        if val > len(basis)/2:
            ar.append((w, val+val2/10))
    ar.sort(key=lambda x: x[1])
    ar.reverse()
    return [x[0] for x in ar]
    
def arrange_s(inp, words):   #spell 기준. keyword는 입력된 음성, words는 함수/클래스 풀
    ar=[]
    for w in words:
        if spell(inp, w):
            ar.append(w)
    ar.sort(key=lambda x: len(x))
    return ar

def soundEx(keyword):   # 일반 케이스
    ret=str(ALPHA[ord(keyword[0])-smallA])
    cur='?'
    for c in keyword[1:]:
        i=ALPHA[ord(c)-smallA]
        cur=i
        if i != 0 and c != cur:
            ret+=str(i)
            '''
            if len(ret)==4:
                return ret
                '''
    return ret
    #return ret.ljust(4,'0')

def spell(inp, keyword):    # 스펠을 부른 케이스
    return (keyword.find(inp) == 0)

def lcs(a, b):  # LCS에서 거리가 3 이상 되면 쳐내도록 수정 예정
    prev = [0]*len(a)
    for i,r in enumerate(a):
        current = []
        for j,c in enumerate(b):
            if r==c:
                e = prev[j-1]+1 if i * j > 0 else 1
            else:
                e = max(prev[j] if i > 0 else 0, current[-1] if j > 0 else 0)
            current.append(e)
        prev = current
    return current[-1]

def standardize(keyword):   # snake, camel/pascal 표기법 지원하여 단어 분리, 숫자 분리
    length=len(keyword)
    # snake (first_second_third)
    ls=keyword.split('_')
    if len(ls) >= 2:
        for i in range(len(ls)):
            ls[i]=ls[i].lower()
        return ls
    # camel/pascal (firstSecondThird/FirstSecondThird)
    for i in range(length):
        keyword('next')

def hme(letter):    # 리턴 (초, 중, 종성)
    letter=ord(letter)-BASEORDER
    ed=ED[letter % 28]
    letter //= 28
    md=MD[letter % 21]
    letter //= 21
    hd=HD[letter]
    if md in DM:
        md=DM[md]
    if ED[ed] in DM:
        ed=DM[ed]
    return hd+md+ed
