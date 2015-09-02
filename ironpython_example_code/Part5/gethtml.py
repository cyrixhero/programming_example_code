# -*- coding: big5 -*-
import clr                              # 匯入 clr
clr.AddReference("System")              # 加入參考 System
from System.Net import *                # 匯入 System.Net
from System.Text import *               # 匯入 System.Text
import cStringIO                        # 匯入 cStringIO

def gethtmldata(url="http://www.python.org/", enc="utf-8"):
        client = WebClient()            # 建立 WebClient 實體
        if enc == "utf-8":              # 設定編碼
                myenc = Encoding.UTF8
        else:
                myenc = Encoding.GetEncoding(encode)
        client.Encoding = myenc         # 設定 URL 編碼
        s = client.DownloadString(url)  # 取得 URL 指向的資料
        f = cStringIO.StringIO()        # 建立 StringIO 實體
        f.write(s)                      # 寫出資料
        f.seek(0)                       # 搜尋位置返回開頭
        return f                        # 回傳 StringIO 物件

