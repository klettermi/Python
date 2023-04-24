# function: 탭을 4개의 공백으로 바꾸기
# input: 문서 파일 일기, 문자열 변경하기
# output: 탭이 공백으로 수정된 문서 파일

# version 0.0
# date: 2023.04.24

# review

# python tabto4.py src dst
# >> python tabto4.py a.txt b.txt

import sys

src = sys.argv[1]   # 기존 문서
dst = sys.argv[2]   # 변경 문서

# # Create txt file
# f = open('a.txt', 'w')
# f.write('Life   is  too short \n')
# f.write('You    need    python')
# f.close()

f = open(src)
tab_content = f.read()
f.close()

space_content = tab_content.replace("\t", " "*4)

f = open(dst, 'w')
f.write(space_content)
f.close()