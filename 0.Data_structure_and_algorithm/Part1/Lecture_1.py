'''
파이썬의 기본적인 Data Type
1. 문자열 (str), 정수 (int), 실수 (float) 등
2. 리스트 (list)
3. 사전 (dict)
4. 순서쌍 (tuple)
5. 집합 (set)
등이 있다.

왜 Data Structure 를 알아야 할까 ? -> 더욱 효과적인 문제 해결을 위하여
'''

# 기본적인 데이터 타입으로의 접근시 비효율적인 예제
import time

n = int(input('Numer of elements ?'))
haystack = [i for i in range(n)]

ts = time.time()
max_value = max(haystack)
elapsed = time.time() - ts

print('Maximum value = {}, Elapse time = {:.2f}'.format(max_value, elapsed))

# n 값이 커질 경우 n 에 비례 하는 만큼의 시간 소요가 요구되는 것을 알 수 있다.

'''Algorithm 이란 ?
사전적 정의 : 어떤 문제를 해결하기 위한 절차, 방법, 명령어들의 집합
프로그래밍 : 주어진 문제의 해결을 위한 자료구조와 연산 방법에 대한 선택
'''

def solution(x):
    return x[0] + x[-1]