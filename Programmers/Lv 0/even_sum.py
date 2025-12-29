# 정수 n이 주어질 때, n이하의 짝수를 모두 더한 값을 return 하도록 solution 함수를 작성.

def solution(n):
    sum  = 0 #1. n 이하의 짝수의 합을 담는 변수 초기화
    for i in range(1,n+1): #2. n 이하 수(각 반복 시 i가 들어감)를 순회하며 짝수를 더하자
        if(i % 2 == 0): 
            sum += i #3. 짝수라면 sum에 누적시킴
    return sum #4. 합을 담은 변수 return