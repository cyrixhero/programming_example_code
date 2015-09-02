# -*- coding: big5 -*-
# 定義名為 Bookurl 的類別
class Bookurl:
    g_url = ""   
    # 顯示應用目標的方法
    def print_outlines(self):
        print "This is a Bookurl class"
    # 設定 URL 的方法
    def set_url(self, url):
        self.url = url
    # 取得 URL 的方法
    def get_url(self):
        return self.url
    # 初始化用的特殊方法
    def __init__(self, *url):
        if len(url) != 0:
            self.url = url[0]
    # 轉換成字串的特殊方法
    def __str__(self):
        return "g_url=" + Bookurl.g_url + " ,self.url=" + self.url

