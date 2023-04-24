# function: gugudan
# input: n
# output: n값의 구구단, 리스트 형식으로 return

# version 0.0
# date: 2023.04.24

def gugudan(n):
    result = []
    
    for i in range(1, 10):
        result.append(n*i)
    
    return result

print(gugudan(2))