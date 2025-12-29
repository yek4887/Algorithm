def solution(n):
    answer = [] # 오름차순으로 정렬된 n의 약수를 담을 빈 배열 선언
    for i in range(1,n+1): # n 이하의 수를 순회
        if(n % i == 0): # 나누어떨어진다면 n의 약수
            answer.append(i) # 해당 수를 빈 배열에 추가
    answer.sort() # 오름차순 정리 후
    return answer # 정렬된 배열 리턴!
   