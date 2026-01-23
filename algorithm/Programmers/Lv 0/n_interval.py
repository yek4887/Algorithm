def solution(num_list,n):
    answer = [] # 1. 원소들을 차례대로 담을 빈 배열 생성
    for i in range(0,len(num_list),n): # 2. n 간격으로 len(num_list)-1까지 반복
        answer.append(num_list[i]) # 3. answer 배열에 num_list의 i번째 원소 추가(n 간격)
    return answer # 4. 최종적으로 answer 배열 반환