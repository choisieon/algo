def solution(n, k):
    answer = 12000 * n + 2000 * k
    
    if n < 10:
        return answer

    else:   
        answer = answer - 2000 * (n//10) 
        return answer

print(solution(10, 3))
print(solution(64, 6))

