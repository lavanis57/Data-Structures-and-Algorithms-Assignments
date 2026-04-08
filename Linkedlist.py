class Node:
    def __init__(self, val, nxt=None):
        self.val = val
        self.next = nxt


def factorialLL(n, digits_per_node):
    base = 10 ** digits_per_node
    head = Node(-1) #Could be any negative number 
    head.next = Node(1)
    head.next.next = head
    curr = head
    carry = 0

    for i in range(2, n + 1):
        curr = curr.next
        carry = 0  

        while curr.val != -1:
            prod = curr.val * i + carry
            curr.val = prod % base
            carry = prod // base
            prev = curr
            curr = curr.next

        while carry > 0:
            node = Node(carry % base)
            carry //= base
            prev.next = node
            prev = node

        prev.next = curr

    return head


def printLL(head, digits_per_node):
    curr = head.next
    vals = []

    while curr.val != -1:
        vals.append(curr.val)
        curr = curr.next

    vals.reverse()

    print(vals[0], end='')
    for v in vals[1:]:
        print(str(v).zfill(digits_per_node), end='')
    print()


if __name__ == "__main__":
    N = 10
    Digits = 2
    result = factorialLL(N, Digits)
    printLL(result, Digits)
