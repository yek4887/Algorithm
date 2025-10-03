class Node():
    def __init__(self):
        self.data = None
        self.link = None

def printNodes(start): # 매개변수로 시작 노드를 전달받는다.
    current = start # 전달받은 노드를 현재 노드로 지정
    if current.link == None: # 노드가 하나도 없는 경우(head가 None인 경우)
        return
    print(current.data, end=' ') # current가 가리키는 노드의 데이터
    while current.link != start:
        current = current.link # current를 다음 노드로 이동
        print(current.data, end=' ') # current가 가리키는 노드의 데이터 출력
    print()

def insertNode(findData, insertData): # findData 뒤에 insertData를 삽입하는 함수
    global memory, head, current, pre
    if head.data == findData: # 첫번째 노드 뒤에 삽입하는 경우
        node = Node()
        node.data = insertData
        node.link = head # 새로 생성된 노드의 링크는 헤드가 가리키는 첫번째 노드를 가리킴
        last = head
        while last.link != head: # 마지막 노드를 찾기 위한 반복문
            last = last.link
        last.link = node # 마지막 노드의 링크는 새로 생성된 노드를 가리킴
        head = node # head는 새로 생성된 노드를 가리킴(= 첫번째 노드를 헤드로 지정)
        return
    
    current = head # current는 첫번째 노드를 가리킴
    while current.link != head: # 중간 노드 삽입
        pre = current
        current = current.link
        if current.data == findData: # current가 찾는 데이터와 같다면
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            return
    # 마지막 노드 뒤에 삽입하는 경우
    node = Node()
    node.data = insertData
    node.link = head 
    current.link = node
           