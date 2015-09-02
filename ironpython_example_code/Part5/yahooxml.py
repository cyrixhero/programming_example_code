# -*- coding: big5 -*-
import clr
clr.AddReference("System.Xml")
from System.Xml import *

# �H�ɮצ�y�إ� XmlDocument
def load(filename):
        xmldoc = XmlDocument()
        xmldoc.Load(filename)
        return xmldoc

# �إ� XmlNamespaceManager
# (�]�� Yahoo ���j�M���G���S�� prefix ���R�W�Ŷ���)
def addnamespace(xmldoc):
        nsmgr = XmlNamespaceManager(xmldoc.NameTable)
        nsmgr.AddNamespace("ya", "urn:yahoo:jp:srch")
        return nsmgr

# �ǤJ��y�� XML �ɦW, �إ� dict
def getdata(xmlstream="yahoosearch.xml"):
        # �إ� XmlDocument
        xmldoc = load(xmlstream)
        # �[�J XML �R�W�Ŷ�
        nsmgr = addnamespace(xmldoc)
        # �إ� Result �`�I�M��
        list = xmldoc.SelectNodes("/ya:ResultSet/ya:Result", nsmgr)
        # �إ� Title, Summary, Url ���M��
        results = []
        for r in list:
                title = r.SelectSingleNode("ya:Title", nsmgr).InnerText
                summary = r.SelectSingleNode("ya:Summary", nsmgr).InnerText
                url = r.SelectSingleNode("ya:Url", nsmgr).InnerText
                results.append([title, summary, url])
        # ���o�j�M���G�������T
        totalresults = xmldoc.SelectSingleNode(
                "/ya:ResultSet/@totalResultsAvailable", nsmgr).Value
        totalreturned = xmldoc.SelectSingleNode(
                "/ya:ResultSet/@totalResultsReturned", nsmgr).Value
        # �إߦ^�Ǫ� dict
        ret = dict()
        ret["totalResultsAvailable"] = totalresults
        ret["totalResultsReturned"] = totalreturned
        ret["Results"] = results

        return ret
