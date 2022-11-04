import math
import itertools
import re
import operator
import random
import matplotlib.pyplot as plt
from collections import Counter
# 그냥 노트페이지임
[1, 2, 3, 4]


# 22.11.04 클리어완료

def solution(angle):
    marking = angle / 90
    angle_list = [1, 3, 4]

    answer = angle_list[int(marking)]

    return answer


def solution2(angle):
    angle_list = [1, 3, 4]

    marking = angle / 90
    if marking != 1:
        marking = math.trunc(marking)
        answer = angle_list[marking]
    else:
        answer = 2
    return answer


point = 12 // 2
result_list = [i * 2 for i in range(1, point + 1)]

# test_list = [1, 1, 2, 3, 4, 5]
test_list = [149, 180, 192, 170]
# test_list = [180, 120, 140]


test_list.sort()
n = 167


def solution_4(array, height):
    print(max(array))
    if max(array) < height:
        answer = 0
    else:
        for i, data in enumerate(array):
            if n > data:
                answer = len(array[i + 1:])
                break
            break
    return answer


# print(solution_4([149, 180, 192, 170], 167))
answer = len(list(filter(lambda test: test > n, test_list)))
# print(answer)

n = 2
# print(-2//abs(-2))

# dot = [2, 4]
# dot = [-7, -9]
dot = [5, 5]  # 2
# dot = [-5, 5] # 0
# dot = [-5, -5] # -2
# dot = [5, -5] # 0

