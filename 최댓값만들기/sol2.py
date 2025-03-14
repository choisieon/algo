# 정렬을 직접 구현 <버블 정렬>

def solution(numbers):
    n = len(numbers)

    for i in range(n):
        for j in range(0, n-i+1):
            print(i, j)
                if numbers[j] > number[j+1]
            numbers[j], number[j+1] = numbers[j+1], numbers[j]

    return numbers[-1] * numbers[-2]