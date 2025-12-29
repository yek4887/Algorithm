def solution(my_string, letter):
    answer = '' #1. letter가 제거된 문자열을 담을 문자열 변수 선언
    for i in my_string: #2. 문자열을 순회하며 각 문자 인식
        if i != letter: #2-1: 각 문자가 letter(제거해야 할 문자)가 아니라면
            answer += i #2-2: 문자열에 추가
    return answer #3. letter가 제거된 문자열 

# 더 간단한 풀이
def solution(my_string, letter):
    return ''.join([i for i in my_string if i != letter]) # 리스트 컴프리헨션 사용 -> 이후 join을 통해 문자열로 변환
# replace()를 이용한 풀이
def solution(my_string, letter):
    return my_string.replace(letter, '')
