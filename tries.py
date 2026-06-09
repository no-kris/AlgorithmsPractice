from typing import Optional, Self


class TrieNode:
    def __init__(self) -> None:
        self.children = {}


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def search(self, word: str) -> Optional[TrieNode]:
        current_node = self.root
        for char in word:
            if current_node.children.get(char):
                current_node = current_node.children[char]
            else:
                return None
        return current_node

    def insert(self, word: str) -> Self:
        current_node = self.root
        for char in word:
            if current_node.children.get(char):
                current_node = current_node.children[char]
            else:
                new_node = TrieNode()
                current_node.children[char] = new_node
                current_node = new_node
        current_node.children["*"] = None
        return self

    def collect_all_words(self, words, node=None, word="") -> list:
        current_node = node or self.root
        for key, child in current_node.children.items():
            if key == "*":
                words.append(word)
            else:
                self.collect_all_words(words, child, word + key)
        return words

    def print_keys(self, node=None):
        current_node = self.root or node
        for key, child in current_node.children.items():
            print(key)
            if key == "*":
                return
            else:
                self.print_keys(child)

    def autocomplete(self, prefix):
        current_node = self.search(prefix)
        if not current_node:
            return None
        return self.collect_all_words([], current_node)

    def autocorrect(self, word):
        current_node = self.root
        prefix = ""
        for char in word:
            if current_node.children.get(char):
                current_node = current_node.children[char]
                prefix += char
        self.collect_all_words([], current_node, prefix)
