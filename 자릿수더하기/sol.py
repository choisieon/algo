
def solution(n):
    return sum(int(i) for i in str(n))

# 정수 n이 매개변수로 주어질 때 n의 각 자리 숫자의 
# 합을 return하도록 solution 함수 완성

def solution(n):
    answer = 0

    while n > 0:
    a, b = dimvod(n, 10)
    # a = divmod(n, 10)[0] 
    # b = divmod(n, 10)[1]

    answer = answer + b
    n = a

def solution(n):
    answer = 0
    for i in str(n): 
        answer = answer + int(i)
    return answer

def solution(n)
    return sum(map(int,list(str(n))))   