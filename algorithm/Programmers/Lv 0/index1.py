# n번째 원소부터 끝까지 가져오기
def solution(num_list, n):
    # n번째 원소는 인덱스 상에서 n-1에 해당합니다.
    answer = num_list[n-1:]
    return answer
# 또 다른 풀이
# def solution2():
#     answer = [] # n-1번째 인덱스부터 끝까지 담을 배열 선언
#     for i in range(n-1,len(num_list)):
#         answer.append(num_list[i])

def solution(num_list, n):
    answer = []
    for i in range(0,n): # 0번째 인덱스부터 n-1번째 인덱스까지
        answer.append(num_list[i])
    return answer 

# def solution(num_list, n):
#     return [i for i in num_list[:n]] # 0번째 인덱스부터 n-1번째 인덱스까지