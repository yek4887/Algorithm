def solution(num_list):
    for i in num_list: # 1. num_list 배열을 순회하다
        if i < 0: #2. 배열값이 음수라면
            return num_list.index(i) #2-1. 해당 값에 위치한 인덱스 반환
    return -1 # 2-2. 음수가 없다면 -1 반환