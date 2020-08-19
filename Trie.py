#!/usr/bin/env python
# coding: utf-8

# # Building a Trie in Python
# 
# Before we start let us reiterate the key components of a Trie or Prefix Tree. A trie is a tree-like data structure that stores a dynamic set of strings. Tries are commonly used to facilitate operations like predictive text or autocomplete features on mobile phones or web search.
# 
# Before we move into the autocomplete function we need to create a working trie for storing strings.  We will create two classes:
# * A `Trie` class that contains the root node (empty string)
# * A `TrieNode` class that exposes the general functionality of the Trie, like inserting a word or finding the node which represents a prefix.
# 
# Give it a try by implementing the `TrieNode` and `Trie` classes below!

# In[3]:


## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}
    
    def insert(self, char):
        if char not in self.children:
            self.children[char] = TrieNode()
        
        return self.children[char]
            
    
## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        current = self.root
        
        for letter in word:
            current = current.insert(letter)
            
        current.is_word = True

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        current = self.root
        
        for letter in prefix:
            if letter not in current.children:
                return False
            else:
                current = current.children[letter]
                
        return current
            


# In[4]:


a = Trie()
a.insert('Hi')
a.find('Hi')


# # Finding Suffixes
# 
# Now that we have a functioning Trie, we need to add the ability to list suffixes to implement our autocomplete feature.  To do that, we need to implement a new function on the `TrieNode` object that will return all complete word suffixes that exist below it in the trie.  For example, if our Trie contains the words `["fun", "function", "factory"]` and we ask for suffixes from the `f` node, we would expect to receive `["un", "unction", "actory"]` back from `node.suffixes()`.
# 
# Using the code you wrote for the `TrieNode` above, try to add the suffixes function below. (Hint: recurse down the trie, collecting suffixes as you go.)

# In[86]:


## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}
        self.words = []
    
    def insert(self, char):
        if char not in self.children:
            self.children[char] = TrieNode()
        
        return self.children[char]
        

    def suffixes(self, suffix = '', words = None):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point
        if words is None:
            words = []
        if self.children:
            for letter, node in self.children.items():
                if node.is_word:
                    words.append(suffix + letter)

                node.suffixes(suffix + letter, words)
               
        return words
# In[87]:


tri = Trie()
tri.insert('hello')
tri.insert('hi')
tri.insert('hell')
tri.insert('hellion')
tri.insert('bat')
tri.insert('bar')


tri.root.children['h'].children['i'].is_word


# In[88]:


tri.root.children['b'].suffixes()


# # Testing it all out
# 
# Run the following code to add some words to your trie and then use the interactive search box to see what your code returns.

# In[89]:


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)


# In[ ]:


from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact
def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')
interact(f,prefix='');