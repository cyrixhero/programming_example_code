# -*- coding: big5 -*-
import sys

sys.path.append("C:\\Python24\\Lib")    # 加入 CPython 2.4 的類別庫路徑
import pickle                           # 匯入 pickle 模組
o = pickle.load(open("pickle.dump"))    # 從檔案復原物件
print o                                 # 檢查物件內容
