# 암호 해독
def solution(cipher,code):
    answer = '' # 해독된 문자열로 사용될 문자열 선언
    for i in range(code,len(cipher)+1): # code 배수부터 cipher 마지막 문자까지를 순회하며
        if(i % code == 0): # i가 code의 배수라면
            answer += cipher[i-1] # i번쨰 글자를 answer 코드에 추가(0번째 인덱스부터 시작하므로 i-1)
    return answer

# answer += cipher[i-1]이 문자열임에도 가능한 이유: cipher가 문자열이라 인덱싱을 통해 글자를 꺼내올 수 있고.
# 거기에 +=를 통해 이어붙이는 게 가능해서