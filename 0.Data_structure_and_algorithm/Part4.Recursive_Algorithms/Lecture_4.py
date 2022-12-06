'''
재귀 함수 (Recursive Functions) 란 ?
하나의 함수에서 자신을 재호출하여 작업을 수행하는 함수
'''

'''
1. 이진 트리 (binary trees)
하위 좌측 노드는 상위 (루트) 노드보다 작고, 하위 우측 노드는 상위 노드보다 큰 트리 구조가 있을 때,
하위 노드에도 위 조건을 모든 노드에 적용 한다면 ? -> 트리 탐색으로 적용 가능
'''


# 대표적인 재귀 함수의 예제
def recursive_func(n): # O(n)
    if n <= 1: # 재귀 함수는 호출의 종결 조건이 매우 중요하다
        return 1
    return n + recursive_func(n-1)


# print(recursive_func(4))


# 모든 재귀 함수는 그와 대칭 되는 반복적인 알고리즘 (Counter Part) 이 존재한다.
def iterative_func(n): # O(n)
    sum_value = 0
    while n >= 0:
        sum_value += n
        n -= 1
    return sum_value


# print(iterative_func(4))


# 시간 복잡도 측면이 아닌 효율적인 측면에서 보면 iterative한 알고리즘이 더 나을 수도 있다
def constant_func(n): # O(1)
    return n * (n+1) // 2
# 위와 같이 똑같은 리턴 값을 가져도 상수 시간내에 해결 할 수 있는 경우도 있다. -> 무조건적인 재귀 구현이 좋은 것은 아님


# print(constant_func(4))


# n >= 2
def recursive_fibonacci(n:int) -> int:
    if n <= 1:
        return n
    return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)


# print(recursive_fibonacci(5))


def iterative_fibonacci(n):
    # answer = list()
    # a, b = 1, 1
    # for i in range(n):
    #     answer.append(a)
    #     a, b = b, a + b
    # return a

# while문 구현
    cnt = 0
    a, b = 0, 1 # a : 현재값, b : 다음값
    while cnt < n:
        a, b = b, a + b
        cnt += 1
    return a

# for문 구현
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

print(iterative_fibonacci(5))