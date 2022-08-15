from typing import Any

from collections import deque

__all__ = (
    'Node',
    'Graph'
)


class Node:
    def __init__(self, value: Any):
        self.value = value

        self.outbound = []
        self.inbound = []

        self.visited = False

    def point_to(self, other: 'Node'):
        self.outbound.append(other)
        other.inbound.append(self)

    def __str__(self):
        return f'Node({repr(self.value)})'

    __repr__ = __str__


class Graph:
    def __init__(self, root: Node):
        self._root = root

    def __clear_visited(self):
        queue = deque()
        queue.append(self._root)
        while queue:
            node = queue.popleft()
            node.visited = False
            for out in node.outbound:
                if out.visited:
                    queue.append(out)

    def dfs(self) -> list[Node]:
        result = []
        stack = deque()
        stack.append(self._root)
        while stack:
            node = stack.pop()
            if not node.visited:
                node.visited = True
                result.append(node)
                for out in node.outbound[-1::-1]:
                    stack.append(out)
        self.__clear_visited()
        return result

    def bfs(self) -> list[Node]:
        result = []
        queue = deque()
        queue.append(self._root)
        while queue:
            node = queue.popleft()
            if not node.visited:
                result.append(node)
            node.visited = True
            for out in node.outbound:
                if not out.visited and out not in queue:
                    queue.append(out)
        self.__clear_visited()
        return result
