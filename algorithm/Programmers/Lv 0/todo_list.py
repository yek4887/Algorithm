def solution(todo_list, finished):
    answer = [] # 문자열 배열을 리턴할 빈 배열 선언
    for i in range(len(finished)): # 배열 순회 : i에는 finished 배열의 각 인덱스가 들어감
        if int(finished[i])==0: # finished[i]가 false라면
               answer.append(todo_list[i]) # todo_list[i]를 answer에 추가
    return answer