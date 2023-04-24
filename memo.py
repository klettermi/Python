# function: 메모 추가하기, 메모 조회하기
# input: 메모 내용
# output: memo.txt

# version 0.0
# date: 2023.04.24

# review
# sys.argv: 프로그램을 실행할 때 입력된 값을 읽어들일 수 있는 파이썬 라이브러리

import sys

option = sys.argv[1]

# memo 입력
if option == '-a':
    memo = sys.argv[2]
    f = open('memo.txt', 'a')
    f.write(memo)
    f.write('\n')
    f.close()  

# memo 조회
elif option == '-v':
    f = open('memo.txt')
    memo = f.read()
    f.close()
    print(memo)