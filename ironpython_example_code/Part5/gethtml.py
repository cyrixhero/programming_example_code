# -*- coding: big5 -*-
import clr                              # �פJ clr
clr.AddReference("System")              # �[�J�Ѧ� System
from System.Net import *                # �פJ System.Net
from System.Text import *               # �פJ System.Text
import cStringIO                        # �פJ cStringIO

def gethtmldata(url="http://www.python.org/", enc="utf-8"):
        client = WebClient()            # �إ� WebClient ����
        if enc == "utf-8":              # �]�w�s�X
                myenc = Encoding.UTF8
        else:
                myenc = Encoding.GetEncoding(encode)
        client.Encoding = myenc         # �]�w URL �s�X
        s = client.DownloadString(url)  # ���o URL ���V�����
        f = cStringIO.StringIO()        # �إ� StringIO ����
        f.write(s)                      # �g�X���
        f.seek(0)                       # �j�M��m��^�}�Y
        return f                        # �^�� StringIO ����

