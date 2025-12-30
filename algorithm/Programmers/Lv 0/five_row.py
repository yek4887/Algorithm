# 5명씩
def solution(names):
    answer = [] # 5명씩 묶인 리스트의 앞 원소를 담을 배열 선언
    for i in range(0, len(names),5): # names 배열의 인덱스를 5씩 증가시키며 순회
        answer.append(names[i]) # 5명씩 묶인 리스트의 앞 원소를 answer에 추가
    return answer