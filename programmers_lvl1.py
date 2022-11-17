from builtins import len
from collections import deque
from itertools import chain
import math
import sys
import string
import re
import itertools
import datetime

# 22.11.04 Start
# print( sys.getrecursionlimit()) # 재귀허용범위

def 푸드_파이트_대회(food:list):
    foods = [f'{i},{data//2}' for i, data in enumerate(food) if data//2 >= 1]
    result = deque()
    for i in foods[::-1]:
        for _ in range(int(i.split(',')[1])):
            result.appendleft(str(i.split(',')[0]))
            result.append(i.split(',')[0])
    result.insert(int(len(result)/2), '0')
    return ''.join(result)

def 푸드_파이트_대회_효율(food): # stack 뒤집고 chain으로 연결, map으로 문자열 일괄 처리 -> 쓸데없는 반복문과 꼭 해야하는 반복의 범위를 줄임 -> 더 효율적
    stack = []
    for i in range(1, len(food)):
        for _ in range(food[i]//2):
            stack.append(i)
    return ''.join(map(str, chain(stack, [0], stack[::-1])))


# print(푸드_파이트_대회([1, 3, 4, 6]))
# print(푸드_파이트_대회([1, 7, 1, 2]))
def 짝수와_홀수(num:int):
    return 'Even' if num % 2 == 0 else 'Odd'


def 짝수와_홀수_비트연산(num:int): # 비트연산후 인덱싱
    return ["Even", "Odd"][num & 1]



def 평균_구하기(arr:list):
    return sum(arr) / len(arr)



def 약수의_합(n:int):

    result = list()
    for i in range(1, int(math.sqrt(n))+1):
        if n % i == 0:
            result.append(i)
            if i != (n // i):
                result.append(n // i)
    return sum(result)


def 자릿수_더하기(n:int):
    return sum(map(int,list(str(n))))

# print(자릿수_더하기(123))


def 자연수_뒤집어_배열로_만들기(n:int):
    return list(map(int,(list(str(n))[::-1])))

# print(자연수_뒤집어_배열로_만들기(12345))


def 정수_제곱근_판별(n:int):
    return (int(math.sqrt(n)+1)**2) if math.sqrt(n).is_integer() else -1

# print(정수_제곱근_판별(121))

def 문자열_내_p와_y의_개수(s:str):
    check_dict = {'p':0, 'y':0}
    s = s.lower()
    for i in s:
        if i == 'p' or i == 'y':
            check_dict[i] += 1

    return True if check_dict['p'] == check_dict['y'] or sum(check_dict.values()) == 0 else False

# print(문자열_내_p와_y의_개수('pPoooyY'))


def 문자열_내p와_y의_개수_효율(s :str): # count 메소드 활용이 시간, 공간 복잡도 더 적을듯
    return s.lower().count('p') == s.lower().count('y')


def 하샤드_수(arr:int):
    return False if arr % sum(map(int,(list(str(arr))))) else True


def 문자열을_정수로_바꾸기(s:str):
    return int(s)


def x만큼_간격이_있는_n개의_숫자(x:int, n:int):
    return [x * i for i in range(1,n+1)]


def 정수_내림차순으로_배치하기(n:int):
    return int(''.join(map(str,(list(sorted(map(int,list(str(n))),reverse=True))))))

# print(정수_내림차순으로_배치하기(118372))

def 나머지가_1이_되는_수_찾기(n:int):
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 1:
            return i
    return n-1

# print(나머지가_1이_되는_수_찾기(12))

def 두_정수_사이의_합(a, b) -> int:
    max_v, min_v = max([a, b]), min([a, b])
    return int(((max_v+1)*max_v/2) - (((min_v-1)+1)*(min_v-1)/2))

def 두_정수_사이의_합_절댓값(a, b) ->int: # 수열을 이용한 수학식, 내가 푼 가우스 풀이법보다 효율적 -> 쓸데없는 변수없고 즉시 연산
    return (abs(a - b) + 1) * (a + b) // 2


def 콜라츠_재귀(count, n):
    if count >=500:
        return -1
    if n % 2 == 0:
        return 콜라츠_재귀(count+1, n/2)
    else:
        if n == 1:
            return count
        return 콜라츠_재귀(count+1, n*3+1)

def 콜라츠_추측(count, n):
    return 콜라츠_재귀(count, n)
# print(콜라츠_추측(0, 3))


def 서울에서_김서방_찾기(seoul:list):
    if 'Kim' in seoul:
        return '김서방은 {}에 있다'.format(seoul.index('Kim'))

# print(서울에서_김서방_찾기(["Jane", "Kim"]))


def 핸드폰_번호_가리기(phone_number:str):
    deid = phone_number[-4:]
    return '*' * (len(phone_number)-4) + deid

# print(핸드폰_번호_가리기("01033334444"))

def 나누어_떨어지는_숫자_배열(arr, divisor):
    result = sorted(list(filter(None,(map(lambda x: None if x % divisor else x, arr)))))
    return result if result else [-1]

# print(나누어_떨어지는_숫자_배열([5, 9, 7, 10], 5))

def 제일_작은_수_제거하기(arr):
    arr.remove(min(arr))
    return arr or [-1]

# print(제일_작은_수_제거하기([4,3,2,1]))


def 음양_더하기(absolutes, signs)-> int:

    answer = 0
    for i, integer in enumerate(absolutes):
        if signs[i]:
            answer += integer
        else: answer += -integer

    return answer

# print(음양_더하기([4,7,12], [True,False,True]))

def 없는_숫자_더하기(numbers:list) -> int:
    return sum(set(range(10)) - set(numbers))

# print(없는_숫자_더하기([1,2,3,4,6,7,8,0]))

def 가운데_글자_가져오기(s:str) -> str:
    return s[len(s)//2] if len(s) % 2 else s[(len(s)//2)-1:(len(s)//2)+1]

# print(가운데_글자_가져오기('qwer'))

def 수박수박수박수박수박수(n:int) -> str:
    a = '수박'*(n//2+1)
    return a[:n]

def 내적(a:list, b:list) -> int:
    answer = 0
    for i  in range(len(a)):
         answer += a[i] * b[i]
    return answer

# print(내적([1,2,3,4],[-3,-1,0,2]))

def 문자열_내림차순으로_배치하기(s:str) -> str:
    return ''.join(sorted(s, reverse=True))


def 문자열_다루기_기본(s:str) -> bool:
    return True if s.isdigit() and (len(s) == 4 or len(s) == 6) else False


def 약수의_개수_함수(x:int) -> int:
    count = 0
    for i in range(1, int(math.sqrt(x)+1)):
        if x % i == 0:
            count += 1
    return count

def 약수의_개수와_덧셈(left, right) -> int:
    answer = 0
    for i in range(left, right+1):
        count = 0
        for j in range(1, int(math.sqrt(i) + 1)):
            if i % j == 0:
                count += 1
                if j != (i // j):
                    count += 1
        if count % 2 == 0:
            answer += i
        else:
            answer += -i
    return answer


# print(약수의_개수와_덧셈(13, 17))
# print(약수의_개수와_덧셈(24, 27))

def 행렬의_덧셈(arr1:list, arr2:list) -> list:

    for i, j in zip(arr1, arr2):
        for k in range(len(i)):
            i[k] += j[k]
    return arr1

    # print(arr1)

def 직사각형_별찍기(a, b):

    answer = ['*' * a for i in range(b)]
    for i in answer:
        print(i)


def 최대공약수와_최소공배수(n, m) ->list:
    return [math.gcd(n, m), math.lcm(n, m)]


# print(최대공약수와_최소공배수(3, 12))

def 같은_숫자는_싫어(arr:list) -> list:

    answer = [None]
    for i in arr:
        if not answer[-1] == i:
            answer.append(i)

    return answer[1:]


def 이상한_문자_만들기(s:str) -> str:
    s = s.split(' ')
    answer = ''
    for i in s:
        for j in range(len(i)):
            if not j % 2 == 0:
                answer += i[j].lower()
            else:
                answer += i[j].upper()
        answer += ' '
    return answer[:-1]

# print(이상한_문자_만들기("try hello world"))

def binary_convert(n): # 진수변환 컨버터
    n, b = divmod(n, 3)
    if n == 0:
        return tmp[b]
    else:
        return binary_convert(n) + tmp[b]


tmp = string.digits+string.ascii_lowercase
def three진법_뒤집기(n:int) -> int:
    return int(str(binary_convert(n)[::-1]), 3)


def 예산(d:list, budget:int) -> int:
    d.sort()
    cnt = 0
    for i in d:
        cnt += 1
        if budget - i < 0:
            cnt -= 1
        budget -= i
    return cnt

def 시저_암호(s:str ,n:int) -> str:
    a = ''.join(list(map(lambda x : chr(ord(x)+n - 26) if ord(x.upper())+n >= 91 else chr(ord(x)+n), s)))
    return re.sub(r'[^a-zA-Z]', ' ', a)

# print(시저_암호('AB', 1))
# print(시저_암호('z', 1))
# print(시저_암호("a B z", 4))

def 카카오_비밀지도_2018(n, arr1, arr2):
    arr1 = list(map(lambda x: format(x, 'b') if len(format(x, 'b')) == n else '{0:b}'.format(x).zfill(n), arr1))
    arr2 = list(map(lambda x: format(x, 'b') if len(format(x, 'b')) == n else '{0:b}'.format(x).zfill(n), arr2))

    answer = list()
    for i in range(n):
        result = str()
        for j in range(n):
            if arr1[i][j] == '0' and arr2[i][j] == '0':
                result += ' '
            else:
                result += '#'
        answer.append(result)
    return answer

# print(카카오_비밀지도_2018(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
# print(카카오_비밀지도_2018(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10]))


def 카카오_비밀지도_2018_효율(n, *maps): # 개인적으로 제일 잘 구현 된 코드라 생각
    return [line(n, a | b) for a, b in zip(*maps)] # 재귀 구현


def line(n, x):
    return ''.join(' #'[int(i)] for i in f'{x:016b}'[-n:])


def 최소직사각형(sizes:list):
    for i in sizes:
        i.sort()
    c = sum(sizes, [])

    return max(c[::2]) * max(c[1::2])

# print(최소직사각형([[60, 50], [30, 70], [60, 30], [80, 40]]))

def 문자열_내_맘대로_정렬하기(strings, n):
    strings = sorted(strings, key=lambda x: (x[n], x[:n], x[n:]))
    return strings


def k번째_수(array, commands):
    answer = list()
    i, j, k  = list(map(lambda x: x[0], commands)), list(map(lambda x: x[1], commands)), list(map(lambda x: x[2], commands))
    for x in range(len(i)):
        answer.append(list(sorted(array[i[x]-1:j[x]]))[k[x]-1])
    return answer

# print(k번째_수([1, 5, 2, 6, 3, 7, 4],	[[2, 5, 3], [4, 4, 1], [1, 7, 3]]))

def 숫자_문자열과_영단어(s:str):
    int_str = {'0' : 'zero', '1' : 'one', '2' : 'two', '3' : 'three', '4' : 'four', '5' : 'five', '6' : 'six', '7' : 'seven', '8' : 'eight', '9' : 'nine'}

    for i, j in int_str.items():
        if j in s:
            s = s.replace(j, i)
    return s

# print(숫자_문자열과_영단어("one4seveneight"))
# print(숫자_문자열과_영단어("23four5six7"))

def 두_개_뽑아서_더하기(numbers:list):
    answer = list()
    numbers = list(itertools.combinations(numbers, 2))
    for i in numbers:
        answer.append(sum(i))
    return sorted(list(set(answer)))

# print(두_개_뽑아서_더하기([2,1,3,4,1]))
# print(두_개_뽑아서_더하기([5,0,2,7]))

def 삼총사(number:list) -> int:

    numbers = list(itertools.combinations(number, 3))
    cnt = 0
    for i in numbers:
        if sum(i) == 0:
            cnt += 1
    return cnt

# print(삼총사([-2, 3, 0, 2, -5]))

def 현재는무슨요일(a, b):
    days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    return days[datetime.date(2016, a, b).weekday()]
# print(현재는무슨요일(3, 1))

def 폰켓몬(nums):
    a = int(len(nums) / 2)
    return a if len(set(nums)) > a else len(set(nums))

# print(폰켓몬([3,1,2,3]))
# print(폰켓몬([3,3,3,2,2,4]))
# print(폰켓몬([3,3,3,2,2,2]))

def 모의고사(answers): # 완전 탐색
    pattern = [[1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5]]
    result = dict()
    answer = list()

    for i in range(len(pattern)):
        cnt = 0
        for j in [answers[j:j + len(pattern[i])] for j in range(0, len(answers), len(pattern[i]))]:
            for idx, data in enumerate(j):
                if pattern[i][idx] == j[idx]:
                    cnt += 1
        result[i+1] = cnt

    max_v = max(result.values())
    for i, j in result.items():
        if j == max_v:
            answer.append(i)

    return answer

# print(모의고사([1,2,3,4,5,1,2,3,4,4]))
# print(모의고사([1,2,3,4,5]))
# print(모의고사([1,3,2,4,2]))


def 모의고사_다른코드(answers): # 배열 선생성후 진행
    p = [[1, 2, 3, 4, 5],
         [2, 1, 2, 3, 2, 4, 2, 5],
         [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    s = [0] * len(p)

    for q, a in enumerate(answers):
        for i, v in enumerate(p):
            if a == v[q % len(v)]:
                s[i] += 1
    return [i + 1 for i, v in enumerate(s) if v == max(s)]

def 모의고사_다른코드2(answers): # cycle 함수를 사용했군
    giveups = [
        itertools.cycle([1,2,3,4,5]),
        itertools.cycle([2,1,2,3,2,4,2,5]),
        itertools.cycle([3,3,1,1,2,2,4,4,5,5]),
    ]
    scores = [0, 0, 0]
    for num in answers:
        for i in range(3):
            if next(giveups[i]) == num:
                scores[i] += 1
    highest = max(scores)

    return [i + 1 for i, v in enumerate(scores) if v == highest]

def 소수_찾기(n): # 에라토스테네스의 체
    prime_flag = [True for i in range(n+1)]  # 0을 포함한 n길이만큼의 배열 생성 후 소수로 간주

    for i in range(2, int(math.sqrt(n)) + 1):
        if prime_flag[i] == True:
            j = 2
            while i * j <= n:
                prime_flag[i*j] = False
                j += 1

    return len([i for i in range(2, n+1) if prime_flag[i]])


# print(소수_찾기(10))
# print(소수_찾기(5))


def 소수_찾기_다른코드(n): # 에라토스테네스의 체를 좀 더 짧게 함축
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)


def 소수_만들기(nums:list) -> int:
    nums = list(map(lambda x: sum(x), itertools.combinations(nums, 3)))

    n = max(nums)

    prime_flag = [True for i in range(n + 1)]

    for i in range(2, int(math.sqrt(n)) + 1):
        if prime_flag[i] == True:
            j = 2
            while i * j <= n:
                prime_flag[i*j] = False
                j += 1
    cnt = 0
    prime_flag = [i for i in range(2, n+1) if prime_flag[i]]
    for i in nums:
        if i in prime_flag:
            cnt +=1
    return cnt
# print(소수_만들기([1,2,3,4]))

def 소수_만들기_다른코드(nums:list) -> int: # 깔끔한 코드, 단일 소수 판별, 시간 복잡도 많이 낮을것
    from itertools import combinations as cb
    answer = 0
    for a in cb(nums, 3):
        cand = sum(a)
        for j in range(2, cand):
            if cand%j==0:
                break
        else:
            answer += 1
    return answer


def 실패율(N:int, stages:list) -> list:
    stages = sorted(stages)
    total_stage = [0 for _ in range(1, N+2)]
    clear_dict = { idx+1:val for idx,val in enumerate(total_stage) }
    for i in stages:
        clear_dict[i] += 1

    data = list(clear_dict.values())
    for idx, clear in enumerate(data):
        if clear == 0 or sum(data[idx:]) == 0:
            continue
        if idx < N:
            clear_dict[idx+1] = clear / sum(data[idx:])

    answer = sorted(clear_dict.items(), key=lambda x: (-x[1], x[0]))
    return list(filter(lambda x:x<=N, list(dict(answer).keys())))

# print(실패율(5, [2, 1, 2, 6, 2, 4, 3, 3]))
# print(실패율(4, [4,4,4,4,4]))
# print(실패율(5, [2, 2, 2, 2, 2, 2, 2, 2]))


def 실패율_다른코드(N:int, stages:list) -> list: # count를 사용 직관적이지만 시간복잡도 증가
    result = {}
    denominator = len(stages)
    for stage in range(1, N + 1):
        if denominator != 0:
            count = stages.count(stage)
            result[stage] = count / denominator
            denominator -= count
        else:
            result[stage] = 0
    return sorted(result, key=lambda x: result[x], reverse=True)


def 다트_게임(dartResult:str) -> int:

    # options = list()
    # for idx, data in enumerate(dartResult):
    #     if data in ['*', '#']:
    #         options.append([idx, data])
    # print(list(map(lambda x: x[1] if squared.get(x[1]) is not None else 0, list(enumerate(dartResult)))))
    # result = list(map(lambda x: int(dartResult[x[0]-1]) ** squared.get(x[1]) if squared.get(x[1]) is not None else 0, list(enumerate(dartResult))))

    # print(result)
    # print(options)
    # for i in options:
        # print(i)
        # if i[1] == '*':
        #     print(i[0])
        #     result[i[0]-1] = result[i[0]-1] * 2
        #     result[i[0]-3] = result[i[0]-3] * 2
        #     if result[i[0]-3] * 2 == 0:
        #         result[i[0]-4] = result[i[0]-4] * 2
        # elif i[1] == '#':
        #     result[i[0]-1] = -result[i[0]-1]
    # print(result)
    # return sum(result)


    # option = list()
    # for idx, data in enumerate(score):
    #     if '*' in data:
    #         option.append([idx-1, data[0]])
    #     elif '#' in data:
    #         option.append([idx - 1, data[0]])


    # bonus = [i for i in dartResult if i in ['S','D','T']]


    # print(option)
    # print(bonus)

    squared = {'S': 1, 'D': 2, 'T': 3}
    score = re.split(r'[SDT]', dartResult)
    score = list(map(lambda x: re.sub(r'[^0-9]', '', x),score))[:-1]

    a = re.finditer('[SDT*#]', dartResult)
    before = list()
    # print(a)
    cnt = 0
    for idx, data in enumerate(a):
        # print(data)
        # input('data check')
        if not data[0] in ['*', '#']:
            # before.append([int(dartResult[data.start()-1]), dartResult[data.start()]])
            before.append([dartResult[data.start()]])
        if data[0] in ['*', '#']:
            cnt += 1
            before[idx-cnt].append(data[0])

    score = list(map(int, score))

    for idx, data in enumerate(before):
        score[idx] = score[idx] ** squared[data[0]]
        if data[-1] == '*':
            score[idx] *= 2
            if idx != 0:
                score[idx-1] *= 2
        elif data[-1] == '#':
            score[idx] = -score[idx]
    return sum(score)

    # for idx, data in enumerate(before):
    #     data[0] = data[0] ** squared[data[1]]
    #     if data[-1] == '*':
    #         data[0] *= 2
    #         if idx != 0:
    #             before[idx-1][0] *= 2
    #     elif data[-1] == '#':
    #         data[0] = -data[0]



    # print(score)
    #

# print(다트_게임('1S2D*3T'))
# print(다트_게임('1S2D*3T'))
# print(다트_게임('1D2S#10S'))
# print(다트_게임('1D2S0T'))
# print(다트_게임('1S*2T*3S'))
# print(다트_게임('1D#2S*3S'))
# print(다트_게임('1T2D3D#'))
# print(다트_게임('1D2S3T*'))


def 다트_게임_다른코드(dartResult:str): # 접근을 너무 잘못햇다. 간단하게 정규표현식으로 끝내야할 문제 였음. 굳이 한게임별 배열을 생성할 필요가 X, 컴파일 모듈을 좀 더 알고 있었어야했다.
    bonus = {'S': 1, 'D': 2, 'T': 3}
    option = {'': 1, '*': 2, '#': -1}
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    print(dart)
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i - 1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    answer = sum(dart)
    return answer

def 과일_장수(k, m, score):
    score.sort(reverse=True)
    apples = len(score)//m
    result = list()
    answer = 0
    cnt = 0
    for i in range(apples):
        result.append(score[cnt:m+cnt])
        cnt += m
    for i in result:
        answer += min(i) * len(i)
    return answer


def 과일_장수(k, m, score):
    score.sort(reverse=True)
    answer = 0

    for i in range(0, len(score)-m+1, m):
        answer += (min(score[i:i+m])) * m
    return answer

# print(과일_장수(3, 4,[1, 2, 3, 1, 2, 3, 1]))
# print(과일_장수(4, 3, [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]))

def 햄버거_만들기(ingredient:list) -> int: # 스택 문제

    cnt = 0
    stack = list()

    for idx, data in enumerate(ingredient):
        stack.append(data)
        if len(stack) >= 4:
            if stack[-4:] == [1,2,3,1]:
                for _ in range(4):
                    stack.pop()
                cnt += 1
    return cnt

# print(햄버거_만들기([2, 1, 1, 2, 3, 1, 2, 3, 1]))
# print(햄버거_만들기([1, 3, 2, 1, 2, 1, 3, 1, 2]))

def 로또의_최고_순위와_최저_순위(lottos:list, win_nums:list):
    result_dict = { 6 : 1, 5 : 2, 4 : 3, 3 : 4, 2 : 5, 1 : 6, 0 : 6}

    min_v = len(set(a) & set(b))
    max_v = lottos.count(0) + min_v

    return [result_dict[max_v],result_dict[min_v]]

a = [44, 1, 0, 0, 31, 25]
b = [31, 10, 45, 1, 6, 19]

# print(로또의_최고_순위와_최저_순위(a, b))

def 콜라_문제(a, b, n):
    cnt = 0
    while n >= a:
        x, y = divmod(n, a)
        cnt += x * b
        n = x * b + y
        print(n)

    return int(cnt)

# print(콜라_문제(2, 1, 20))
# print(콜라_문제(3, 1, 20))

def 체육복(n:int, lost:list, reserve:list):
    new_reserve = sorted(list(set(reserve) - set(lost)))
    new_lost = sorted(list(set(lost) - set(reserve)))

    for i in new_reserve[::-1]:
        if new_lost.count(i + 1):
            new_reserve.pop(new_reserve.index(i))
            new_lost.pop(new_lost.index(i+1))
        elif new_lost.count(i - 1):
            new_reserve.pop(new_reserve.index(i))
            new_lost.pop(new_lost.index(i-1))
        else:
            pass
    return n - len(new_lost)


# print(체육복(5, [2, 4], [3, 1]))
# print(체육복(5, [2, 4], [1, 2, 4]))
# print(체육복(5, [2, 4, 5], [1, 2, 4]))
# print(체육복(7, [1, 3, 4], [1, 3, 5]))
# print(체육복(5, [2, 4], [1, 3, 5]))
# print(체육복(5, [2, 4], [3]))
# print(체육복(3, [3], [1]))
# print(체육복(5, [5], [1]))
a = [1, 2]

# for i in range(1000, 100001, 1000):
#     print(i)
#     print(int(i + (i * 0.03)))
#     print(int(i + (i * 0.03)) / 5990)
#     print('----')

def 완주하지_못한_선수(participant, completion):

    player = dict()
    participant.sort()

    for i in participant:
        if i not in player.keys():
            player[i] = 1
        else:
            player[i] += 1

    for i in completion:
        player[i] -= 1

    return [key for key, value in player.items() if value == 1][0]


# print(완주하지_못한_선수(["leo", "kiki", "eden"],["eden", "kiki"]))
# print(완주하지_못한_선수(["mislav", "stanko", "mislav", "ana"],	["stanko", "ana", "mislav"]))

def 완주하지_못한_선수_해쉬(participant, completion):
    temp = 0
    dic = dict()
    for part in participant:
        print(hash(part))
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer

# print(완주하지_못한_선수_해쉬(["leo", "kiki", "eden"],["eden", "kiki"]))


def 키패드_누르기(numbers, hand): # 카카오 2020 인턴쉽 문제
    keypad = { 1: (0, 0), 2: (0, 1), 3: (0, 2),
               4: (1, 0), 5: (1, 1), 6: (1, 2),
               7: (2, 0), 8: (2, 1), 9: (2, 2),
               '*': (3, 0), 0: (3, 1), '#': (3, 2)
    }
    if hand == 'right':
        hand = 'R'
    else:
        hand = 'L'
    key_stack = {'L': (3, 0), 'R': (3, 2)}
    answer = str()

    for idx, data in enumerate(numbers):
        if data in [1, 4, 7]:
            answer += 'L'
            key_stack['L'] = keypad[data]
        elif data in [3, 6, 9]:
            answer += 'R'
            key_stack['R'] = keypad[data]
        elif data in [2, 5, 8, 0]:
            d = [abs(key_stack.get('L')[0] - keypad[data][0]), abs(key_stack.get('L')[1] - keypad[data][1])]
            e = [abs(key_stack.get('R')[0] - keypad[data][0]), abs(key_stack.get('R')[1] - keypad[data][1])]
            if sum(d) < sum(e):
                key_stack['L'] = keypad[data]
                answer += 'L'
            elif sum(d) > sum(e):
                key_stack['R'] = keypad[data]
                answer += 'R'
            elif sum(d) == sum(e):
                key_stack[hand] = keypad[data]
                answer += hand

    return answer

# print(키패드_누르기([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], 'right'))
# print(키패드_누르기([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], 'left'))
# print(키패드_누르기([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 'right'))

def 크레인_인형뽑기_게임(board, moves): # 스택으로 접근

    stack = list()
    cnt = 0

    for i in moves:
        while len(stack) >= 2:
            if stack[-1] == stack[-2]:
                cnt += 2
                for _ in range(2):
                    stack.pop()
            else:
                break

        for idx, data in enumerate(board):
            if data[i-1]:
                stack.append(data[i-1])
                board[idx][i-1] = 0
                break

    return cnt

def 크레인_인형뽑기_게임_다른코드(board, moves): # 가장 간결하게 pythonic 한 코드
    cols = list(map(lambda x: list(filter(lambda y: y > 0, x)), zip(*board)))
    a, s = 0, [0]

    for m in moves:
        if len(cols[m - 1]) > 0:
            if (d := cols[m - 1].pop(0)) == (l := s.pop()):
                a += 2
            else:
                s.extend([l, d])

    return a

def 신규_아이디_추천(new_id):
    '''
    1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다. O
    2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다. O
    3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다. O
    4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다. O
    5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다. O
    6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다. O
     만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다. O
    7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다. O
    '''
    new_id = re.sub(r'\.+', '.', re.sub(r'[^a-z0-9-_.]', '', new_id.lower())).lstrip('.').rstrip('.')[:15].rstrip('.')
    if not new_id:
        new_id = 'a'

    if len(new_id) <= 2:
        new_id += new_id[-1] * 2
        new_id = new_id[:3]

    return new_id


# print(신규_아이디_추천("...!@BaT#*..y.abcdefghijklm"))
# print(신규_아이디_추천("aaaaaaaaaaaaaa"))
# print(신규_아이디_추천("dd..d"))


def 숫자_짝궁(X, Y):

    result_dict = dict()

    for i in set(X):
        a = Y.count(i)
        if a > X.count(i):
            result_dict[i] = X.count(i)
        else:
            result_dict[i] = a

    answer = str()
    for i, j in result_dict.items():
        answer += i*j

    if not answer:
        return '-1'
    elif sorted(list(answer))[-1] == '0':
        return '0'

    return ''.join(sorted(list(answer),reverse= True))

# print(숫자_짝궁("100", "2345"))
# print(숫자_짝궁('100', "203045"))
# print(숫자_짝궁('100', "123450"))
# print(숫자_짝궁('12321', "4253100"))
# print(숫자_짝궁("5525",'1255'))

# print(숫자_짝궁("5525",'125555'))

def 옹알이_ver2(babbling:list):
    accent = {'a': "aya",'y': "ye",'w': "woo",'m': "ma"}

    cnt = 0
    for i in babbling:
        stack = ['']
        while True:
            if len(i) == 0:
                cnt += 1
                break
            if accent.get(i[0]):
                if i[:len(accent.get(i[0]))] == accent.get(i[0]):
                    stack.append(accent.get(i[0]))
                    if stack[-1] == i[len(accent.get(i[0])):][:len(accent.get(i[0]))]:
                        break
                    i = i[len(accent.get(i[0])):]

                else:
                    break
            else:
                break
    return cnt

# print(옹알이_ver2(["aya", "yee", "u", "maa"]))
# print(옹알이_ver2(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]))

def 옹알이_ver2_다른코드(babbling:list): # 아주 간결한 코드
    answer = 0
    for i in babbling:
        for j in ['aya','ye','woo','ma']:
            if j*2 not in i:
                i=i.replace(j,' ')
        if len(i.strip())==0:
            answer +=1
    return answer


def 성격_유형_검사하기(survey, choices):
    score = { 1: 3, 2: 2, 3: 1, 4: 0, 5: 1, 6: 2, 7: 3}
    your_type = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}

    for idx, data in enumerate(survey):
        if choices[idx] > 4:
            your_type[data[1]] += score[choices[idx]]
        elif choices[idx] < 4:
            your_type[data[0]] += score[choices[idx]]
        else:
            pass
    result = [[list(your_type.items())[i], list(your_type.items())[i+1]] for i in range(0, int(len((your_type.items()))), 2)]
    answer = str()
    for i in result:
        if i[0][1] >= i[1][1]:
            answer += i[0][0]
        else:
            answer += i[1][0]
    return answer

# print(성격_유형_검사하기(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))
# print(성격_유형_검사하기(["TR", "RT", "TR"], [7, 1, 3]))

def 신고_결과_받기(id_list, report, k): # 카카오 2022 블라인드 테스트
    report_dict = dict()
    result_mail = dict()
    report = list(set(report))
    id_list = {data: 0 for idx, data in enumerate(id_list)}

    for i in report:
        a, b = i.split(' ')[0], i.split(' ')[1]
        if not report_dict.get(b):
            report_dict[b] = 1
            if not result_mail.get(b):
                result_mail[b] = [a]
            else:
                result_mail[b].append(a)
        else:
            report_dict[b] += 1
            if not result_mail.get(b):
                result_mail[b] = [a]
            else:
                result_mail[b].append(a)

    block_list = list()

    for key, value in report_dict.items():
        if value >= k:
            block_list.append(key)

    for i in block_list:
        for j in result_mail[i]:
            id_list[j] += 1

    return list(id_list.values())

def 신고_결과_받기_다른코드1(id_list, report, k): # 직관적이고 간결한코드 1

    answer = [0] * len(id_list)
    reports = {x : 0 for x in id_list}

    for r in set(report):
        reports[r.split()[1]] += 1

    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer

def 신고_결과_받기_다른코드2(id_list, report, k): # 직관적이고 간결한 코드 2
    answer = [0] * len(id_list)
    dic_report = {id: [] for id in id_list}  # 해당 유저를 신고한 ID
    for i in set(report):
        i = i.split()
        dic_report[i[1]].append(i[0])

    for key, value in dic_report.items():
        if len(value) >= k:
            for j in value:
                answer[id_list.index(j)] += 1

    return answer


# print(신고_결과_받기(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))
# print(신고_결과_받기(["con", "ryan"],["ryan con", "ryan con", "ryan con", "ryan con"], 3))

def 기사단원의_무기(number:int, limit:int, power:int) -> int:

    result = int()
    for i in range(2, number+1):
        count = 0
        for j in range(1, int(math.sqrt(i) + 1)):
            if i % j == 0:
                count += 1
                if j != (i // j):
                    count += 1
        if not count > limit:
            result += count
        else:
            result += power
    # result = map(lambda x: power if x > limit else x, result)
    return result + 1
print(기사단원의_무기(5, 3, 2))
print(기사단원의_무기(10, 3, 2))