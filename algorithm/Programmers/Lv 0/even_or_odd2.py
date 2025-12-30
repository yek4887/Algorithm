n = int(input()) # int는 input()으로 받은 문자열을 정수로 변환
if(n % 2 == 0): # n이 짝수라면
    print("{} is even".format(n)) # 문자열 포매팅
else: # n이 홀수라면
    print(f"{n} is odd") # f-string 포매팅