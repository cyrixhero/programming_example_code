# -*- coding: big5 -*-
import sys

# 更換預設編碼方式
sys.setdefaultencoding("big5")
# 開啟 Big5 檔案並顯示出來
first = open(u"中文.txt", "r")
for line in first:
    print line
# 關閉檔案
first.close()
