# function: 특정 디렉터리부터 하위 파일 중 *.py 파일만 출력
# input: dirname
# output: directory 안의 py 파일명

# version 0.0
# date: 2023.04.24

# review
# os.path.splitext: 파일 이름을 확장자를 기준으로 두 부분으로 나눠줌
# os.walk: 시작 디렉터리부터 시작하여 그 하위 모든 디렉터리를 차례대로 방문하게 해주는 함수

import os

def search(dirname):
    try:
        filenames = os.listdir(dirname)
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)
            if os.path.isdir(full_filename):    # 디렉토리면 시행
                search(full_filename)
            else:   # 파일이면 실행
                ext = os.path.splitext(full_filename)[-1]
                if ext == '.py':
                    print(full_filename)
    except PermissionError:
        pass


search("/Users/jangmi/Desktop/Coding/Python")

# # os.walk 사용
# import os

# for (path, dir, files) in os.walk('/Users/jangmi/Desktop/Coding/Python'):
#     for filename in files:
#         ext = os.path.splitext(filename)[-1]
#         if ext == '.py':
#             print("%s/%s" %(path, filename))