# -*- coding: big5 -*-
import sys

# 更換預設編碼方式
sys.setdefaultencoding("big5")
# 開啟第 1 個引數字串指定的檔案
first = open(sys.argv[1], 'r')
# 開啟第 2 個引數字串指定的檔案
second = open(sys.argv[2], 'w')
# 顯示檔名
print u'輸入檔名是 ', sys.argv[1]
print u'輸出檔名是 ', sys.argv[2]
# 輸出檔案內容
for line in first:
        second.write(line)
# 關閉檔案
first.close()
second.close()
raw_input()
