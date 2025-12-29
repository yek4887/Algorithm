# 순서쌍의 개수

def solution(n): #1. 자연수 n을 받아서
    cnt = 0 #2. 각 쌍을 이루는 변수 초기화
    for i in range(1,n+1): #2-1: n 이하의 정수들을 순회
        if(n % i == 0): #2-2: i가 n의 약수라면(순서쌍에 포함되므로 카운트)
            cnt += 1 # 3. 값 누적
    return cnt