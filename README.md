## 敏感词过滤  
本代码的敏感词过滤使用 DFA算法 和 AC自动机 实现。

### 敏感词库
常用敏感词词库，包括：色情、政治、广告等方面。

### Trie树
Trie树，又称单词查找树，是一种树形结构，哈希树的变种。其典型应用是用于统计，排序和保存大量的字符串（但不仅限字符串），所以经常被搜索引擎系统用于文本词频统计。

优点：利用字符串的公共前缀来减少查询时间，最大限度地减少无谓的字符串比较，查询效率比哈希树高。

具有以下特征：
- 根节点不包含字符，除根节点外的每一个子节点都包含一个字符。
- 从根节点到某一节点，路径上经过的字符连接起来，就是该节点对应的字符串。
- 每个单词的公共前缀作为一个字符节点保存。

### DFA算法
DFA，Deterministic Finite Automaton, 即确定有穷自动机。

数据结构：Trie树。

原理：有一个有限状态集合和一些从一个状态通向另一个状态的边，每条边上标记有一个符号，其中一个状态是初态，某些状态是终态。但不同于不确定的有限自动机，DFA中不会有从同一状态出发的两条边标志有相同的符号。

### AC自动机

与DFA相比，在构建时多一些指针等。

### 使用方法
```
from sensitive_word_filter import DFAFilter

dfa_filter = DFAFilter()

dfa_filter.readFile("./data4sensitive/")
# dfa_filter.readFile("./data4sensitive/敏感词.txt")

# text = "在哪儿呢，你是不是傻X，TMD找不到地方。"
text = "小爱同学你这个大傻x，这真的有气枪和炸药吗？这家微店。"

text_conver = dfa_filter.coverSensitive(text, "*")
print(text_conver)
# 小爱同学你这个大**，这真*有**和**吗？这家**。

text_check = dfa_filter.checkSentence(text)
print(text_check)
# True
```
