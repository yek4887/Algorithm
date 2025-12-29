def solution(numbers): #1.매개변수 numbers(배열)을 받음
    total = 0 #2. 배열의 합을 저장하는 변수 선언
    for i in numbers: #3. 배열을 순회하며 각각의 원소 저장
        total += i #4. 원소의 합을 total 변수의 저장
    return total / len(numbers) #5. 합을 크기로 나눈 평균값 리턴