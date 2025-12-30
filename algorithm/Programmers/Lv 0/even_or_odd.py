# 짝수인지 홀수인지에 따라 다른 값 반환하기

def solution(n): # n을 매개변수로 받아
    sum = 0 # 합을 담을 변수 초기화
    if(n % 2 == 1): # n이 홀수라면
        for i in range(1, n+1, 2): # n 이하의 홀수를 순회하며
            sum += i # 홀수를 합에 더하기
    else: # n이 짝수라면
        for i in range(2,n+1,2): # n 이하의 짝수를 순회하면
            sum += (i**2) # 짝수의 제곱을 합에 더하기
    return sum # 최종 합 반환