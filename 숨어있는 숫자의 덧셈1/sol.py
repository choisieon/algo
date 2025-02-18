def solution(my_string):
    result = []
    for char in my_string:
        if '0' <= char <= '9':
            result.append(int(char))
            sum(result)
    return result


#문자열 my_string이 매개변수로 주어집니다. 
# my_string안의 모든 자연수들의 합을 
# return하도록 solution 함수를 완성해주세요.

def solution(my_string):
    answer = 0
    numbers = []

    for char in my_string:
        if char.isdigit():
            numbers.append(int(char))



return sum(numbers)

def solution(my_string):
    answer = 0
    for char in my_string:
        if not (ord('A') <= ord(char) <= ord('z')):
            anwer += int(char)


def solution(my_string):
    answer = 0
    numbers = '0123456789'

    for char in my_string:
        if char in numbers:
            answer += int(char)

    return answer

def solution(my_string):
    answer = 0

    for char in my_string:
        try:
            answer += int(char)
        except:
            continue

    return answer