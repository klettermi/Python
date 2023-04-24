# function: mult_add
# input: n (1~999 자연수)
# output: 3의 배수와 5의 배수의 총합

# version 0.0
# date: 2023.04.24

def mult_add(n):
    result = 0

    for i in range(1, n+1):     
        # 3의 배수과 5의 배수 result에 더하기
        if i % 3 == 0 or i % 5 == 0:
            result += i
    
    return result

print(mult_add(10))