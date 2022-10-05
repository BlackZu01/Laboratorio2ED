from classes.Node import Node

class CircularLinkedList:

    

    def __init__(self) -> None:
        self.currentNode = None
        self.ROOT = Node(None, None)
        self.TAIL = Node(None, None)
        self.prev = None
        self.ROOT.next = self.TAIL
        self.TAIL.next = self.ROOT
        self.size = 0

    def addNode(self, node: Node) -> None:
        P = node

        if self.ROOT.data == None:
            self.ROOT = P
            self.TAIL = P
        else:
            self.TAIL.next = P
            self.TAIL = P
        self.TAIL.next = self.ROOT
        self.size += 1
    
    def first(self):
        self.currentNode = None
        return self.next()

    def displayList(self) -> None:
        self.current = self.ROOT

        if self.ROOT == None:
            print('[+] La lista esta vacía !!!')
            return
        print('[+] Current nodes:')
        print(f'\t{self.current.data}')
        while self.current.next != self.ROOT:
            self.current = self.current.next
            print(f'\t{self.current.data}')

    def next(self):
        
        if self.currentNode == None:
            self.currentNode = self.ROOT
            return self.currentNode
        
        self.currentNode = self.currentNode.next
        return self.currentNode
        
        
    def addNodeAlreadyCreated(self, moveNode: Node, newNode: Node) -> None:
        P = self.ROOT  
        
        while P.data != moveNode.data:
            # print(f'{self.prev} - {P.data}')
            self.prev = P  
            P = P.next       

        temp = self.prev.next
        self.prev.next = newNode
        newNode.next = moveNode
        

    def __len__(self):
        return self.size

    def removeNode(self, node: Node) -> None:
        if (self.ROOT == None):
            print("Empty list")
        
        
        p = self.ROOT
        i = 0
        while i <= len(self):
            if p.data == node.data:
                break
            temp = p
            p = p.next
            i += 1
        if i > len(self):
            return False

        if p == self.ROOT:
            self.TAIL.next = self.ROOT.next
            self.ROOT = self.ROOT.next
            p.next = self.ROOT
            self.size -= 1
            return p

        elif p == self.TAIL:
            i = 0
            position = len(self) - 1
            while i < position:
                Prevp = p
                p = p.next
                i += 1
            p.next = self.ROOT
            self.TAIL = Prevp.next
            self.size -= 1
            return p
        else:
            temp.next = p.next
            self.size -= 1
            return p
    
    def reverseList(self):
        current = self.ROOT
        prev = None
        while current != None:
            self.next = current.next
            current.next = prev
            prev = current
            current = self.next
        DROOT = prev
        temp = self.ROOT
        self.ROOT = self.ROOT.next
        self.TAIL = temp
        self.TAIL.next = self.ROOT
        return DROOT

    def __repr__(self) -> str:
        respuesta = ''
        P = self.ROOT
        respuesta = str(P.data) + ' -> '
        P = P.next
        
        while P != self.ROOT:
            respuesta += str(P.data) + ' -> '
            P = P.next
        respuesta += str(P.data)    
        return respuesta