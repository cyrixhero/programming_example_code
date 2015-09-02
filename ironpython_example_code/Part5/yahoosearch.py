# -*- coding: big5 -*-
import clr                                # 匯入 clr
clr.AddReference("System")                # 新增參考 System
clr.AddReference("System.Web")            # 新增參考 System.Web
from System.Net import *                  # 匯入 System.Net

# Yahoo Search 的 URL
yahoosearchurl = "http://api.search.yahoo.co.jp/WebSearchService/V1/webSearch"
yahooappid = "YahooDemo"                  # 設定 Yahoo 應用程式 ID
def setappid(appid = "YahooDemo"):
        global yahooappid                 # 定義全域變數
        yahooappid = appid

def getappid():
        return yahooappid

# 呼叫 Yahoo Search
def dosearch(query = u"台北", result = 2):
        import yahooxml                   # 從 XML 取出資料的模組
        client = WebClient()              # 建立 WebClinet 實體
        # 建立查詢引數
        querystring = getquerystring(query, result)
        # 開啟指定的 URL, 取得讀取用的 FileStream
        fs = client.OpenRead(yahoosearchurl + querystring)
        data = yahooxml.getdata(fs)       # 取出 XML 資料
        fs.Close()                        # 關閉檔案串流
        return data

# 建立查詢引數, 並轉成 URL 編碼
def getquerystring(query, result):
        import System.Web as Web
        # language=tzh 代表搜尋繁體中文資料
        param = "language=tzh&appid=" + yahooappid + "&query="
        # 將搜尋字串轉成 URL 編碼
        param = param + Web.HttpUtility.UrlEncode(query)
        param = param +  "&results=" + str(result)
        return "?" + param

