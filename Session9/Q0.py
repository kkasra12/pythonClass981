class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.previous=None
    def setNext(self,nextNode):
        if type(nextNode)!=type(self):
            raise Exception("nextNode is not node!!!")
        self.next=nextNode
        nextNode.previous=self
    def setPrevious(self,previousNode):
        if type(previousNode)!=type(self):
            raise Exception("previousNode is not node!!!")
        self.previous=previousNode
        previousNode.next=self
    def add(self,newNode):
        assert type(newNode)==type(self)
        newNode.setNext(self.next)
        self.setNext(newNode)
    def printToEnd(self):
        currentNode=self
        while currentNode!=None:
            print(currentNode.data,end=" ")
            currentNode=currentNode.next
        print()
    def delete(self):
        self.next.setPrevious(self.previous)
        # self.previous.setNext(self.next)
    def root(self):
        currentNode=self
        while currentNode.previous!=None:
            currentNode=currentNode.previous
        return currentNode
    def __len__(self):
        currentNode=self
        counter=0
        while currentNode.previous!=None:
            currentNode=currentNode.previous
            counter+=1

        currentNode=self
        while currentNode.next!=None:
            currentNode=currentNode.next
            counter+=1
        counter+=1
        return counter

if __name__ == '__main__':
    nodes=[node(i) for i in range(10)]
    for node_,nextNode in zip(nodes,nodes[1:]):
        node_.setNext(nextNode)
    nodes[0].printToEnd()
    nodes[4].add(node(4.5))
    nodes[0].printToEnd()
    print("g",len(nodes[4]))
