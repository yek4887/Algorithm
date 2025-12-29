def solution(numbers):
    numbers.sort() # 배열 오름차순 정렬
    return max(numbers[0]*numbers[1],numbers[-1]*numbers[-2])