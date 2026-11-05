# Traverse thorough every eleement of linkedList
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def travs(head):
    current=head
    while current is not None:
        print(current.data)
        current=current.next

head=Node(200)
head.next=Node(30)
head.next.next=Node(40)

travs(head)