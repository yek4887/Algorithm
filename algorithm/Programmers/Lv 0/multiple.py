def solution(n,numlist):
    #1. 새 배열 생성 -> n의 배수를 담는 배열 리턴하기 위해
	answer = []
    #2. numlist 배열의 원소들을 순회하며 n의 배수 점검
	for i in numlist:
		if(i % n == 0): # i가 n의 배수라면
			answer.append(i) # answer 배열에 추가
	return answer