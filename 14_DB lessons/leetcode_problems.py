from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Создаем фиктивный узел, который будет началом нового связанного списка
        dummy = ListNode()
        current = dummy

        # Итерируем по обоим спискам
        while list1 and list2:
            # Сравниваем значения текущих узлов
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            current = current.next

        # Если один из списков закончился, добавляем оставшиеся узлы из другого списка
        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        return dummy.next  # Возвращаем новый связанный список, начиная с первого узла


# Пример использования
list1 = ListNode(6, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(5, ListNode(4)))

solution = Solution()
merged_list = solution.mergeTwoLists(list1, list2)

# Вывод результата
while merged_list:
    print(merged_list.val, end=" ")
    merged_list = merged_list.next
