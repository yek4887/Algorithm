def solution(n):
    result = 0
    #2. n 정수를 문자열로 바꾼 뒤 해당 문자열 순회
    for i in str(n): # if n = 241 for i in “241” i -> “2”, “4”, “1”
        result += int(i) #3. 해당 문자열의 문자를 정수로 변환한 뒤 저장
    return result
