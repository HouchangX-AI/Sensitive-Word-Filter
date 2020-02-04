"""
Encoding: utf-8
Author: April
Email: imlpliang@gmail.com
CreateTime: 2020-01-18 2:21
Description: test.py
Version: 1.0
"""
import time
from SensitiveWordFilter import DFAFilter
from SensitiveWordFilter import AcAutomationFilter

if __name__ == "__main__":
    start_time = time.time()

    """
    dfa_filter = DFAFilter()

    dfa_filter.readFile("./data4sensitive/")
    # dfa_filter.readFile("./data4sensitive/敏感词.txt")

    # text = "在哪儿呢，你是不是傻逼，TMD找不到地方。"
    text = "小爱同学你这个大傻x，这真的有气枪和炸药吗？这家微店。"

    text_conver = dfa_filter.coverSensitive(text, "*")
    print(text_conver)

    text_check = dfa_filter.checkSentence(text)
    print(text_check)
    """

    ac_filter = AcAutomationFilter()
    ac_filter.readFile("./data4sensitive/敏感词.txt")

    text = "在哪儿新浪，你是习近平"
    text_check = ac_filter.checkSentence(text)
    print(text_check)

    print('总共耗时：' + str(time.time() - start_time) + 's')