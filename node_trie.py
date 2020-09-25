# Author: Pietro Malky
# Date: 09/25/2020
# Purpose: Node-based trie


class Trie:
    def __init__(self, value: str = "*"):
        super().__init__()
        self.value = value
        self.children: list = []

    # private methods

    def _add_node(self, node: "Trie") -> bool:
        child: Trie
        for child in self.children:
            if child.value == node.value:
                return False
        self.children.append(node)

    def _generate_trie(self, level: int) -> str:
        children_str: str = ""
        curr: str
        for node in self.children:
            if len(self.children) > 0:
                curr = node._generate_trie(level+1)
            children_str += curr

        return "\n%s%s%s" % (
            " "*level,
            self.value,
            children_str,
        )

    def _add_word(self, word: str, w: int, children: list, i: int) -> list:
        if w >= len(word):
            return

        char: str = word[w]

        # main list of children nodes is empty, add first node to list
        if len(children) == 0:
            children.append(Trie(char))
            return self._add_word(
                word=word,
                w=w+1,
                children=children[0].children,
                i=0
            )

        # otherwise, if list already contains children, traverse them until you find a matching one, or none
        else:
            while i < len(children):
                node: Trie = children[i]

                # current node and char are the same
                if node.value == char:
                    return self._add_word(
                        word=word,
                        w=w+1,
                        children=node.children,
                        i=0
                    )
                i += 1

            children.append(Trie(char))
            return self._add_word(
                word=word,
                w=w+1,
                children=children[len(children)-1].children,
                i=0
            )

    def _search_word(self, word: str) -> bool:
        print(word)

    # public methods

    def search_word(self, word: str):
        return self._search_word(word=word)

    def add_word(self, word: str):
        self._add_word(word=word, w=0, children=self.children, i=0)

    def print(self):
        print(self._generate_trie(level=0))


t = Trie()
t.add_word("test")
t.add_word("xray")
t.add_word("toro")
t.add_word("xxxxx")
t.print()
