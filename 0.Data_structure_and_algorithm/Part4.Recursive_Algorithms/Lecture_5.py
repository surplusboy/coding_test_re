import math
import itertools

# 재귀 알고리즘의 응용

# 간단한 경우의 수의 갯수 구하기

def combi_func(n, m):
    return math.factorial(n) / (math.factorial(m) * math.factorial(n-m))

def recursive_combi(n, m):
    # trivial case
    if n == m or m == 0:
        return 1
    else:
        return recursive_combi(n-1, m) + recursive_combi(n-1, m-1)

# print(combi_func(10, 3))
data = [i for i in range(10)]
# print(len(list((itertools.combinations(data, 3)))))
# print(recursive_combi(10, 3))

test_list = [3, [1, 4, [3, [6, 2], 5], 1, 3], 4]
# print(list(itertools.chain.from_iterable(test_list)))

# 재귀 함수가 효율성 측면에서 무조건적으로 좋은 것은 아니지만 아래와 같은 예시의 경우 좋은 적용 사례가 될 수 있다.
def recursive_unpack(array):
    result = list()
    for i in array:
        if isinstance(i, list):
            result += recursive_unpack(i)
        else:
            result += [i]
    return result
# print(recursive_unpack(test_list))


def hanoi_tower(num:int, from_, by_, to_): # 출발지, 목적지, 나머지 기둥
    if num == 1: # 재귀 탈출 조건
        print('{} -> {}'.format(from_, to_))
        return
    # n 개의 원반을 by를 이용해 from에서 to로 이동
    hanoi_tower(num-1, from_, to_, by_)
    print('{} -> {}'.format(from_, to_))
    # hanoi_tower(num-1, by_, from_, to_)
    hanoi_tower(num-1, by_, from_, to_)
# print(hanoi_tower(2, 'A', 'B', 'C'))

def recursive_binsearch(array:list, x:int, lower:int, upper:int) -> int: # 재귀적 이진 탐색
    # Test Case 1 : array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], x = 7, lower = 0, upper = 10

    if lower > upper: # 분기에 의해 lower 값이 upper 보다 높아지는 경우 = 찾는 값이 없을 경우
        return -1

    mid = (lower + upper) // 2

    if x == array[mid]:
        return mid
    elif x < array[mid]: # mid value 가 target value 보다 높을 경우 오른쪽 구간 재귀 호출
        return recursive_binsearch(array, x, lower, mid - 1)
    else: # mid value 가 target value 보다 낮을 경우 왼쪽 구간 재귀 호출
        return recursive_binsearch(array, x, mid + 1, upper)

# L = [2, 5, 7, 9, 11]
# L = [i for i in range(100000000)]
# print(recursive_binsearch(L, 11, 0, len(L)))