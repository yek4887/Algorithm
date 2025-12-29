def solution(money):
    answer = [] #1. 최대 아아 잔수와 남는 돈을 담을 배열 생성
    cnt = money // 5500 #2. 최대 구매 가능한 아아 잔수 저장 이때 정수만 필요하므로 /가 아닌 // 사용
    change = money % 5500 #3. 남는 돈 계산
    answer.append(cnt) #4. 배열에 최대 잔수 추가
    answer.append(change) #5. 배열에 남는 돈 추가
    return answer #6. answer 배열 리턴

# 더 간단한 풀이

# def solution(money):

#     answer = [money // 5500, money % 5500]
#     return answer