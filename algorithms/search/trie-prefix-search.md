# Trie and Prefix Search

```python
##
# Disclaimer
# Taken with a minor modifications from
# https://albertauyeung.github.io/2020/06/15/python-trie.html/
##

import typing


class TrieNode:
    def __init__(self, char):
        self.char = char
        self.is_end = False
        self.counter = 0
        self.children = {}


class Trie:
    def __init__(self):
        self.root = TrieNode("")

    def insert(self, word):
        node = self.root

        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node

        node.is_end = True
        node.counter += 1

    def suggest(self, prefix):
        node = self.root

        for char in prefix:
            if char in node.children:
                node = node.children[char]
            else:
                return []

        words = self._dfs(node, prefix[:-1], [])

        return sorted(words)

    def _dfs(self, node: TrieNode, prefix, words) -> typing.List:
        if node.is_end:
            words.append((prefix + node.char, node.counter))

        for child in node.children.values():
            self._dfs(child, prefix + node.char, words)

        return words
```