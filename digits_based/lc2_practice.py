a = [2,4,3]
b = [5,6,4]

carry = 0
result = []

for i in range(len(a)):
    total = a[i] + b[i] + carry
    digit = total % 10
    carry = total // 10
    result.append(digit)

# print(result)


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

node1 = ListNode(2)
node2 = ListNode(4)
node3 = ListNode(3)

node1.next = node2
node2.next = node3

current =  node1
while current:
    print(f"Current Value : {current.val} | Next : {current.next}")
    current = current.next