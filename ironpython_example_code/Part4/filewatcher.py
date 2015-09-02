# -*- coding: big5 -*-
from System import *                # 匯入 System
from System.IO import *             # 匯入 System.IO

class App:
        # 初始化方法
        def __init__(self, source = ".", target = "New"):
                self.checkfolder(source, False)            # 檢查複製來源目錄
                self._source = source                      # 留下複製來源
                self._target = target                      # 留下複製目標
                self.checkfolder(target,True)              # 檢查複製目標目錄
                self._w = FileSystemWatcher(source)        # 建立實體
                # 事件過濾器只監視 FileName
                self._w.NotifyFilter = NotifyFilters.FileName
                self._w.Created += self.created            # 登記事件處理器
                # 開始監視
                self.start()

        # 建立檔案的事件處理器
        def created(self, sender, e):
                self.movefile(e.Name)

        # 移動檔案的方法
        def movefile(self, filename):
                try:
                        source = Path.Combine(self._source, filename)
                        target = Path.Combine(self._target, filename)
                        File.Move(source, target)
                except:
                        raise u"無法移動檔案"
                print filename, u"已移動到新目錄"

        # 檢查目錄是否存在
        def checkfolder(self, folder, create = False):
                try:
                        ret = Directory.Exists(folder)     # 目錄已存在
                        if ret :
                                return
                        if create :                        # 建立新目錄
                                Directory.CreateDirectory(folder)
                                return
                finally:
                        pass
                raise u"檢查目錄時發生錯誤"

        # 停止監視
        def stop(self):
                self._w.EnableRaisingEvents = False

        # 開始監視
        def start(self):
                self._w.EnableRaisingEvents = True

import sys
# 模組被當成檔案執行
if __name__ == "__main__":
        
        count = len(sys.argv)
        if count == 2:         # 引數只有一個
                app = App(sys.argv[1])
        elif count > 2:        # 引數有兩個以上
                app = App(sys.argv[1], sys.argv[2])
        else:                  # 未指定引數
                app = App()
        print u"開始監視目錄"
        print u"按 Enter 結束監視"
        raw_input()            # 等待按鍵

