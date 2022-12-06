'''
파이썬의 내장 정렬 메소드
sorted() : 정렬 작업후 원본을 건드리지 않고 결과 값 반환
sort() : 리스트 원본을 직접 수정, 결과 값을 따로 반환하지 않음
기본적으로 삽입 + 병합을 합친 Tim sort 알고리즘이 표준으로 채택되어 있음
정렬 순서는 기본적으로 사전 순서를 따름

reference
1. https://velog.io/@toezilla/1D1Q-파이썬의-sort-내장함수는-어떤-정렬-알고리즘을-이용할까
2. https://leffept.tistory.com/432
3. https://gmlwjd9405.github.io/2018/05/06/algorithm-insertion-sort.html
'''

L = ['abcd', 'uni', 'babymon']
L.sort(key = lambda x: len(x))
print(L)


# 대표적인 탐색 알고리즘의 종류
def linear_search(L, x): #1. 선형 탐색: 인덱스의 순서대로 선형적으로 탐색 -> O(n) 의 시간 복잡도
    i = 0
    while i < len(L) and L[i] != x:
        i += 1
    if i < len(L):
        return i
    else:
        return -1

# print(linear_search([1, 5, 3, 6], 6))

# 2. 이진 탐색: 한 번 비교가 일어날 때마다 리스트가 절반으로 줄어듬 -> O(log n) 의 시간 복잡도
def binary_search(L, x):
    lower = 0
    upper = len(L) -1
    idx = -1

    while lower <= upper:
        middle = (lower + upper) // 2
        if L[middle] == x:
            idx = middle
            return idx
        elif L[middle] < x:
            lower = middle + 1
        else:
            upper = middle - 1

    return idx

print(binary_search([1, 2, 3], 3))
print(binary_search([2, 5, 7, 9, 11], 4))
L = [i for i in range(100000000)]
print(binary_search(L, 2))