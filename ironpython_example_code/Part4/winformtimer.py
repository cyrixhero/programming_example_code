# -*- coding: big5 -*-
import clr
clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")
from System import *
from System.Windows.Forms import *
from System.Drawing import *

class App(Form):
        # ��l�Ƥ�k
        def __init__(self):
                # �p�ɾ����
                self.timer1 = Timer()
                self.timer1.Interval= 1000
                self.timer1.Tick += self.timer1_tick

                # ��ܥΪ����ұ��
                self.label1 = Label()
                self.label1.AutoSize = True
                self.label1.Location = Point(41, 22)
                self.label1.Text = "00:00:00"
                self.label1.Font = Font("Microsoft JhengHei", 
                                        20.0, FontStyle.Regular)
                self.Controls.Add(self.label1)

                clientwidth = 215

                # �}�l���s���
                b1 = Button()
                b1.Location = Point((clientwidth - b1.Width * 2)/3, 68)
                b1.Text = u"�}�l"
                b1.Click += self.start_click
                self.Controls.Add(b1)

                # ������s���
                b2 = Button()
                b2.Location = Point(
                        (clientwidth - b1.Width * 2)/3*2 + b1.Width , 68)

                b2.Text = u"����"
                b2.Click += self.stop_click
                self.Controls.Add(b2)

                # �]�w�����j�p
                self.ClientSize = Size(clientwidth, 103)
                self.Text = u"�X��"
                self.StartPosition = FormStartPosition.CenterScreen

        # �p�ɾ����ƥ�B�z��
        def timer1_tick(self, sender, e):
                self.starttime = self.starttime + TimeSpan(0,0,1)
                self.label1.Text = self.starttime.ToString()

        # �}�l���s���ƥ�B�z��
        def start_click(self, sender, e):
                self.starttime = TimeSpan(0,0,0)
                self.label1.Text = self.starttime.ToString()
                self.timer1.Start()

        # ������s���ƥ�B�z��
        def stop_click(self, sender, e):
                self.timer1.Stop()

# ����Ҳծɪ��ʧ@
if __name__ == "__main__":
        app = App()
        Application.Run(app)
