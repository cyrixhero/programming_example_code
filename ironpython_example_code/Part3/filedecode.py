# -*- coding: big5 -*-
import sys

# 以二進位模式開啟 Big5 的檔案
f = open("test.txt", "rb")
for line in f:
    # 轉成 Unicode
    wk = line.decode("big5")
    print wk
# 關閉檔案
first.close()
