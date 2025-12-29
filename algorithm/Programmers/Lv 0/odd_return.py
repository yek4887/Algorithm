# 나는 짝수가 싫어요
def solution(n):
	answer = [] # 1. 빈 배열 선언
	for i in range(1,n+1): # 2. n 이하 숫자를 순회하며
		if(i%2 !=0): # 3. 홀수라면
			answer.append(i) #4. 홀수를 answer 배열에 추가
	return answer

# 더 간단한 풀이
def solution(n):
    return [i for i in range(1, n+1, 2)] # n 이하의 홀수만을 리턴하도록 하는 컴프리헨션 식