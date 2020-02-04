"""
Encoding: utf-8
Author: April
Email: imlpliang@gmail.com
CreateTime: 2020-01-18 1:57
Description: SensitiveWordFilter.py
Version: 1.0
"""
import os


class DFAFilter:
    """
    DFA
    """
    def __init__(self):
        """
        Initializes the sensitive word trie.
        """
        self.root = {}
        self.word_end = "END"

    def insert(self, word):
        """
        :function: Inserts a word into the trie.
        :param word: str
        :return: void
        """
        curr_node = self.root
        for ch in word:
            if ch not in curr_node:
                curr_node[ch] = {}
            curr_node = curr_node[ch]
        curr_node[self.word_end] = True

    def readFile(self, file_path):
        """
        :function: Read sensitive word files or directories
        :param file_path: file path or directory path
        :return: void
        """
        if os.path.isfile(file_path):
            with open(file_path, mode='r', encoding='utf-8') as file_handle:
                for word in file_handle:
                    self.insert(word.strip().lower())
        if os.path.isdir(file_path):
            for root, dirs, files in os.walk(file_path, topdown=False):
                for file in files:
                    curr_path = os.path.join(root, file)
                    print(curr_path)
                    with open(curr_path, 'r', encoding='utf-8') as file_handle:
                        for word in file_handle:
                            self.insert(word.strip().lower())
        del self.root[self.word_end]

    def search(self, word):
        """
        :function: Returns if the word is in the trie.
        :param word: str
        :return: bool
        """
        curr_node = self.root
        for ch in word.lower():
            if ch not in curr_node:
                return False
            curr_node = curr_node[ch]
        # Doesn't end here
        if self.word_end not in curr_node:
            return False
        return True

    def startsWith(self, prefix):
        """
        :function: Returns if there is any word in the trie that starts with the given prefix.
        :param prefix: str
        :return: bool
        """
        curr_node = self.root
        for ch in prefix.lower():
            if ch not in curr_node:
                return False
            curr_node = curr_node[ch]
        return True

    def checkSentence(self, text):
        """
        :function: Returns if the text contains sensitive words.
        :param text: a Chinese text
        :return: bool
        """
        text = text.lower()
        index = 0
        while index < len(text):
            curr_node = self.root.copy()
            curr_text = text[index:]
            temp_index = 0
            count = 0
            while temp_index < len(curr_text) and curr_text[temp_index] in curr_node:
                curr_node = curr_node[curr_text[temp_index]]
                temp_index += 1
                count += 1
            if self.word_end in curr_node:
                # sensitive_word = curr_text[:count]
                # print(sensitive_word)
                return True
            index += 1
        return False

    def coverSensitive(self, text, cover_str):
        """
        :function: Returns a paragraph of Chinese text replacing sensitive words with *
        :param text: a Chinese text
        :param cover_str: a character that replaces a sensitive word
        :return:
        """
        text = text.lower()
        result = ''
        index = 0
        len_text = len(text)
        while index < len_text:
            count = 0
            curr_node = self.root.copy()
            # temp = ''
            while index < len_text and text[index] in curr_node:
                curr_node = curr_node[text[index]]
                count += 1
                index += 1
            if count == 0:
                temp = text[index]
                index += 1
            elif self.word_end in curr_node:  # and count != 0
                temp = cover_str * count
            else:
                temp = text[index-count:index]
            result += temp
        return result




class node(object):
    def __init__(self):
        self.next = {}
        self.fail = None
        self.isWord = False
        self.word = ""


class AcAutomationFilter:
    """
    Ac Automation
    """
    def __init__(self):
        self.root = node()

    def insertWord(self, word):
        curr_node = self.root
        for char in word:
            if char not in curr_node.next:
                curr_node.next[char] = node()
            curr_node = curr_node.next[char]
        curr_node.isWord = True
        curr_node.word = word

    def readFile(self, file_path):
        if os.path.isfile(file_path):
            with open(file_path, mode='r', encoding='utf-8') as file_handle:
                for word in file_handle:
                    self.insertWord(word.strip().lower())
        if os.path.isdir(file_path):
            for root, dirs, files in os.walk(file_path, topdown=False):
                for file in files:
                    curr_path = os.path.join(root, file)
                    print(curr_path)
                    with open(curr_path, 'r', encoding='utf-8') as file_handle:
                        for word in file_handle:
                            self.insertWord(word.strip().lower())
        self.root.isWord = False
        self.root.word = ''

    def checkSentence(self, text):
        """
        :function: Returns if the text contains sensitive words.
        :param text: a Chinese text
        :return: bool
        """
        text = text.lower()
        result = []
        index = 0
        while index < len(text):
            curr_node = self.root
            curr_text = text[index:]
            temp_index = 0
            while temp_index < len(curr_text) and curr_text[temp_index] in curr_node.next:
                curr_node = curr_node.next[curr_text[temp_index]]
                temp_index += 1
            if curr_node.isWord:
                result.append(curr_node.word)
            index += 1
        # print(result)
        if len(result) != 0:
            return True
        else:
            return False

