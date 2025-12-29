def solution(my_string):
    answer = '' # 대소문자화된 문자열을 담을 빈 문자열 선언
    for i in my_string: # 문자열을 순회하자
        if i.isupper(): # 대문자라면
            answer += i.lower() # 소문자화된 문자를 문자열에 추가
        else: # 소문자라면
            answer += i.upper() # 대문자화한 뒤 문자열에 추가
    return answer # 리턴
           