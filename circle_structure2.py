class Node():
    def __init__(self):
        self.data = None
        self.link = None

node1 = Node() # 첫번째 노드 생성
node1.data = "가을"
node1.link = node1 # 첫번째 노드의 링크는 자기 자신을 가리킴 : 원형 구조

node2 = Node() # 두번째 노드 생성
node2.data = "리즈"
node1.link = node2 # 첫번째 노드의 링크는 두번째 노드를 가리킴
node2.link = node1 # 두번째 노드의 링크는 첫번째 노드를 가리킴(이게 핵심, 매 노드 생성시 링크를 첫번째 노드로 연결)

node3 = Node() # 세번째 노드 생성
node3.data = "원영"
node2.link = node3 # 두번째 노드의 링크는 세번째 노드를 가리킴
node3.link = node1 # 세번째 노드의 링크는 첫번째 노드를 가리킴

node4 = Node() # 네번째 노드 생성
node4.data = "레이"
node3.link = node4 # 세번째 노드의 링크는 네번째 노드를 가리킴
node4.link = node1 # 네번째 노드의 링크는 첫번째 노드를 가리킴

node5 = Node() # 다섯번째 노드 생성
node5.data = "이서"
node4.link = node5 # 네번째 노드의 링크는 다섯번째 노드를 가리킴
node5.link = node1 # 다섯번째 노드의 링크는 첫번째 노드를 가리킴

newNode = Node() # 새로운 노드 생성
newNode.data = "유진" # 유진 데이터를 리즈와 원영 사이에 삽입
node2.link = newNode # 두번째 노드의 링크는 새로운 노드를 가리킴
newNode.link = node3 # 새로운 노드의 링크는 세번째 노드를 가리킴 -> node2.link = node3로 연결되던 것을 newNode로 변경

print(newNode.data)# 새로운 노드의 데이터 출력 : 유진

current =  node1 # current는 첫번째 노드를 가리킴
print(current.data, end=' ') # current가 가리키는 노드의 데이터 출력 공백으로 구분
while (current.link != node1): # current의 링크가 첫번째 노드를 가리키지 않을 때까지 반복
# 즉, 마지막 노드의 링크가 첫번째 노드를 가리키므로 마지막 노드까지 출력
    current = current.link
    print(current.data, end=' ') # current가 가리키는 노드의 데이터 출력 공백으로 구분

