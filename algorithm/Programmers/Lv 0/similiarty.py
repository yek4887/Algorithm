# 두 배열이 얼마나 유사한지 확인해보려고 합니다. 문자열 배열 s1과 s2가 주어질 때 
# 같은 원소의 개수를 return하도록 solution 함수를 완성

# def solution(s1, s2):
#     return len(set(s1) & set(s2))

def solution(s1, s2): 
    #1. 원소 개수를 담는 변수 선언
    cnt = 0
    #2. 문자열 배열을 순회하며 값 비교
    for i in s1: # s1에 원소 i값을 꺼냈는데
        if i in s2: # 해당 원소가 s2 배열에도 있다면
            cnt += 1 #3. cnt 1 추가
    return cnt #4. 리턴