# 클래스와 함수 선언 부분

class Node2():
    def __init__(self):
        self.plink = None # 앞쪽 노드
        self.data = None
        self.nlink = None # 뒤쪽 노드

def printNodes(start):
    current = start
    if current.nlink == None: 
        return
    print("정방향-->", end=' ')
    print(current.data, end=' ')
    while current.nlink != None: # 마지막 노드까지
        current = current.nlink
        print(current.data, end=' ')
    print()
    print("역방향-->", end=' ')
    print(current.data, end=' ')
    while current.plink != None: # 첫번째 노드까지
        current = current.plink
        print(current.data, end=' ')
# 전역 변수 선언 부분
memory = []
head, current, pre = None, None, None
dataArray = ['다현', '정연', '쯔위', '사나', '지효']

if __name__ == "__main__":

    node = Node2() # 첫번째 노드
    node.data = dataArray[0] # '다현'
    head = node # head가 첫번째 노드를 가리킴
    memory.append(node)

    for data in dataArray[1:]: # 두번째 이후 노드
        pre = node
        node = Node2()
        node.data = data
        pre.nlink = node
        node.plink = pre
        memory.append(node)
    
    printNodes(head)
