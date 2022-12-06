
'''
Python 에서는 배열 (Arrays)이 따로 존재하지 않고 리스트 (List) 가 그 역할을 대체하게 된다.
다른 프로그래밍 언어에서의 배열보다 조금 더 동적인 데이터 타입이다.
'''

L = ['babymon', 'uni', 'dao', 'puppy']
# print(isinstance(L.pop(), int))
# print(L)

'''
리스트 내의 기본 메소드인
append (리스트 마지막 인덱스에 삽입)
pop (리스트 마지막 원소 삭제 후 반환)
은 상수 시간 O(1)의 시간복잡도가 소요된다.

반면
insert (삽입값, 인덱스를 매개변수로 받아 리스트 수정)
del (인덱스를 지정하여 삭제)
는 배열내 삽입 및 삭제 후 재정렬을 하므로 리스트의 길이에 비례한 시간 즉 선형 시간 O(n)이 소요된다.
'''

# 실습 문제
def 정렬된_리스트에_원소_삽입(L, x) -> list:
    # L.append(x)
    # L.sort()
    # return L
    # 출제 의도대로 풀어보기
    for idx, data in enumerate(L):
        print(data)
        if x <= data:
            L.insert(idx, x)
            return L

# print(정렬된_리스트에_원소_삽입( [20, 37, 58, 72, 91] , 65))

def 리스트에서_원소_찾아내기(L:list, x:int) -> list:
    answer = list()
    # cnt = L.count(x)
    # idx = 0
    # while cnt != 0:
    #     if x in L[idx:]:
    #         answer.append(L[idx:].index(x) + idx)
    #         cnt -= 1
    #         idx = answer[0] + 1
    #     else:
    #         break

    for idx, data in enumerate(L):
        if data == x:
            answer.append(idx)

    return answer if answer else [-1]

print(리스트에서_원소_찾아내기([64, 72, 83, 72, 54], 72))
print(리스트에서_원소_찾아내기([64, 72, 83, 72, 54], 49))