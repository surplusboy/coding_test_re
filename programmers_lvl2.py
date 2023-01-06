import itertools
import math
import re
from functools import reduce
from collections import deque


# 22.11.17 Start
def 최댓값과_최소값(s: str) -> str:
    return '{} {}'.format(min(map(int, s.split(' '))), max(map(int, s.split(' '))))

# print(최댓값과_최소값('1 2 3 4'))


def JadenCase_문자열_만들기(s: str) -> str:
    # return ' '.join(list(map(lambda x: x.lower() if x[0].isdigit() else x.capitalize(), re.sub(r' +', ' ', s).lstrip().rstrip().split(' '))))
    return ' '.join(list(map(lambda x: x[0].upper() + x[1:].lower() if x else x, s.split(' '))))

# print(JadenCase_문자열_만들기("3people   unFollowed me"))

# print(JadenCase_문자열_만들기('a aAa2 231A dasdagzA1 camel CaASD '))
# print(JadenCase_문자열_만들기('a3SdfffTtAffttfftt3133Sdf'))


def 최솟값_만들기(A: list, B: list)-> int:
    A.sort(), B.sort(reverse=True)
    return sum(map(lambda x, y: x * y, A, B))

# A = [[1, 2], [4, 3], [2, 5]]
# print(reduce(lambda x, y: x * y, A))

# print(최솟값_만들기([1, 4, 2], [5, 4, 4]))
# print(최솟값_만들기([1, 2], [3, 4]))

# A = [1, 4, 2]
# B = [5, 4, 4]
# print(list(zip(A, B)))


def 올바른_괄호(s: str) -> bool:
    stack = list()
    if len(s) %2 != 0 or s[0] != '(' or s[-1] != ')':
        return False

    for i in s:
        if i == ')':
            if len(stack) == 0:
                return False
            stack.pop()
        else:
            stack.append(i)

    if len(stack) == 0:
        return True
    return False


def 올바른_괄호_다른코드(s: str) -> bool: # ternary operator 를 이용한 구현, 엄청나게 간결하다.
    x = 0
    for w in s:
        if x < 0:
            break
        x = x+1 if w=="(" else x-1 if w==")" else x
    return x==0

# print(올바른_괄호('()()'))
# print(올바른_괄호('(())()'))
# print(올바른_괄호(")()("))
# print(올바른_괄호("(()("))
# print(올바른_괄호('()())(()'))
# print(올바른_괄호('(()())'))
# print(올바른_괄호('()))((()'))
# print(올바른_괄호('((())())'))
# print(올바른_괄호('((()()))'))
# print(올바른_괄호('()())(()'))


def 이진_변환_반복하기(s):

    zero_cnt = 0
    trans_cnt = 0
    while True:
        zero_cnt += str(s).count('0')
        bin_val = s.replace('0', '')
        s = bin(int(len(bin_val)))[2:]
        trans_cnt += 1
        if int(s) == 1:
            return [trans_cnt,zero_cnt]

# print(이진_변환_반복하기("110010101001"))


def 숫자의_표현(n:int) -> int:
    chk = 1
    answer = 0
    while n > 0:
        if n%chk == 0:
            print(chk)
            answer += 1
        n -= chk
        chk += 1

# print(숫자의_표현(15))


def 피보나치_수(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def 다음_큰_숫자(n):

    one = str((bin(n)[2:]).count('1'))
    flag = True
    i = n + 1
    while flag:
        if str((bin(i)[2:]).count('1')) == one:
            return i
        else:
            i += 1

# print(다음_큰_숫자(1))

# for i in range(1, 100):
#     print(bin(i)[2:])


def 카펫(brown, yellow) -> list:
    # yellow = (x-2)(y-2)
    a = brown + yellow
    for i in range(3, int(math.sqrt(a))+1):
        if (a / i).is_integer() and (int(a/i)-2)*(i-2) == yellow:
            return [int(a/i), i]


# print(카펫(10,2))
# print(카펫(18,6))
# print(카펫(24,24))

def 멀리_뛰기(n):
    # combi_list = list()
    # combi_list.append([n, 0])
    #
    # loop = n // 2

    # for i in range(1, loop + 1):
    #     combi_list.append([n-(i*2),i])
    # print(combi_list)
    # result = list()

    # for x, y in combi_list:
    #     print(x,y)
        # result.append(math.factorial(x+y) / math.factorial(x) / math.factorial(y))

    # return int(sum(result) % 1234567)
    cnt = 0
    a, b = 0, 1
    while cnt < n:
        a, b = b, a + b
        cnt += 1
    return b%1234567


# print(멀리_뛰기(12))

def 짝지어_제거하기(s):
    stack = list()

    for i in s:
        if len(stack) >= 1:
            if i == stack[-1]:
                stack.pop()
            else:
                stack.append(i)
        else:
            stack.append(i)
    if stack:
        return 0
    else:
        return 1

# print(짝지어_제거하기('baabaa'))
# print(짝지어_제거하기('cdcd'))

def 영어_끝말잇기(n, words):
    stack = list()
    cnt = 1
    stack.append(words[0])

    for idx, data in enumerate(words[1:]):
        cnt += 1
        if stack[-1][-1] != data[0]:
            return [cnt, (idx+1)//n+1]

        if data not in stack:
            stack.append(data)
        else:
            return [cnt, (idx+1)//n+1]
        if cnt == n:
            cnt = 0
    return [0, 0]


# print(영어_끝말잇기(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
# print(영어_끝말잇기(5, 	["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
# print(영어_끝말잇기(2, ["hello", "one", "even", "never", "now", "world", "draw"]))

# print(int('a0_0x47dd'))

from collections import deque
def 구명보트(people, limit) -> int:
    cnt = 0
    people.sort()

    people = deque(people)
    while people:
        value = people.pop()
        print(value)
        if not people:
            cnt += 1
            break
        else:
            if people[0] + value <= limit:
                people.popleft()
                cnt += 1
            else: cnt += 1

    return cnt

print(구명보트([70, 50, 80, 50], 100))

def 구명보트_간결(people, limit) -> int:
    answer = 0
    people.sort()

    a = 0
    b = len(people) - 1
    while a < b:
        if people[b] + people[a] <= limit:
            a += 1
            answer += 1
        b -= 1
    return len(people) - answer