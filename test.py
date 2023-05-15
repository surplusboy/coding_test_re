import os
import pandas as pd
import csv
import itertools
from pydantic import BaseModel
from typing import Optional, List
from jose import jwt
from datetime import datetime, timedelta


i = 1

data = [None, 3, 6, 5]

# print(len(L))
left = 2 * i
right = (2 * i) + 1
smallest = i
# vali = [smallest, left, right]
# check = [data[smallest], data[left], data[right]]
# smallest = vali[check.index(max(check))]

# max(L[smallest], L[left], L[right])
# if data[right]:
#     print('true')


# test = []
# print(bool([]))
#
# test = [1,2,3,4,5]
#
# stack = []
# while test:
#     print(test.pop())



# if not not test:
#     print('ture')
# else:
#     print('false')

# L = [[1,2], [2,1], [1,1]]

# L.sort(key = lambda x : (-x[1], x[0]))
# print(L)


def print_ls(path):
    PATH = path

    file_ls = []
    max_depth = 0
    for path, dir, files in os.walk(PATH):
        for file in files:
            current = os.path.join(path, file).replace('\\', '/')
            file_ls.append(current)
            print('/'.join(current.split('/')[4:]))
            # input()

            # if len(current.split('/')) > max_depth:
            #     max_depth = len(current.split('/'))
    # return file_ls

# print(print_ls())

def write_csv(csv_path, max_depth, path):
    PATH = path
    os.chdir(csv_path)
    depth = list(range(0, max_depth, 1))
    with open('folder_data.csv', 'w', newline='', encoding='cp949') as f:
        w = csv.writer(f)
        w.writerow(' '.join(str(e) for e in depth).split())

        for path, dir, files in os.walk(PATH):
            for file in files:
                current = os.path.join(path, file).replace('\\', '/')
                row = os.path.relpath(current, PATH).split(os.sep)
                w.writerow(row)

    df = pd.read_csv('folder_data.csv', error_bad_lines=False, index_col=None,
                     header=0, engine='python', encoding='cp949')

# TL = [1,2,3,4]
# a = itertools.accumulate(TL)
#
# for i in a:
#     print(i)

# a = [i for i in range(11)]
#
# for i in range(0, len(a)-1, 2):
#     print(a[i])


a = 1000
b = ''
# for i in range(a):
#     b += '(진짜 모름'
# b += ')'*a

print(b)

test_dict = {'a': 1, 'b': 2, 'c': 3}

# if test_dict.get('c'):
#     print('true')


# token = {'user_id' : 'test4'}
# print(token.user_id)

class Token(BaseModel):
    user_id: str = 'admin'
    user_name: str = '관리자'
    user_type: Optional[str] = "N"
    exp: str

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(
            minutes=60 * 24 * 8
        )
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7", algorithm="HS256"
    )
    return encoded_jwt


data = {
    "user_id": 'admin',
    "user_name": '관리자',
    "user_type": 'AD',
}
test_token = create_access_token(data)
print(test_token)


# def verify_access_token(token: str):
#     payload = jwt.decode(
#         'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiYWRtaW4iLCJ1c2VyX25hbWUiOiJcdWFkMDBcdWI5YWNcdWM3OTAiLCJ1c2VyX3R5cGUiOiJBRCIsImV4cCI6MTY4MDMyNTQzOH0.5sHwmfdqWQMY3ZKkjn4klXGZBohPZxrczqUKaE_wr54',
#         "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7", "HS256"
#         )
#     token_data = Token(**payload)
#     return token_data
#         if token_data.user_name is None:
#             raise credentials_exception
#     except JWTError:
#         raise credentials_exception
#     # 실제 사용자가 존재하는지 데이터베이스 조회
#     user = get_user(user_id=token_data.user_id)
#     if user is None:
#         raise credentials_exception
#     logger.info("token_data is %s", token_data)
#     return token_data

# decode_test = verify_access_token('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiYWRtaW4iLCJ1c2VyX25hbWUiOiJcdWFkMDBcdWI5YWNcdWM3OTAiLCJ1c2VyX3R5cGUiOiJBRCIsImV4cCI6MTY4MDMyNjkzN30.EPtkJ5JwOF11XUw5RA5lanPhJsN7KtCyTSR6CbnOyaU')
# print(decode_test)

# def test_func(x:int):
#     return x

class User(BaseModel):
    id: int
    username : str
    password : str
    confirm_password : str
    alias = 'anonymous'
    timestamp: Optional[datetime] = None
    friends: List[int] = []

# data = {'id': 'asd', 'username': 'wai foong', 'password': 'Password123', 'confirm_password': 'Password123', 'timestamp': '2020-08-03 10:30', 'friends': [1, '2', b'3']}
# a = User(**data)
# print(a.friends)