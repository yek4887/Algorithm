"""오른쪽 정렬 별찍기. 이때 공백의 크기는 전체 줄 - 현재 줄
(또는 별의 개수)
"""
#sol1
n = int(input())

for i in range(1,n+1): #1부터 n번째 줄까지 별 출력
  print(" " * (n-i) + '*'*i) # (n-i) = 총 줄 - 현재 줄 <<공백 수
#sol2
n = int(input())

for i in range(1,n+1):
  star = print("*" * i)
  print(star.rjust(n))
#sol3
n = int(input())

for i in range(n): # 0 ~ n-1줄까지 반복
  print(" " * (n-i-1) + '*' * (i+1))