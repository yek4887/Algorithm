def solution(numbers):
    numbers.sort() #1.배열을 오름차순 정렬(reverse = True 시 내림차순)
    for i in numbers: #2. 배열의 원소들을 순회
        return numbers[len(numbers)-1] * numbers(len(numbers)-2)
    #3. 가장 오른쪽 원소(최댓값)과 그 다음 원소(최댓값 다음으로 큰 값)의 곱 리턴