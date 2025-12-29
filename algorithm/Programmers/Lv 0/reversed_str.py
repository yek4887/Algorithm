#Q. 문자열 my_string이 매개변수로 주어집니다. my_string을 거꾸로 뒤집은 문자열을 return하도록 solution 함수를 완성해주세요.
def solution(my_string):
    return ''.join(list(reversed(my_string)))

#1단계 : 뒤집힌 문자열을 return -> ex) ‘hello’ -> ‘olleh’
#2단계: reversed()를 통해 문자열 뒤집기 + 리스트화(list())
# result = list(reversed(my_string))
# join() 함수를 통해 해당 리스트를 문자열로 합침
# return ‘ ‘.join(result)

# ** ‘ ‘.join(리스트) -> 괄호 안 문자열들을 하나의 문자열로 합침. 주의할 점은, 정수같은 숫자는 합칠 수 없음. 합치기 위해선 문자 변환 필요
# ** 이터레이터 : 데이터를 집어올리는 **집게** < 이터레이터를 반환하는 함수 실행 시 해당 함수의 데이터를 하나씩 꺼내며, 모두 꺼내면 사라짐