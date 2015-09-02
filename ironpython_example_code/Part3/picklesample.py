# -*- coding: big5 -*-
import sys

sys.path.append("C:\\Python24\\Lib")     # 加入 CPython 2.4 的類別庫路徑
import pickle                            # 匯入 pickle 模組
o = [1,2,3,{"one":1, "two":2}]           # 建立複雜物件
print o                                  # 檢查物件內容
pickle.dump(o, open("pickle.dump", "w")) # 將物件 pickle 化, 存入檔案
