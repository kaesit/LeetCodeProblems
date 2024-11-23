class Node():
     def __init__(self, data = None, next = None):
          self.data = data
          self.next = next
          
          
class LinkedList():
     def __init__(self):
          self.head = None
          
          
     def addNode(self, data):
          newNode:Node = Node(data)
          if self.head is None:
               self.head = newNode
               return
          else:
               temp:Node = self.head
               while temp.next is not None:
                    temp = temp.next
               temp.next = newNode
               """newNode.next = self.head
               self.head = newNode"""
     def deletNode(self, data:int):
          temp:Node = self.head
          prev:Node = None
          if temp is not None and temp.data == data:
               head = temp.next
               del temp
          else:
               while temp is not None and temp.data != data:
                    prev = temp
                    temp = temp.next
               if temp is None:
                    print("Aranan değer bulunamadı")
               else:
                    prev.next = temp.next
          
          
                    
     def returnList(self):
          temp:Node = self.head
          while(temp is not None):
               print(temp.data)
               temp = temp.next
               
               


class Main():
     def __init__(self):
          lst = LinkedList()
          
          lst.addNode(5)
          lst.addNode(3)
          lst.addNode(1)
          lst.addNode(7)
          lst.addNode(4)
          
          lst.returnList()
          lst.deletNode(4)
          print("Yenisi")
          lst.returnList()

if __name__ == '__main__':
     Main()
     
                    
          