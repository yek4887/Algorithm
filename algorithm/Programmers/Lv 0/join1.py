# 더 크게 합치기 -> 합친 값들 중 큰 값 반환
def solution(a, b):
    x = str(a) + str(b) 
    y = str(b) + str(a)
#2. 두 문자열을 정수형으로 바꾼 뒤 값 비교
    if int(x) > int(y):
        return int(x)
    else:
        return int(y)