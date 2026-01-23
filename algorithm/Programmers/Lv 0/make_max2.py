def solution(numbers):
    numbers.sort() # 배열 오름차순 정렬
    return max(numbers[0]*numbers[1],numbers[-1]*numbers[-2])
#정수값(최소 ~ 최대 순 정렬)-> 음수 * 음수 / 양수 * 양수 중 더 큰 값을 도출하여 리턴