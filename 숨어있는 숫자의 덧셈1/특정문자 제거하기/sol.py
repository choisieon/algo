def solution(my_string, letter):
    answer = ''

    for char in my_string:
        if char != letter:
            answer = answer + char


    return answer


def solution(my_string, letter):
    answer = ''

    answer = my_string.replace(letter, '')
    
    return answer