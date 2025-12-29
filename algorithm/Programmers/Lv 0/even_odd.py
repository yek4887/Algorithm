def solution(num_list):
    # 1. 카운트 변수 생성 (함수 안이니까 4칸 들여쓰기)
    even_cnt = 0 # 2-1: 짝수 변수
    odd_cnt = 0 # 2-2 : 홀수 변수

    # 2. 정수 리스트를 순회하며 각 정수 인식
    for num in num_list:
        if num % 2 == 0: # 3. 짝수라면 (if문 안쪽은 8칸)
            even_cnt += 1 
        else:            # 3-2. 홀수라면
            odd_cnt += 1 

    # 4. 결과 리턴 (for문과 같은 라인인 4칸 위치)
    return [even_cnt, odd_cnt]

# def solution(num_list):
#     answer = [0,0]
#     for n in num_list:
#         answer[n%2]+=1
#     return answer