point = (dot[0] // abs(dot[0])) + (dot[1] // abs(dot[1]))
if point == 0:
    if dot[0] < 0:
        point = 2
    else:
        point = 4
# print(abs(point - 1))
# print(point)
# print(result)


# print(test_list.index(3))
#
# if n >= test_list[int(len(test_list)/2)]:
#     for i in test_list[int(len(test_list)/2):]:
#         print(i)
# else:
#     for i in test_list[:int(len(test_list)/2)]:
#         print(i)


# def baby():
#     possible = ["aya", "ye", "woo", "ma"]

# babbling = ["aya", "yee", "u", "maa"]
babbling = ["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]
# babbling = ["ayayewoomawooma"]
possible = {'a': 'aya', 'y': 'ye', 'w': 'woo', 'm': 'ma'}
keys = possible.keys()

count = 0

for i in range(len(babbling)):
    check_str = babbling[i]
    check_list = list()
    flag = True

    while check_str and check_str[0] in keys:
        if len(check_str) < 2:
            break
        vali_str = check_str[0]
        check_str = check_str.replace(possible[check_str[0]], '', 1)
        if not check_list or check_list[-1] != vali_str:
            check_list.append(vali_str)
        elif check_list[-1] == vali_str:
            flag = False
            break
    # print(check_str)
    if not check_str and flag:
        count += 1


# print(count)

# Test Case 첫번째 통과 못하는 코드
# for i in range(len(babbling)):
#     check_str = babbling[i]
#
#     for j in possible:
#         check_str = check_str.replace(j, 'x', 1)
#         if len(list(filter(lambda text: text == 'x', check_str))) >= 2:
#             continue
#         check_str = check_str.replace('x', '')
#     if len(check_str) == 0:
#         print(babbling[i])
#         count += 1
#
# print(count)

def solution_5(babbling):
    answer = 0
    bab = ['aya', 'ye', 'woo', 'ma']
    words = []
    for i in range(1, 5):
        w = []
        for i, case in enumerate(itertools.permutations(bab, i)):
            w.append('')
            for babs in case:
                w[i] += babs
        words.append(w)
    words = list(itertools.chain(*words))
    for i in range(0, len(babbling)):
        if babbling[i] in words:
            answer += 1

    return answer


# print(solution_5(["ayayewoomawooma"]))

# print(len(list(filter(lambda test: test == 'x', 'xyx'))))

def solution_6(babbling):
    babbling_list = {'a': 'aya', 'y': 'ye', 'w': 'woo', 'm': 'ma'}

    answer = 0
    for word in babbling:  # 검증할 문장
        stack = list()
        flag = True
        keys = babbling_list.keys()

        while word and word[0] in keys:
            print(word)
            if len(word) < 2:
                break
            new_stack = word[0]
            word = word.replace(babbling_list[word[0]], '', 1)
            if not stack or stack[-1] != new_stack:
                stack.append(new_stack)
            elif stack[-1] == new_stack:
                flag = False
                break

        if not word and flag:
            answer += 1

    return answer


# print(solution_6(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]))

# n = 2
# test_list = [i*2 for i in range(n, 11)]
# print(test_list)

# test_list = '1234'
# test_list.reverse()
# my_string = 'jaron'
# rev = my_string[::-1]
# print(rev)
# answer = ''.join(rev)

def 순서쌍찾기():
    n = 100

    # 1 9, 3 3, 9 1
    answer = 0
    point = math.sqrt(n)
    print(point)
    i = 1
    while i <= point:
        if n % i == 0:
            answer += 2
        i += 1
    if i - 1 == point:
        answer -= 1
        print(answer)
    else:
        print(answer)


# n = 101
# answer = 0
# #
# # if n % 2 == 0:
# if True:
#     # point = int(math.sqrt(n))
#     point = n // 2
#     # print(point)
#     for i in range(1, point):
#         if point % i == 0:
#             answer += 1
#             print(i)
#     result = (answer * 2) + 2
# #     #
#     if (n * 0.1) * (n * 0.1) == n:
#         result -= 1
# print(result)

# test_input = [1, 3, 6, 4, 1, 2]
# test_input = [1, 2, 3]
# test_input = [-1, -3, 1, 2, 5, 3]
test_input = [-1, -3]

test_input.sort()
test_input = list(set(test_input))


# if min(test_input) < 0:
#     positive_list = [i for i in test_input if i > 0]
#     vali_list = [i for i in range(1, len(positive_list) + 1)]
#     for i in range(len(positive_list)):
#         if positive_list[i] != vali_list[i]:
#             result = vali_list[i]
#         else:
#             result = vali_list[-1] + 1
#     print(result)
# else:
#     vali_list = [i for i in range(1, len(test_input) + 1)]
#     for i in range(len(test_input)):
#         if test_input[i] != vali_list[i]:
#             result = vali_list[i]
#         else:
#             result = vali_list[-1] + 1
#     print(result)

# def result_func(data:list, vali:list):
#     for i in range(len(data)):
#         if data[i] != vali[i]:
#             result = vali[i]
#             return result
#         else:
#             result = vali[-1]
#             return result
# null_list = []
# if null_list:
#     print()
#
# if min(test_input) < 0:
#     positive_list = [i for i in test_input if i > 0]
#     if not positive_list:
#         vali_list = [i for i in range(1, len(positive_list) + 1)]
#         c = result_func(positive_list, vali_list)
#         print(c)
#     else:
#         print(1)
#
# else:
#     vali_list = [i for i in range(1, len(test_input) + 1)]
#     c = result_func(test_input, vali_list)
#     print(c)


# print(vali_list)

# for i in range(len(test_input)):
#     if test_input[i] != vali_list[i]:
#         # print(test_input[i])
#         # print(vali_list[i])
#         result = vali_list[i]
#     else:
#         result = vali_list[-1] +1
#
# print(result)


# min_value = min(test_input)
# avg_value = round(test_input)/2)

# print(min_value)
# print(avg_value)

# test_it = iter(test_input)
# for i in test_input:
#     print(i)

# A = [1, 3, 6, 4, 1, 2] # 5
# A = [1, 2, 3] # 4
# A = [1]
# A = [-1, -3] # 1
# A = [-1, -3, 3, 2]
# A = [-1, -3, 3, 7, 5, 2]
# A = [1567, 5671, 66, 77, 77, 88, 99, 100, 102, 104]

def solution_7(A: list):
    A.sort()
    A = list(set(A))
    positive_list = [i for i in A if i > 0]
    A = positive_list
    B = [i for i in range(1, len(A) + 1)]  # 검증용 리스트

    if len(A) > 0:
        for i in range(1, len(A) + 1):
            if i != A[i - 1]:
                return i
                break
            elif A == B:
                return A[-1] + 1
                break
    else:
        return 1


def solution_8(A: list):
    A.sort()
    A = list(set(A))
    result = 1
    for i in A:
        if i == result:
            result += 1
    return result


# print(solution_8(A))

# A.sort()
# A = list(set(A))
# if min(A) < 0:
#     positive_list = [i for i in A if i > 0]
#     A = positive_list
# B = [i for i in range(1, len(A) + 1)] # 검증용 리스트
#
# A.sort()
# print('A',A)
# index_point = len(A)//2
# print(index_point)
# print(A[:index_point])
# print(A[index_point:])
# input()
#
#
# if len(A) > 0:
#     for i in range(1, len(A)+1):
#         if i != A[i-1]:
#             print(i)
#             break
#         elif A == B:
#             print(A[-1] + 1)
#             break
# else:
#     print(1)

# print(solution_7(A))

def 정수판별():
    if math.sqrt(4) == 2:
        print('true')

    if float(math.sqrt(4)).is_integer():
        print('True')

    print(isinstance(4.0, int))
    if 4.0 == 4:
        print('True')


def 정규표현식활용():
    my_string = "1a2b3c4d123"
    my_string = re.sub(r'[^0-9]', '', my_string)
    print(my_string)
    answer = sum(map(int, (my_string)))

    print(answer)


# def 최댓값_만들기(1):

# numbers = sorted([1, 2, 3, 4, 5], reverse=True)


numbers = [1, 2, 3, 4, 5]


def multiple(x):
    return x * 2


def 배열2배(numbers):
    answer = list(map(lambda n: n * 2, numbers))
    return answer


def 배열유사도검사():
    s1 = ["a", "b", "c"]
    s2 = ["com", "b", "d", "p", "c"]
    answer = len(set(s1).intersection(set(s2)))
    return len(set(s1) & set(s2))


def 피자나눠먹기_3():
    slice = 7
    n = 10
    result = math.ceil(n / slice)
    return result


def 문자열안에문자열(string1, string2):
    # a = re.compile(string2)
    # if a.search(string1):
    #     return 1
    # else:
    #     return 2

    return 1 + int(string2 not in string1)


def 삼각형만들기():
    sides = [1, 2, 3]

    if sum(sides) - (max(sides) * 2) > 0:
        print(1)


def 특정배수만고르기():
    n = 3
    numlist = [4, 5, 6, 7, 8, 9, 10, 11, 12]
    answer = list(filter(lambda x: x if x % n == 0 else None, numlist))


def 아이스아메리카노():
    money = 15000
    print(money // 5500, money % 5500)


def 모음제거():
    my_string = 'nice to meet you'
    a = re.sub(r'[aeiou]', '', my_string)
    print(a)


def 짝수는싫어요():
    n = 10
    result = [i for i in range(1, n + 1) if i % 2 != 0]

    print(result)


def 약수구하기():
    n = 9
    i = 1
    data_list = list()
    result = list()
    while i < math.sqrt(n) + 1:

        if n % i == 0:
            data_list.append(i)
        i += 1
    print('data_list', data_list)

    if sum(data_list) == 1:
        print(data_list + [n])
    else:
        for i in data_list:
            result.append(n // i)

    print(sorted(list(set(data_list + result))))


def 개미군단():
    attack = [5, 3, 1]
    hp = 999
    result = list()

    for i in attack:
        a = hp // i
        hp -= a * i
        result.append(a)

    print(sum(result))


def 소문자가싫어():
    print(''.join(sorted('BdsadadB'.lower())))


def 야숫자어딨어():
    num = 29183
    k = 1

    print(int(str(num).index(str(k))) + 1 if str(k) in str(num) else -1)


def 저는말을잘못해요():
    my_string = "hello"
    n = 3

    print(''.join(list(map(lambda x: x * n, my_string))))


def 옷가게할인():
    price = 580000
    if price >= 500000:
        return math.floor(price * 0.8)
    if price >= 300000:
        return math.floor(price * 0.9)
    if price >= 100000:
        return math.floor(price * 0.95)
    return price


def 문자열을바꿔보까():
    my_string = list('hello')
    num1 = 1
    num2 = 2

    [my_string[num1], my_string[num2]] = [my_string[num2], my_string[num1]]

    print(''.join(my_string))


def 삼육구():
    check_list = [3, 6, 9]
    count = 0
    order = 00000
    for i in str(order).replace('0', ''):
        if int(i) % 3 == 0:
            count += 1
    return count


def 대소문자반대로():
    my_string = 'cccCCC'

    result = str()

    for i in my_string:
        if i.isupper():
            result += i.lower()
        else:
            result += i.upper()
    print(result)


def 가위바위보하자():
    model = {'2': '0', '0': '5', '5': '2'}
    rsp = '205'
    answer = str()

    answer += ''.join(model[i] for i in rsp)
    return answer

    # for i in rsp:
    #     if not int(i):
    #         answer += '5'
    #     else:
    #         answer += '2' if int(i)%2 else '0'
    #
    # return answer


def 중앙값찾기():
    data = [1, 2, 7, 10, 11]
    data.sort()

    print(data[int(len(data) / 2)])


def 문자열을정렬하자():
    my_string = 'hi12392'
    a = re.sub(r'[^0-9]', '', "hi12392")
    a = map(int, (list(a)))
    answer = map(int, list(re.sub(r'[^0-9]', '', my_string)))
    print(sorted(answer))


def 외계행성이래():
    age = 51
    answer = str()
    for i in str(age):
        answer += chr(int(i) + ord('a'))
    return answer


def 밀어내기_당겨오기():
    numbers = [4, 455, 6, 4, -1, 45, 6]

    print(numbers[1:] + [numbers[0]])
    numbers = [1, 2, 3]
    print([numbers[-1]] + numbers[:-1])


def 박스안에주사위넣기():
    box = [10, 8, 6]
    n = 3
    result = 1
    for i in box:
        result *= i // n

    print(result)


def 칠의성애자():
    data_list = [7, 77, 17]

    for i in data_list:
        len(re.sub(r'[^7]', '', str(i)))


# print(ord(my_string[0]))

def 최대곱을구해보자():
    numbers = [1, 2, -3, 4, -5]
    # numbers = [10, 20, 30, 5, 5, 20, 5]
    numbers.sort()

    if numbers[0] * numbers[1] > max(numbers) * numbers[-2]:
        print(numbers[0] * numbers[1])
    else:
        print(max(numbers) * numbers[-2])


def 피자를잘라라():
    n = 12
    i = 1
    while True:
        if i % n == 0 and i % 6 == 0:
            print(i / 6)
            break
        i += 1


def 배열을생성해라():
    # num_list = [1, 2, 3, 4, 5, 6, 7, 8]
    num_list = [100, 95, 2, 4, 5, 6, 18, 33, 948]
    n = 3

    result_list = list()

    i = 0
    while i < len(num_list):
        result_list.append(num_list[i:n + i])
        i += n


def A로B만들기():
    before = "olleh"
    after = 'hello'

    if sorted(list(before)) != sorted(list(after)):
        return 0
    else:
        return 1


def 순서유지_중복제거():
    my_string = "people"

    result = list(dict.fromkeys(my_string))

    return ''.join(result)


def 합성수를찾아라(n: int):
    prime_flag = [0] * (n + 1)
    print(prime_flag)

    for i in range(2, int(math.sqrt(n)) + 1):
        if prime_flag[i] == False:
            j = 2
            while i * j <= n:
                prime_flag[i * j] = 1
                j += 1

    # print([i for i in range(2, n+1) if prime_flag[i]])

    return sum(prime_flag)


# print(합성수를찾아라(4))

def 좀더직관적인합성수찾기(n: int):
    prime_flag = [1] * (n + 1)  # 0을 포함한 n길이만큼의 배열 생성 후 소수로 간주처리

    for i in range(2, int(math.sqrt(n)) + 1):  # 최대 약수는 n의 제곱근보다 작을 수 밖에 없음
        if prime_flag[i] == True:  # i가 소수일 경우
            for j in range(i + i, n, i):  # 모든 배수를 False 처리
                prime_flag[j] = 0

    print(prime_flag)
    result = [i for i in range(2, n + 1) if prime_flag[i] == True]

    return result


# print(좀더직관적인합성수찾기(10))

def 합성수찾아보기(n: int):
    prime_flag = [0] * (n + 1)
    m = math.sqrt(n)

    for i in range(2, int(m) + 1):
        if prime_flag[i] == 0:
            for j in range(i + i, n + 1, i):
                prime_flag[j] = 1

    return sum(prime_flag)


def 특정단위로_배열잘라보리기():
    my_str = "abc1Addfggg4556b"
    n = 6

    result_list = list()

    i = 0
    while i < len(my_str):
        result_list.append(my_str[i:i + n])
        i += n

    print(result_list)


def 한번만등장한문자는(s):
    answer = str()
    check = sorted(list(set(s)))

    for i in check:
        if s.count(i) == 1:
            answer += i
    return answer


def 모스부호_1(letter: str):
    morse = {
        '.-': 'a', '-...': 'b', '-.-.': 'c', '-..': 'd', '.': 'e', '..-.': 'f',
        '--.': 'g', '....': 'h', '..': 'i', '.---': 'j', '-.-': 'k', '.-..': 'l',
        '--': 'm', '-.': 'n', '---': 'o', '.--.': 'p', '--.-': 'q', '.-.': 'r',
        '...': 's', '-': 't', '..-': 'u', '...-': 'v', '.--': 'w', '-..-': 'x',
        '-.--': 'y', '--..': 'z'
    }

    decode = letter.split(' ')
    answer = str()
    for i in decode:
        answer += morse[i]

    return answer


def 종이자르기(m, n):
    if m >= 2:
        a = m // 1 - 1
        b = (n - a) * m
        return b + 1
    elif n >= 2 and m == 1:
        a = n // 1 - 1
        b = (m - a) * n
        return b + 1
        print(1)
    else:
        return 0

    return m * n - 1


def k의갯수(i, j, k):
    count = 0
    for i in range(i, j + 1):
        if str(k) in str(i):
            a = str(i).count(str(k))
            count += a
    return count


# print(k의갯수(10, 50, 5))


def 팩토리얼(n):
    if n <= 1:
        return 1
    return n * 팩토리얼(n - 1)


def 팩토리얼_찾기():
    # result = [팩토리얼(i) for i in range(1, 11)]
    # print(result)
    # n = 1
    # i = 0
    # while True:
    #     if n < result[i]:
    #         print(i)
    #         break
    #     elif n == result[i]:
    #         print(i+1)
    #         break
    #     i += 1

    print(math.factorial(10))


def 가까운수(array, n):
    result = sorted(array + [n])
    point = result.index(n)
    if result.index(n) != 0 and max(result) != n:
        a = max(result[point - 1: point + 2])
        b = min(result[point - 1: point + 2])
        if abs(n - b) <= abs(n - a):
            return b
        else:
            return a
    elif max(result) == n:
        return result[-2]
    elif min(result) == n:
        return result[1]


array_list = [3, 12, 12, 28]
n = 20


def 좀더효율적인가까운수(array_list, n):
    array_list.sort()  # 비정렬 상태이므로 높은 수가 낮은 수보다 앞에 있을 수 있다는 점을 고려한 정렬
    result = [abs(i - n) for i in array_list]
    return array_list[result.index(min(result))]


def 이진수덧셈():
    bin1 = '0b10'
    bin2 = '11'
    print(format(int(bin1, 2) + int(bin2, 2), 'b'))


def 공던지기게임():
    k = 3
    # 2 5 3
    # numbers = [1, 2, 3, 4]
    # numbers = [1, 2, 3, 4, 5, 6]
    numbers = [1, 2, 3]

    result = numbers * k
    print(result)
    print(result[::2][k - 1])

def 외계어사전():


    # spell = ["p", "o", "s"]
    spell = ["z", "d", "x"]
    # dic = 	["sod", "eocd", "qixm", "adio", "soo"]
    dic = 	["def", "dww", "dzx", "loveaw"]

    spell.sort()
    check = ''.join(spell)
    dic = map(sorted, dic)

    print(check)
    for i in dic:
        # ''.i)
        if check == ''.join(i):
            print('ㄷㅇ일')


def 삐뽀삐뽀진료순서():
    emergency = [1, 2, 3, 4, 5, 6, 7]
    check = dict()
    answer = list()

    for i, data in enumerate(sorted(emergency)[::-1]):
        check[data] = i + 1

    for i in emergency:
        answer.append(check[i])

    return answer

def 문자열을밀자():
    a = 'hello'
    b = 'ohell'

    result = list()
    for i in range(1, len(a)):
        result.append(a[-i:] + a[:len(a) - i])
    result.insert(0, a)
    if b in result:
        return result.index(b)
    else:
        return -1
# print(팩토리얼())


def 소인수분해(n):
    result_list = list()
    # if n == 0:
    #     return '0'

    for i in range(2, int(math.sqrt(n)+1)):
        while n % i ==0:
            result_list.append(i)
            n /= i
    if n >=2:
        result_list.append(int(n))

    return sorted(list(set(result_list)))

# for i in range(100):
#     print(소인수분해(i))


def 영어가싫어요(numbers:str):
    convert_list = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i, number in enumerate(convert_list):
        if not numbers.isdigit():
            numbers = re.sub(number, str(i), numbers)
    return int(numbers)


def 영어가싫어요_2(numbers:str): # 좀더 짧게
    for num, eng in enumerate(["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
        numbers = numbers.replace(eng, str(num))
    return int(numbers)

def 숨어있는_숫자의_덧셈2(my_string:str):
    my_string = re.sub(r'[^0-9]',  ' ', my_string)
    sum_list = my_string.split(' ')
    sum_list = list(map(int,list(filter(None, sum_list))))
    return sum(sum_list)


def 숨어있는_숫자의_덧셈2효율(my_string:str):

    return sum([int(i) for i in re.findall(r'[0-9]+', my_string)])

def 다음에올숫자(common:list): # 등차, 등비 수열
    a, b, c, d = common[-1], common[-2], common[0], common[1]
    if a - b == d - c:
        return common[-1] + (common[1] - common[0])
    else:
        return common[-1] * (common[1] / common[0])

def 구슬을나누는경우의수(balls, share):
    n = math.factorial(balls)
    m = math.factorial(share)
    result = n / ((math.factorial(balls-share)) * m)
    return result
    # return math.comb(balls, share) # 걍 수열 메소드 쓰는 방법

# print(math.factorial(5))
# print(구슬을나누는경우의수(5, 3))

my_string = "3 + 4 + 5 + 6"

a = '3'
b = '4'
c = '+'

def 문자열_계산하기(my_string:str):

    data = my_string.split(' ')
    data = list(filter(None, data))

    n = int(data[0]) + int(data[2]) if data[1] == '+' else int(data[0]) - int(data[2])
    calc = [data[i:i+2:] for i in range(3, len(data), 2)]

    if len(data) > 3:
        for i in calc:
            if i[0] == '+':
                n += int(i[1])
            else:
                n -= int(i[1])
        return n
    else:
        return n

# print(문자열_계산하기('3 + 4'))

def 문자열_계산하기_효율(my_string): # 그냥 list comprehension 하면서 문자뒤에 - 붙이면 int 형변환 가능
    test = [int(i) for i in my_string.replace(' - ', ' + -').split(' + ')]
    print(test)
    return sum(int(i) for i in my_string.replace(' - ', ' + -').split(' + '))

# print(문자열_계산하기_효율('3 - 5'))

def 유한소수_판별하기(a:int, b:int):
    result_list = list()

    gcd = math.gcd(a, b)
    n = a/b
    c, d = a/gcd, b/gcd

    for i in range(2, int(math.sqrt(d)+1)):
        while d % i == 0:
            result_list.append(i)
            d /= i
    if d >= 2:
        result_list.append(int(d))
    result_list = list(set(result_list))

    if 2 and 5 in result_list[0:2] or sum(result_list) == 2 or n.is_integer():
        return 1
    else:
        return 2


    return 1 if a/b * 1000 % 1 == 0 else 2 # 숏코딩 하는 법

def 캐릭터의_좌표(keyinput:list, board:list):

    result = [0, 0]
    x, y = (board[0]-1)//2, (board[1]-1)//2
    arrows = {'up': '1,1', 'down': '1,-1', 'left': '0,-1', 'right': '0,1'}
    x_y = {'up' : y, 'down': y, 'left': x, 'right': x}

    for i in keyinput:
        a = int(arrows[i].split(',')[0])
        b = int(arrows[i].split(',')[1])

        if i == 'down' or i == 'left':
            result[a] +=  b if  result[a] -1 >= -x_y[i] else 0

        elif i == 'up' or i == 'right':
            result[a] += b if result[a] +1 <= x_y[i] else 0
    return result

def 연속된_수의_합(num:int, total:int) -> list: # 배열 생성후 좌우 이동
    print(num, total)
    compare1, compare2 = [i for i in range(0, num)], [i for i in range(1, num+1)]
    n = (total - sum(compare1)) / (sum(compare2) - sum(compare1))
    return list(map(lambda x:int(x+n) , compare1))
    # print(compare1)
    # print('sum(compare2) - sum(compare1)', sum(compare2) - sum(compare1))
    # print('sum(compare1)',sum(compare1))
    # print('total - sum(compare1)', total - sum(compare1))
    # print('total - (sum(compare2) - sum(compare1))', total - (sum(compare2) - sum(compare1)))

def 컨트롤제트(s:str):
    s = s.split(' ' )
    i = 0
    while True:
        if s[i] == 'Z':
            s.pop(i)
            s.pop(i-1)
            i = 0
        i += 1
        if 'Z' not in s:
            return sum(map(int,s))

def 등수_매기기(score:list):
    answer = list()
    compare1 = list()

    for i in score:
        compare1.append(sum(i)/2)
    compare2 = sorted(compare1, reverse=True)
    for i in compare1:
        answer.append(compare2.index(i)+1)

    return answer

def 등수_매기기_효율(score:list): # 딕셔너리를 이용한 방법 더 직관적
    rank = sorted([sum(s) / 2 for s in score], reverse=True)
    rankDict = {}
    for i, r in enumerate(rank):
        if r not in rankDict.keys():
            rankDict[r] = i + 1

    return [rankDict[sum(s) / 2] for s in score]

def 특이한정렬(numlist:list, n:int):
    sort_dict = dict()
    result = list()
    numlist.sort()
    for i, data in enumerate(numlist):
        if data not in sort_dict.keys():
            sort_dict[data] = abs(n-data)

    d1 = sorted(sort_dict.items(), key=operator.itemgetter(1), reverse=True)
    for key, value in d1[::-1]:
        result.append(key)

    return result

def 특이한정렬_효율(numlist:list, n:int):
    answer = sorted(numlist, key=lambda x: (abs(x-n), n-x))
    return answer


def 직사각형_넓이(dots:list):
    x = [i[0] for i in dots]
    y = [i[1] for i in dots]

    # x_min, x_max = min(x), max(x)
    # y_min, y_max = min(y), max(y)

    # width = x_min - x_max
    # height = y_min - y_max

    width = min(x) - max(x)
    height = min(y) - max(y)

    return width * height

def 로그인성공(id_pw, db):
    db = dict(db)
    if db.get(id_pw[0]):
        db_pw = db.get(id_pw[0])
        return 'login' if db_pw == id_pw[1] else 'wrong pw'
    else:
        return 'fail'

def 삼각형의완성조건_2(sides:list):
    a, b, c = max(sides), min(sides), sum(sides)
    return (c - a - 1) + (a - (a - b)) # 나머지 한변, 가장 긴변이 a 일 경우

def 주문(coupon):
    if coupon < 10:
        return 0
    else:
        service = math.floor(coupon/10)
        return service + 주문(service + (coupon % 10))

def 치킨쿠폰(chicken:int):
    return 주문(chicken)

def 치킨쿠폰2(chicken:int):

    return (max(chicken,1)-1)//9

def 최빈값구하기(array:list):
    check_dict = dict()
    for i in array:
        if i in check_dict.keys():
            check_dict[i] += 1
        else:
            check_dict[i] = 1
    result = sorted(check_dict.items(), key=operator.itemgetter(1), reverse=True)
    if len(result) == 1 or result[0][1] != result[1][1]:
        return result[0][0]
    else:
        return -1


# print(최빈값구하기([1]))
array = [1, 2, 3, 3, 3, 4, 4, 4, 4]

def 최빈값구하기_효율(array:list):

    while len(array) != 0:
        for i, a in enumerate(set(array)):
            array.remove(a)
        if i == 0:
            return a
    return -1

#
# print(108//10)
# print(10//10)

def 저주의_숫자_3(n:int):
    compare = 0
    result = list()

    i = 0
    while compare<n:
        i += 1
        if i % 3 and '3' not in str(i):
            result.append(i)
            compare += 1
    return result[n-1]

# for i in range(1, 41):
#     print(저주의_숫자_3(i))

def OX퀴즈(quiz):
    result = list()
    for i in quiz:
        a = i.split('=')[0][:-1].split(' ')
        b = i.split('=')[1][1:]
        check = ['+', '-']
        a = list(map(lambda x: int(x) if x not in check else x, a))
        if a[1] == '+':
            x = a[0] + a[2]
        else:
            x = a[0] - a[2]
        # opt = str()
        # for i in a:
        #     if isinstance(i, int):
        #         x += int(opt+str(i))
        #     else:
        #         opt = i

        result.append('O') if x == int(b) else result.append('X')
    return result

# print(OX퀴즈(["3 - 4 = -3", "5 + 6 = 11"]))
# print(OX퀴즈(["19 - 6 = 13", "5 + 66 = 71", "5 - 15 = 63", "3 - 1 = 2"]))
# print(OX퀴즈(["-3 + -3 = 5"]))


# print(dots[0][0] - dots[1][0])
# print(dots[0][0] - dots[2][0])

# print(캐릭터의_좌표(["left", "right", "up", "right", "right"], [11, 11]))
# print(캐릭터의_좌표(["down", "down", "down", "down", "down"], [7, 9]))
# print(캐릭터의_좌표( ["left", "left", "left", "right"], [3, 3]))
# print(캐릭터의_좌표(["up", "up", "up", "down"], [3, 3]))

def 다항식_더하기(polynomial:str):
    polynomial = polynomial.split(' ')
    polynomial = list(map(lambda x: '1x' if x == 'x' else x, polynomial))
    result_dict = {'x' : 0}
    constant = list()

    for i in polynomial:
        if 'x' in i:
            result_dict[i[1]] += int(i[0])
        elif i.isdigit():
            constant.append(int(i))
    x = str(result_dict.get('x'))+'x'

    if int(x[0]) == 1:
        x = 'x'

    if sum(constant) != 0 and result_dict.get('x') != 0:
        return x + ' + ' + str(sum(constant))
    elif result_dict.get('x') == 0:
        return sum(constant)
    elif sum(constant) == 0:
        return x

def 다항식_더하기_2(polynomial):

    x = 0
    const = 0
    for i in polynomial.split("+"):
        i = i.strip()
        if 'x' in i:
            i = i.replace("x","")
            if i.isdigit():
                x += int(i)
            else:
                x += 1

        elif i.isdigit():
            const += int(i)

    if x > 1:
        return f'{x}x + {const}' if const != 0 else f'{x}x'
    if x == 1:
        return f'x + {const}' if const != 0 else f'x'
    if x == 0:
        return str(const)



# print(다항식_더하기_2("3x + 7 + x"))
# print(다항식_더하기_2("x + x + x"))
# print(다항식_더하기_2("1 + 1 + x"))
# print(다항식_더하기_2("1 + 1"))
# print(다항식_더하기_2("1 + 1"))
# print(다항식_더하기_2("x"))

def 최소공배수(a, b):
    return int((a * b) / math.gcd(a, b))

def 분수의_덧셈(denum1, num1, denum2, num2):

    result = [int, int]
    lcm = 최소공배수(num1, num2)
    a, b = lcm/num1, lcm/num2
    result[0] = (int(denum1 * a + denum2 * b))
    result[1] = lcm
    gcd = math.gcd(result[0], result[1])
    while gcd > 1:
        result[0] /= gcd
        result[1] /= gcd
        gcd = int(math.gcd(int(result[0]), int(result[1])))

    return list(map(int, result))

def 분수의_덧셈2(denum1, num1, denum2, num2):
    gcd = math.gcd(num1, num2)
    lcm = math.lcm(num1, num2)

    denum1 = (lcm/num1) * denum1
    denum2 = (lcm/num2) * denum2
    c = int(denum1+denum2)

    if math.gcd(c, lcm) != 1:
        x = int(c/int(math.gcd(c, lcm)))
        y = int(lcm/int(math.gcd(c, lcm)))
        return [x, y]
    return [c, lcm]

def 분수의_덧셈_효율(denum1, num1, denum2, num2):
    denum = denum1 * num2 + denum2 * num1
    num = num1 * num2
    gcd = math.gcd(denum, num)
    return [denum//gcd, num//gcd]
    
# random_test = list()
# for i in range(50):
#     random.randint(1, 999)
#     random_test.append([random.randint(1, 100),random.randint(101, 300),random.randint(301, 600),random.randint(601, 900)])
#
# for i in random_test:
#     print('a:', 분수의_덧셈(i[0], i[1], i[2], i[3]), 'b:', 분수의_덧셈2(i[0], i[1], i[2], i[3]))
#     print()

# print(분수의_덧셈(1, 2, 3, 4))
# print(분수의_덧셈(9, 2, 1, 3))
# print(분수의_덧셈(7, 2, 10, 20))

def 안전지대(board:list):
    boom_coord = list()
    count = 0

    for i, data in enumerate(board):
        if 1 in data:
            x = list(filter(lambda x: data[x] == 1, range(len(data))))
            x_y = [[i, data] for data in x]
            boom_coord += x_y

    for i in boom_coord:
        try:
            if i[0] == 0:
                board[i[0]][i[1]:i[1] + 2] = list(map(lambda x: 1, board[i[0]][i[1]:i[1] + 2]))
                board[i[0]+1][i[1]:i[1] + 2] = list(map(lambda x: 1, board[i[0]+1][i[1]:i[1] + 2]))
            if i[1] == 0:
                board[i[0]-1][0:i[1] + 2] = list(map(lambda x: 1, board[i[0]-1][0:i[1] + 2]))
                board[i[0]][0:i[1] + 2] = list(map(lambda x: 1, board[i[0]][0:i[1] + 2]))
                board[i[0]+1][0:i[1] + 2] = list(map(lambda x: 1, board[i[0]+1][0:i[1] + 2]))
            if i[0] >= 1:
                board[i[0]-1][i[1]-1:i[1]+2] = list(map(lambda x: 1, board[i[0]-1][i[1]-1:i[1]+2]))
            board[i[0]][i[1]-1:i[1]+2] = list(map(lambda x: 1, board[i[0]][i[1]-1:i[1]+2]))
            board[i[0]+1][i[1]-1:i[1]+2] = list(map(lambda x: 1, board[i[0]+1][i[1]-1:i[1]+2]))
        except:
            pass
    for i in board:
        count += sum(i)

    return (len(board)**2) - count

def 안전지대_효율1(board):
    answer = 0

    for col in range(len(board)):
        for row in range(len(board[col])):
            if board[row][col] == 1:
                for j in range(max(col-1,0),min(col+2,len(board))):
                    for i in range(max(row-1,0),min(row+2,len(board))):
                        if board[i][j] == 1:
                            continue
                        board[i][j] = -1
    for i in board:
        answer += i.count(0)

    return answer

def 안전지대_효율2(board): # 개인적으로 제일 간결하고 직관적인 라인
    n = len(board)
    danger = set()
    for i, row in enumerate(board):
        for j, x in enumerate(row):
            if not x:
                continue
            danger.update((i+di, j+dj) for di in [-1,0,1] for dj in [-1, 0, 1])
    return n*n - sum(0 <= i < n and 0 <= j < n for i, j in danger)

# print(안전지대([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]))
# print(안전지대([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0]]))
# print(안전지대([[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]))
# print(안전지대([[0, 0, 0, 1, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]))

def 겹치는_선분의_길이(lines):

    min_v , max_v= min(sum(lines, list())), max(sum(lines, list()))
    flat_v = int(abs(min_v))

    for i, line in enumerate(lines):
        lines[i].sort()
    #     lines[i] = list(map(lambda x : x+flat_v, line))

    result_dict =dict()
    # for i in

    # result = list(itertools.combinations(lines, 2))

    result = list()
    count = 0
    for i in lines:
        for j in range(i[0], i[1]):
            if j not in result:
                result.append(j)
            else:
                result.pop(result.index(j))
                count += 1

    return count

    # s1, s2, s3 = set(lines[0]), set(lines[1]), set(lines[2])
    # for i, data in enumerate(result):
    #     lines[i] = list(result[i])
    #     s1 = set(result[i][0])
    #     s2 = set(result[i][1])
    #     if len(list(s1 & s2)) >= 2:
    #         result[i] = list(s1 & s2)
    #     else:
    #         result[i] = [None]
    # result = list(filter(None,list(set(sum(result, list())))))
    # print('result:', result)
    #
    # return len(result)

    # result += list(s1 & s2)
    # result += list(s1 & s3)
    # result += list(s2 & s3)
    # if len(list(filter(None,list(set(result))))) > 0:
    #     return len(list(filter(None,list(set(result))))) + 1
    # else:
    #     return 0
    # print(len(list(filter(None,list(set(result))))))
    # if len(list(set(result))) > 1:
    #     return len(list(set(result)))


# print(겹치는_선분의_길이([[0, 1], [2, 5], [3, 9]]))
# print('---')
# print(겹치는_선분의_길이([[-1, 1], [1, 3], [3, 9]]))
# print('---')
# print(겹치는_선분의_길이([[-1, 1], [0, 2], [0, 2]]))
# print(겹치는_선분의_길이([[0, 5], [3, 9], [1, 10]]))
# print('---')
# print(겹치는_선분의_길이([[3, 7], [2, 3], [1, 10]]))
# print(겹치는_선분의_길이([[0, -1], [0, 1], [1, 2]]))
# print(겹치는_선분의_길이([[3,5], [3,5], [3,5]]))

def 겹치는_선분의_길이_효율(lines):
    sets = [set(range(min(l), max(l))) for l in lines]
    print(sets)
    print(sets[0] & sets[1] | sets[0] & sets[2] | sets[1] & sets[2])
    return len(sets[0] & sets[1] | sets[0] & sets[2] | sets[1] & sets[2])

# print(겹치는_선분의_길이_효율([[0, 5], [3, 9], [1, 10]]))


def 기울기(xy : list):
    slope = float((xy[3] - xy[1]) / (xy[2] - xy[0]))
    return slope

def 평행(dots:list):
    a = list(itertools.combinations(dots, 2))
    result = list()
    for i in a:
        result.append(기울기(sum(i,list())))

    return 1 if [i for i in result if Counter(result).get(i) >= 2] else 0



print(평행([[1, 4], [9, 2], [3, 8], [11, 6]]))
print(평행([[3, 5], [4, 1], [2, 4], [5, 10]]))


# a = list(itertools.combinations([[1, 4], [9, 2], [3, 8], [11, 6]], 2))
# a = list(itertools.combinations([[3, 5], [4, 1], [2, 4], [5, 10]], 2))
# print(a)
# for i in a:
#     plt.plot((i[0][0], i[1][0]), (i[0][1], i[1][1]))

# plt.show()
#
# plt.plot((1, 3), [4, 8],color="green")
# plt.plot([9, 11], [2, 6],color="red")

# plt.plot((3, 5), [5, 10],color="green")
# plt.plot([3, 5], [3, 8],color="red")
# plt.show()




# print(안전지대([[0, 0], [1, 0]]))

# print(before)
# print(after)
# return before[::-1]

# print(A로B만들기())

# for i in range(len(result_list)):
#     for j in range(n):
#         answer_list.append(


# for i in range(int(len(num_list)/n)):
#
#     n += n

# print(result_list)

# print(삼육구())
# print(list(str(order)))
# print(price//100000)

# for i in result:
#     print(n % i)


# s3 = set(s1)&set(s2)
# print(s3)
# for i in s1:
#     if i in s2:
#         print('true')

# print(len(set(s1).intersection(set(s2))))

# result = len(filter(lambda )

# print(result)


def 놀이기구(price:int, money:int, count:int):
    a = sum([i for i in range(price, price * count + 1, price)]) - money
    return 0 if a <= 0 else a
