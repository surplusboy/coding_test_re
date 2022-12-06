import math
# import spacy
# nlp = spacy.load("en_core_web_sm")

# def solution(stack1, stack2, stack3):
#     stack4 = list()
#
#     check_dict = {}
#     check_stack = [stack1, stack2, stack3]
#
#     for i in check_stack:
#         i.sort(reverse=True)
#         stack4.extend(i)
#
#     for i, data in enumerate(check_stack):
#         for j in data:
#             check_dict[j] = i
#
#     stack4.sort(reverse=True)
#
#     result = str()
#
#     for i, data in enumerate(stack4):
#         result += str(check_dict[data] + 1)
#
#     return result
#
# stack1 = [2, 7]
# stack2 = [4, 5]
# stack3 = [1]
#
# stack1 = [10, 20, 30]
# stack2 = [8]
# stack3 = [1]
#
# stack1 = [7]
# stack2 = []
# stack3 = [9]


# print(solution(stack1, stack2, stack3))

a = 'John is old'
b = 'Mark Oldham ate an apple'

# doc = nlp(a)
# def 이름비식별화(string):
#     doc = nlp(string)
#     check_dict = dict()
#
#     for i, token in enumerate(doc):
#         if token.pos_ == 'PROPN':
#             check_dict[token.text] = 'X' * len(token.text)
#         else:
#             check_dict[token.text] = token.text
#     count = 0
#     result = str()
#     for key, value in check_dict.items():
#         if value == 'X'*len(key):
#             result += f'{value}'
#             count += 1
#             if count > 1:
#                 result += 'X'
#                 count = 0
#         else:
#             result += f' {value}'
#             count = 0
#
#     return result
# test = ['Mark Oldham ate an apple', 'John is old']
# for i in test:
#     print(이름비식별화(i))
# # for token in doc2:
# #     print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_, token.shape_, token.is_alpha, token.is_stop)
#
# S = 'aabcba'
# C = [1, 3, 2]
# check_list = list(S)


# check_list.insert(1, C)

# for idx, i in enumerate(range(10000, 359000, 1000)):
#     a = i * 0.03 # 1000
#     b = i + a # 1300
#     c = b / 5990 # 1300 / 5990
#
# # if format(c, ".2f").split(".")[1][0] == '0':
#     print(f'현금화 금액 : {i} 실결제 : {int(b)} 적립횟수 : {format(c, ".2f")} 적립금액 : {990 * round(c)} 차액 : {int(b - i)} 순익 {990 * round(c) - int(b - i)}')
#     # print(f'현금화 금액 : {i} 실결제 : {int(b)} 적립횟수 : {format(c, ".2f")} 적립금액 : {990 * round(c)} 차액 : {int(b - i)} 순익 {990 * round(c) - int(b - i)}')
#
#     if c >= 20:
#         break
#
#     if b >= 359000:
#         break
