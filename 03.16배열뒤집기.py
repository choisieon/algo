# 문제 설명
# 정수가 들어 있는 배열 num_list가 매개변수로 주어집니다. num_list의 원소의 순서를 거꾸로 뒤집은 배열을 return하도록 solution 함수를 완성해주세요.

# 제한사항
# 1 ≤ num_list의 길이 ≤ 1,000
# 0 ≤ num_list의 원소 ≤ 1,000

def solution(num_list):
    answer = num_list[::-1]
    return answer
num_list = [1,2,3,4]

print(solution(num_list))


# 다른풀이
def solution(num_list):
    answer = list(reversed(num_list))
    return answer