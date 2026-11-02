# Задача: развернуть участок односвязного списка

# Дана голова односвязного списка head и два числа left и right
# (позиции считаются с 1, 1 ≤ left ≤ right ≤ длина списка).

# Разверни узлы с позиции left по позицию right включительно,
# остальные узлы оставь на своих местах. Верни голову списка.

# Примеры:
#   Вход:  1 → 2 → 3 → 4 → 5,  left = 2, right = 4
#   Выход: 1 → 4 → 3 → 2 → 5

#   Вход:  1 → 2 → 3,  left = 1, right = 3
#   Выход: 3 → 2 → 1          (разворачиваем весь список)

#   Вход:  5,  left = 1, right = 1
#   Выход: 5

# Требования:
#   - переставляй сами узлы (меняй .next), а не значения .val;
#   - нельзя складывать узлы или значения в list/массив;

# Усложнение: реши за один проход по списку.

# Узел списка:

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_between(head, left, right):
    if not head or left == right:
        return head

    dummy = ListNode(0, head)
    prev = dummy

    for _ in range(left - 1):
        prev = prev.next

    curr = prev.next

    for _ in range(right - left):
        nxt = curr.next

        curr.next = nxt.next
        nxt.next = prev.next
        prev.next = nxt

    return dummy.next

def build(values):
    dummy = ListNode()
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def to_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out

if __name__ == '__main__':
    print(to_list(reverse_between(build([1, 2, 3, 4, 5]), 2, 4)))  # [1, 4, 3, 2, 5]
    print(to_list(reverse_between(build([1, 2, 3]), 1, 3)))        # [3, 2, 1]
    print(to_list(reverse_between(build([5]), 1, 1)))              # [5]