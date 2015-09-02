# -*- coding: big5 -*-
import sys

sys.path.append("C:\\Python24\\Lib")    # 加入 CPython 2.4 的類別庫路徑
import fileinput                        # 匯入 fileinput
for line in fileinput.input():
        # 從引數指定的檔案或標準輸入一次讀取一行資料處理
        tsv = line.split()              # 以空白字元切成 list
        print "|".join(tsv)             # 將元素以 '|' 連起來顯示

#
#  「^Z」: 按一次 [CTRL]+[Z] 結束輸入、第二次離開迴圈
#

fileinput.close()                       # 關閉 fileinput 序列
