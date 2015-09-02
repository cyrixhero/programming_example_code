# -*- coding: big5 -*-
import clr
clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")
from System import *
from System.Windows.Forms import *
from System.Drawing import *

class App(Form):
        # 初始化方法
        def __init__(self):
                # 計時器控制項
                self.timer1 = Timer()
                self.timer1.Interval= 1000
                self.timer1.Tick += self.timer1_tick

                # 顯示用的標籤控制項
                self.label1 = Label()
                self.label1.AutoSize = True
                self.label1.Location = Point(41, 22)
                self.label1.Text = "00:00:00"
                self.label1.Font = Font("Microsoft JhengHei", 
                                        20.0, FontStyle.Regular)
                self.Controls.Add(self.label1)

                clientwidth = 215

                # 開始按鈕控制項
                b1 = Button()
                b1.Location = Point((clientwidth - b1.Width * 2)/3, 68)
                b1.Text = u"開始"
                b1.Click += self.start_click
                self.Controls.Add(b1)

                # 停止按鈕控制項
                b2 = Button()
                b2.Location = Point(
                        (clientwidth - b1.Width * 2)/3*2 + b1.Width , 68)

                b2.Text = u"停止"
                b2.Click += self.stop_click
                self.Controls.Add(b2)

                # 設定視窗大小
                self.ClientSize = Size(clientwidth, 103)
                self.Text = u"碼表"
                self.StartPosition = FormStartPosition.CenterScreen

        # 計時器的事件處理器
        def timer1_tick(self, sender, e):
                self.starttime = self.starttime + TimeSpan(0,0,1)
                self.label1.Text = self.starttime.ToString()

        # 開始按鈕的事件處理器
        def start_click(self, sender, e):
                self.starttime = TimeSpan(0,0,0)
                self.label1.Text = self.starttime.ToString()
                self.timer1.Start()

        # 停止按鈕的事件處理器
        def stop_click(self, sender, e):
                self.timer1.Stop()

# 執行模組時的動作
if __name__ == "__main__":
        app = App()
        Application.Run(app)
