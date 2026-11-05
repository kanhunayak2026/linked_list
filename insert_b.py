from traverse import travs
from print import Node
def insert_b(head,data):
    new_node=Node(data)
    new_node.next=head
    head=new_node
    return head
head=Node(10)
head.next=Node(30)
head.next.next=Node(40)
head=insert_b(head,50)
travs(head)
