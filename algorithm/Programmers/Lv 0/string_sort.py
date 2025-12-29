def solution(my_string):
    answer = [] # 정렬될 빈 리스트 선언
    for i in my_string: # 문자열을 순회하며 각 문자 인식
        if i.isdigit(): # 해당 문자열의 문자가 숫자라면
            answer.append(int(i)) # int로 숫자화한뒤 빈 리스트에 추가
    answer.sort() # 이후 오름차순 정렬 후 리턴
    return answer

# 간단한 풀이
def solution(my_string):
    return sorted([int(i) for i in my_string if i.isdigit()])