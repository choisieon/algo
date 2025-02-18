solution(n,k):
    # n : 양꼬치 인분수 / k : 음료수 개수
    answer = 0
    #             양꼬치 총액    음료수 총액   서비스 총액
    answer = n * 12000 + k * 2000 - (n//10 * 2000)
    
    return answer