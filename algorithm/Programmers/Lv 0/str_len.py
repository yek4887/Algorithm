# 문자열 앞의 n 글자 가져오기
def solution(my_string, n):
    return my_string[:n] # 문자열 인덱싱을 이용해 앞부터 n글자 가져오기

# 또 다른 풀이
def solution2(my_string,n):
    answer = '' # 앞의 n글자를 담을 빈 문자열 선언
    for i in range(n): # 0 인덱스부터 n-1번쨰 인덱스(=n번째글자)까지 순회
        answer += my_string[i] # 빈 문자열에 n-1번째 인덱스까지의 글자 추가
    return answer