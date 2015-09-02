# -*- coding: big5 -*-
import sys

sys.path.append("C:\\Python24\\Lib")    # 加入 CPython 2.4 的類別庫路徑
import StringIO                         # 匯入 StringIO 模組
f = StringIO.StringIO()                 # 建立虛擬檔案物件
f.write("a" * 2)                        # 寫入 2 個相同字元
f.write("b" * 2)
f.write("c" * 2)
f.write("d" * 2)
f.write("e" * 2)
f.seek(0)                               # 讀寫位置回到檔頭
print f.read()                          # 讀取檔案內容
f.seek(6)                               # 讀寫位置移到第 7 個字元
print f.read()                          # 讀取檔案內容
f.close()                               # 關閉虛擬檔案, 釋放記憶體
