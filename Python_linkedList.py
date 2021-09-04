class NodeofList(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
    def setElement(self, value):
        self.value = value
        
    def getElement(self):
        return self.value
        
    def setNext(self, next):
        self.next = next
        
    def getNext(self):
        return self.next
    
class linkedList(object):
    def __init__(self, head = None):
        self.head = head 
        self.count = 0
        
    def getCount(self):
        return self.count
    
    def elementInsertion(self, data):
        newElement  = NodeofList(data)
        newElement.setNext(self.head)
        self.head = newElement
        self.count += 1
        
    def searchElement(self, value):
        element = self.head
        while(element != None):
            if element.getElement() == value:
                return element
            else:
                element = element.getNext()
        return None
    
    def deleteElement(self, index):
        if index > self.count-1:
            return
        if index == 0:
            self.head = self.head.getNext()
        else:
            temp = 0
            node = self.head
            while(temp < index-1):
                node = node.getNext()
                temp += 1
            node.setNext(node.getNext().getNext())
            self -=1
            
    def endList(self):
        temp = self.head 
        while(temp != None):
            print(temp.getElement())
            temp = temp.getNext()
            
            #Testing
            
element = linkedList()

element.elementInsertion(15)
element.elementInsertion(16)
element.elementInsertion(17)
element.elementInsertion(18)
element.elementInsertion(19)

print("Total Elements in List = ", element.getCount())
print("Finding Element in the list = ", element.searchElement(16))
        
        