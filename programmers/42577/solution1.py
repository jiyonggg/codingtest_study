def make_trie():
    root = dict()
    return root

def insert_word(root, word):
    node = root

    for char in word:
        if char not in node:
            node[char] = dict()
        node = node[char]
    
    node["end"] = "end"

def has_prefix(root, word):
    node = root

    for char in word:
        if "end" in node.keys():
            return True

        node = node[char]

def solution(phone_book):
    root = make_trie()

    for tel in phone_book:
        insert_word(root, tel)

    for tel in phone_book:
        if has_prefix(root, tel):
            return False
    
    return True