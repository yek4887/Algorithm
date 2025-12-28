#해당 값을 담을 변수(num1을 num2로 나눈 값에 1000 곱한) 생성
# 해당 변수의 정수 부분 리턴
#정수 부분만 리턴 -> int 자료형
def solution(num1, num2):
    result = (num1 / num2) * 1000
    return int(result)
