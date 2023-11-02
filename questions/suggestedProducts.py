from typing import List


class TrieNode:
    def __init__(self, char):
        self.char = char
        self.end_of_word = False
        self.children = {}


class Trie:
    def __init__(self):
        self.root = TrieNode("")

    def insert(self, word):
        node = self.root

        for char in word:
            if node.children.get(char):
                node = node.children.get(char)
            else:
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node

        node.end_of_word = True

    def dfs(self, node, pre):
        if node.end_of_word:
            self.word.append((pre + node.char))

        for child in node.children.values():
            self.dfs(child, pre + node.char)

    def search(self, chars):
        node = self.root

        for char in chars:
            if node.children.get(char):
                node = node.children.get(char)
            else:
                return []

        self.word = []
        self.dfs(node, chars[:-1])

        return self.word


class Solution:
    def suggestedProducts(
        self, products: List[str], searchWord: str
    ) -> List[List[str]]:
        # trie = Trie()
        # suggested_products = []
        #
        # for product in products:
        #     trie.insert(product)
        #
        # for i in range(1, len(searchWord) + 1):
        #     output = ["".join(item) for item in trie.search(searchWord[:i])]
        #
        #     suggested_products.append(output[:3])
        # print(suggested_products)
        #
        # return suggested_products

        res = []
        # Initializing empty string temp
        temp = ""

        # Sorting the list
        products.sort()

        # Looping through searchWord
        for word in searchWord:
            # Adding each character of searchWord to temp every iteration
            temp += word
            # Initialzing another empty list to keep the matching products
            res_inner = []
            # Looping through the products
            for j in range(len(products)):
                # Comparing the product upto the same length as temp instead of finding it in the entire product string
                if products[j][: len(temp)] == temp:
                    # Appending the found product to the inner list
                    res_inner.append(products[j])

            # Only considering lexicographically top 3 elements
            res.append(res_inner[:3])
            # Updating the products list to inner list to reduce the search space
            products = res_inner

        return res


solution = Solution()
solution.suggestedProducts(
    ["mobile", "mouse", "moneypot", "monitor", "mousepad"], "mouse"
)
