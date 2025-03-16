# 정수 n이 주어질 때, n이하의 짝수를 모두 더한 값을 return 하도록 solution 함수를 작성해주세요.

# 제한사항
# 0 < n ≤ 1000

# 입출력 예
# n	result
# 10	30
# 4	6

def solution(n):
    answer = 0
    if n % 2 == 0:
        answer = 0.5* n *(0.5*n+1)
    elif n % 2 == 1:
        answer = 0.25*(n-1)*(n+1)
    return answer

# 몫으로 풀이
def solution(n):
    answer = 2 * (n//2 *(n//2 + 1))/2
    return answer

# range 풀이
def solution(n):
    return sum(range(2, n+1, 2))
print(solution(12))