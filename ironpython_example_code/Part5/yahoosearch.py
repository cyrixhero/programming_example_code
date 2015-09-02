# -*- coding: big5 -*-
import clr                                # �פJ clr
clr.AddReference("System")                # �s�W�Ѧ� System
clr.AddReference("System.Web")            # �s�W�Ѧ� System.Web
from System.Net import *                  # �פJ System.Net

# Yahoo Search �� URL
yahoosearchurl = "http://api.search.yahoo.co.jp/WebSearchService/V1/webSearch"
yahooappid = "YahooDemo"                  # �]�w Yahoo ���ε{�� ID
def setappid(appid = "YahooDemo"):
        global yahooappid                 # �w�q�����ܼ�
        yahooappid = appid

def getappid():
        return yahooappid

# �I�s Yahoo Search
def dosearch(query = u"�x�_", result = 2):
        import yahooxml                   # �q XML ���X��ƪ��Ҳ�
        client = WebClient()              # �إ� WebClinet ����
        # �إ߬d�ߤ޼�
        querystring = getquerystring(query, result)
        # �}�ҫ��w�� URL, ���oŪ���Ϊ� FileStream
        fs = client.OpenRead(yahoosearchurl + querystring)
        data = yahooxml.getdata(fs)       # ���X XML ���
        fs.Close()                        # �����ɮצ�y
        return data

# �إ߬d�ߤ޼�, ���ন URL �s�X
def getquerystring(query, result):
        import System.Web as Web
        # language=tzh �N��j�M�c�餤����
        param = "language=tzh&appid=" + yahooappid + "&query="
        # �N�j�M�r���ন URL �s�X
        param = param + Web.HttpUtility.UrlEncode(query)
        param = param +  "&results=" + str(result)
        return "?" + param

