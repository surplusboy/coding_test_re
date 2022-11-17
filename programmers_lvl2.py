import re
from functools import reduce
from collections import deque

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
    return sum(map(lambda x, y: x * y, A,B))

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

print(올바른_괄호_다른코드('()())(()'))
