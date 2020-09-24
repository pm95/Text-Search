# Author: Pietro Malky
# Date: 09/23/2020
# Purpose: Efficient trie-based text search algorithm

import os


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

    def get_child(self, idx: int) -> "Node":
        return self.children[idx]

    def generate_trie(self) -> list:
        children_str: str = ""
        curr: str = ""

        c: Node
        for c in self.children:
            curr = c.value
            if len(c.children) > 0:
                curr = c.generate_trie()
            children_str += curr + ", "

        return "%s: [%s]" % (
            self.value,
            children_str
        )

    def print_self(self):
        print(self.value)

    def print_trie(self):
        print(self.generate_trie())


class TrieTextSearcher:
    def __init__(self, path: str = ""):
        self.path: str = path
        self.text: str = ""
        self.trie: Node = Node("*")

    def load_text(self):
        if self.path == "":
            self.text = ""
            return

        with open(self.path, "r") as fin:
            self.text = fin.read().lower()

    def generate_sub_trie(self) -> Node:
        pass

    def generate_trie(self):
        words: list = self.text.split(" ")

        print(words)

    def print_text(self):
        print(self.text)

    def print_trie(self):
        self.trie.print_trie()


if __name__ == "__main__":
    t = TrieTextSearcher("./data.txt")

    t.load_text()
    t.print_text()
    t.generate_trie()
    t.print_trie()
