class Node():
    def __init__(self): # self : 생성되는 인스턴스
        self.data = None # 다음 노드의 데이터
        self.link = None # 다음 노드를 가리키는 링크

node1 = Node() # 첫 번째 노드 생성
node1.data = "다현"
print(node1.data, end= ' ') # 다현

node2 = Node() # 두 번째 노드 생성
node1.link = node2 # 첫 번째 노드의 링크가 두 번째 노드를 가리킴