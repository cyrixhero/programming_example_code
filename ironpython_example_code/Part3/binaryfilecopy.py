# -*- coding: big5 -*-
import sys

# 以二進位複製檔案
f1 = open("test.png", "rb")     # 輸入檔
f2 = open("test2.png", "wb")    # 複製目標
f2.write(f1.read())             # 複製檔案內容
# 關閉檔案
f1.close()
f2.close()
