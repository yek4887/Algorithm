# 배열 원소의 길이
def solution(strlist): # 1. 문자열 배열 strlit를 매개변수로 받음
    answer = [] # 2. 배열의 원소의 길이를 담을 배열 생성
    for i in strlist: # 3. 배열을 순회하며 각 원소 인식
        answer.append(len(i)) # 4. append(), len() 함수를 사용해 원소의 길이를 answer 배열에 추가
    return answer # 5. answer 배열 리턴 