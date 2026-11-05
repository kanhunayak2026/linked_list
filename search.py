#Search for an element
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def search(head,target):
    current=head
    while current is not None:
        if current.data==target:
            return True
        current=current.next
    return False
head=Node(110)
head.next=Node(102)
head.next.next=Node(390)
print(search(head,10))
print(search(head.next,110))