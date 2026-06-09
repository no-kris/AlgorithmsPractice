from typing import Any, Self


class MaxHeap:
    def __init__(self) -> None:
        self.data: list = []

    def root_node(self):
        return self.data[0]

    def last_node(self):
        return self.data[-1]

    def left_child_index(self, index) -> int:
        return (index * 2) + 1

    def right_child_index(self, index) -> int:
        return (index * 2) + 2

    def parent_index(self, index) -> int:
        return (index - 1) // 2

    def insert(self, value) -> Self:
        self.data.append(value)
        new_node_index = len(self.data) - 1
        while (
            new_node_index > 0
            and self.data[new_node_index] > self.data[self.parent_index(new_node_index)]
        ):
            parent_index = self.parent_index(new_node_index)
            self.data[parent_index], self.data[new_node_index] = (
                self.data[new_node_index],
                self.data[parent_index],
            )
            new_node_index = parent_index

        return self

    def _has_greater_child(self, index) -> bool:
        left_condition = (
            self.left_child_index(index) <= len(self.data)
            and self.data[self.left_child_index(index) > self.data[index]]
        )
        right_condition = (
            self.right_child_index(index) <= len(self.data)
            and self.data[self.right_child_index(index) > self.data[index]]
        )
        return left_condition or right_condition

    def _find_larger_child(self, index) -> int:
        if not self.data[self.right_child_index(index)]:
            return self.left_child_index(index)
        elif not self.data[self.left_child_index(index)]:
            return self.right_child_index(index)
        elif (
            self.data[self.right_child_index(index)]
            > self.data[self.left_child_index(index)]
        ):
            return self.right_child_index(index)
        else:
            return self.left_child_index(index)

    def heap_pop(self) -> Any:
        value_to_delete = self.root_node()
        self.data[0] = self.data.pop()
        trickle_index = 0
        while self._has_greater_child(trickle_index):
            larger_child_index = self._find_larger_child(trickle_index)
            self.data[trickle_index], self.data[larger_child_index] = (
                self.data[larger_child_index],
                self.data[trickle_index],
            )
            trickle_index = larger_child_index
        return value_to_delete
