# n번째 원소부터 끝까지 가져오기
def solution(num_list, n):
    # n번째 원소는 인덱스 상에서 n-1에 해당합니다.
    answer = num_list[n-1:]
    return answer