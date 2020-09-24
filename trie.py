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

        # populate root trie with first letters of each word in text
        for word in words:
            char = word[0]
            node = Node(char)
            self.trie.add_child(node)

        # add words from text to trie, based on their starting characters
        word: str
        for word in words:
            node: Node
            for node in self.trie.children:
                if node.value == word[0]:
                    word_trie: Node = self.generate_sub_trie(
                        word=word,
                        idx=1,
                        trie=node
                    )
                    node.add_child(word_trie)

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
