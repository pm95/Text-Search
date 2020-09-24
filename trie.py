# Author: Pietro Malky
# Date: 09/23/2020
# Purpose: Efficient trie-based text search algorithm

from typing import Type


class Node:
    def __init__(self, value: str = ""):
        super().__init__()
        self.children: list = []
        self.value = value

    def add_child(self, child: "Node") -> bool:
        c: Node
        for c in self.children:
            if c.value == child.value:
                return False
        self.children.append(child)

    def generate_trie(self) -> list:
        children_str: str = ""
        curr: str = ""

        c: Node
        for c in self.children:
            curr = c.value
            if len(c.children) > 0:
                curr = c.generate_trie()
            children_str += curr + ", "

        return "%s:[%s]" % (
            self.value,
            children_str
        )

    def print_trie(self):
        print(self.generate_trie())


# create test nodes
n0: Node = Node("a")
n1: Node = Node("b")
n2: Node = Node("c")
n3: Node = Node("d")
n4: Node = Node("e")
n5: Node = Node("f")
n6: Node = Node("g")
n7: Node = Node("h")
n8: Node = Node("i")
n9: Node = Node("j")


# add children to parent node
n0.add_child(n1)  # a: b
n0.add_child(n2)  # a: b, c
n0.add_child(n3)  # a: b, c, d
n0.add_child(n4)  # a: b, c, d, e
n5.add_child(n6)  # a: b, c, d, e;  f: f
n5.add_child(n7)
n8.add_child(n9)
n5.add_child(n8)
n0.add_child(n5)  # a: b, c, d, e, f: f


# print parent node
n0.print_trie()
