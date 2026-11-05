
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
def travs1(head):
    current=head
    while current is not None:
        print(current.data)
        current=current.next
def insert_end(head,data):
    new_node=Node(data)

    if head is None:
        return new_node
    current=head
    while current.next is not None:
        current=current.next
    current.next=new_node

    return head
head=Node(45)
head.next=Node(67)
head.next.next=Node(78)
head=insert_end(head,56)
travs1(head)
