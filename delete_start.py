class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def delete_first(head):
    if head is None:
        return None
    head=head.next
    return head
def travs(head):
    current=head
    while current is  not None:
        print(current.data)
        current=current.next
head=Node(19)
head.next=Node(20)
head.next.next=Node(30)
head=delete_first(head)
travs(head)