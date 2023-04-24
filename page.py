# function: get_total_page
# input: 게시물의 총 건수(m), 한 페이지에 보여줄 게시물(n)
# output: 총 페이지 수

# version 0.0
# date: 2023.04.24

# review
# 식 안에 return을 넣는 법 기억
# 필요없는 변수 선언하지 않기

# 내가 작성한 코드
def get_total_page(m, n):
    
    # 게시물의 총 건수 <= 한 페이지에 보여줄 게시물
    if m <= n:
        total_page = 1
    # 게시물의 총 건수 > 한 페이지에 보여줄 게시물
    else:
        total_page = m//n + 1

    return total_page

# 답으로 나온 코드
def get_total_page_a(m, n):
    if m % n == 0:
        return m // n
    else:
        return m // n + 1
    
print(get_total_page(5, 10))
print(get_total_page(15, 10))
print(get_total_page(25, 10))
print(get_total_page(35, 10))
print()

print(get_total_page_a(5, 10))
print(get_total_page_a(15, 10))
print(get_total_page_a(25, 10))
print(get_total_page_a(35, 10))