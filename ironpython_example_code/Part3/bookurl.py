# -*- coding: big5 -*-
# �w�q�W�� Bookurl �����O
class Bookurl:
    g_url = ""   
    # ������ΥؼЪ���k
    def print_outlines(self):
        print "This is a Bookurl class"
    # �]�w URL ����k
    def set_url(self, url):
        self.url = url
    # ���o URL ����k
    def get_url(self):
        return self.url
    # ��l�ƥΪ��S���k
    def __init__(self, *url):
        if len(url) != 0:
            self.url = url[0]
    # �ഫ���r�ꪺ�S���k
    def __str__(self):
        return "g_url=" + Bookurl.g_url + " ,self.url=" + self.url

