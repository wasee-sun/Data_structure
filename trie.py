class TrieNode:
    def __init__(self, val = None):
        self.val = val
        self.is_end = False
        self.children = []

class Trie:
    def __init__(self):
        self.root = TrieNode()
            
    def _find_ch(self, ch, ch_node):
        for child in ch_node.children:
            if child.val == ch:
                return child
        return False
    
    def search_word(self, word, prefix = False):
        return self._search_word(word, self.root, prefix)
    
    def _search_word(self, word, cur_node, prefix):
        cur_node = self._find_ch(word[0], cur_node)
        if not cur_node:
            return cur_node
        if len(word) == 1:
            if prefix:
                return cur_node
            if cur_node.is_end:
                return True
            else:
                return False
        return self._search_word(word[1:], cur_node, prefix)
        
    def insert(self, word):
        return self._insert(word, self.root)
    
    def _insert(self, word, cur_node):
        if word == "":
            return
        
        ch = word[0]
        ch_node = self._find_ch(ch, cur_node)
        
        if ch_node:
            if len(word) == 1:
                ch_node.is_end = True
            return self._insert(word[1:], ch_node)
        else:
            ch_node = TrieNode(ch)
            cur_node.children.append(ch_node)
            if len(word) == 1:
                ch_node.is_end = True
            return self._insert(word[1:], ch_node)
        
    def remove(self, word):
        if self._search_word(word, self.root):
            return self._remove(word, self.root)
        else:
            print("Word does not exist")
            return
    
    def _remove(self, word, cur_node):
        if len(word) == 1:
            for child in cur_node.children:
                if child.val == word[0]:
                    if len(child.children) != 0:
                        child.is_end = False
                    else:
                        cur_node.children.remove(child)
            return False
        cur_node = self._find_ch(word[0], cur_node)
        word = word[1:]
        ch_removed = self._remove(word, cur_node)
        
        if ch_removed:
            return ch_removed
        
        for child in cur_node.children:
            if child.val == word[0]:
                if child.is_end or len(child.children) != 0:
                    return True
                else:
                    cur_node.children.remove(child)
                    return False
                
    def get_all_words(self):
        return self._get_all_words(self.root, "")
    
    def _get_all_words(self, cur_node, word):
        elements = []
        if len(cur_node.children) == 0:
            return elements
        
        for child in cur_node.children:
            word = word + child.val
            if child.is_end:
                # print(word)
                elements.append(word)
            elements += self._get_all_words(child, word)
            word = word[:-1]
            
        return elements
    
    def autocomplete(self, prefix):
        prefix_node = self._search_word(prefix, self.root, True)
        if prefix_node:
            return self._get_all_words(prefix_node, prefix)
        else:
            return
        
    
if __name__ == "__main__":
    words = [
        "macaco", 
        "macaroni", 
        "macaron", 
        "machinable", 
        "machine", 
        "macromolecular",
        "macroscopic", 
        "macronuclear",
        ]
    
    trie = Trie()
    for word in words:
        trie.insert(word)
        
    print(trie.search_word("macaroni"))
    # print(trie.remove("macaron"))
    print(trie.get_all_words())
    print(trie.autocomplete("maca"))
    print("word")
        