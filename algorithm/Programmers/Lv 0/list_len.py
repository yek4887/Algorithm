# 길이에 따른 연산
def solution(num_list):
    # 1. 리스트의 길이가 11 이상이라면
    if len(num_list) >= 11:
        return sum(num_list)  # sum() 함수를 사용하면 바로 합계가 나옵니다.
    
    # 2. 리스트의 길이가 10 이하라면 (else)
    else:
        mulist = 1
        for i in num_list:
            mulist *= i
        return mulist