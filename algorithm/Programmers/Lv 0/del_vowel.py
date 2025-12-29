# 모음 제거 문자열 리턴
def solution(my_string):
    # 1. 모음이 담긴 배열 선언
    vowel = ['a', 'e', 'i', 'o', 'u']
    # 2. 빈 문자열 선언
    answer = ''
    # 3. my_string을 순회하며 문자 인식
    for i in my_string:
        # 4. 모음이 아닌 문자들을 빈 문자열에 누적 (공백 8칸)
        if i not in vowel:
            answer += i
    # 5. 모음이 제거된 문자열 리턴
    return answer

# 리스트 컴프리헨션을 이용한 풀이
def solution(my_string):
    return ''.join([i for i in my_string if i not in ['a', 'e', 'i', 'o', 'u']])
# 위 식 :my_string의 i가 join된 문자열 리턴함(단, i가 모음이 아닌 경우)
# 리스트 컴프리헨션 형태 : [출력값 for 요소 in 반복가능한객체 if 조건]