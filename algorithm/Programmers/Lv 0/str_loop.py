# 문자열 반복
def solution(my_string,n):
    answer = ''
    #1. 문자열을 순회하며 각 문자를 인식 
    for i in my_string:
    #2. 각 문자 i에 반복해야 할 정수 n을 곱해주고, 결과를 빈 문자열에 누적시켜 더함
        answer += i * n # 2-1: '문자' * 정수 시 문자로 반복됨
    #3. 각 문자가 n번 곱해진 변수 리턴
    return answer

# 더 간단한 풀이
# def solution(my_string, n):
#     return ''.join(i*n for i in my_string)