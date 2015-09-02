# -*- coding: big5 -*-
import clr
clr.AddReference("System.Xml")
from System.Xml import *

# 以檔案串流建立 XmlDocument
def load(filename):
        xmldoc = XmlDocument()
        xmldoc.Load(filename)
        return xmldoc

# 建立 XmlNamespaceManager
# (因為 Yahoo 的搜尋結果位於沒有 prefix 的命名空間內)
def addnamespace(xmldoc):
        nsmgr = XmlNamespaceManager(xmldoc.NameTable)
        nsmgr.AddNamespace("ya", "urn:yahoo:jp:srch")
        return nsmgr

# 傳入串流或 XML 檔名, 建立 dict
def getdata(xmlstream="yahoosearch.xml"):
        # 建立 XmlDocument
        xmldoc = load(xmlstream)
        # 加入 XML 命名空間
        nsmgr = addnamespace(xmldoc)
        # 建立 Result 節點清單
        list = xmldoc.SelectNodes("/ya:ResultSet/ya:Result", nsmgr)
        # 建立 Title, Summary, Url 的清單
        results = []
        for r in list:
                title = r.SelectSingleNode("ya:Title", nsmgr).InnerText
                summary = r.SelectSingleNode("ya:Summary", nsmgr).InnerText
                url = r.SelectSingleNode("ya:Url", nsmgr).InnerText
                results.append([title, summary, url])
        # 取得搜尋結果的控制資訊
        totalresults = xmldoc.SelectSingleNode(
                "/ya:ResultSet/@totalResultsAvailable", nsmgr).Value
        totalreturned = xmldoc.SelectSingleNode(
                "/ya:ResultSet/@totalResultsReturned", nsmgr).Value
        # 建立回傳的 dict
        ret = dict()
        ret["totalResultsAvailable"] = totalresults
        ret["totalResultsReturned"] = totalreturned
        ret["Results"] = results

        return ret
