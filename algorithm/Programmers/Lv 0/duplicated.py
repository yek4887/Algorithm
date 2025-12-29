# 중복된 숫자 개수
def solution(array,n):
    cnt = 0
    #2. 배열을 순회하며 원소 인식
    for i in array:
        if i == n: # i가 숫자 n과 같다면
            cnt += 1 # 1 증가
    return cnt # 최종 중복 개수 반환
