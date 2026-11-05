# count elements in a linkedlist
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def counts(head):
    count=0
    current=head
    while current is not None:
        count+=1
        current=current.next
    return count
head=Node(10)
head.next=Node(20)
head.next.next=Node(30)

print(counts(head))