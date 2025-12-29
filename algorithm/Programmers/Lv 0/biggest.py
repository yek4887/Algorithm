# 가장 큰 수 찾기
def solution(array):
    max_value = max(array) # 배열의 최댓값을 구해서 변수로 저장
    max_index = array.index(max_value) # 가장 큰 수의 인덱스는 배열.index(해당 수)로 지정
    return [max_value,max_index]

# def solution(array): # 간단하게
#     return(max(array),array.index(max_value))