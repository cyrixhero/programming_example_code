# -*- coding: big5 -*-
import clr  # 匯入 clr
# 新增 WPF 相關類別庫的參考
clr.AddReferenceByPartialName("PresentationCore")
clr.AddReferenceByPartialName("PresentationFramework")
clr.AddReferenceByPartialName("WindowsBase")
# 匯入必要模組
from System import *
from System.Windows import *
from System.Windows.Media import *
from System.Windows.Media.Animation import *
from System.Windows.Controls import *

class Win(Window):

        # 初始化方法
        def __init__(self):
                self.Title = u"動畫按鈕"
                self.Height = 300               # 設定視窗高度
                self.Width = 300                # 設定視窗寬度
                # 載入 myfirstwpf.xaml
                self.Content = LoadXaml("myfirstwpf.xaml")
                # Walk() 函式由 avalon 模組提供
                buttons = [n for n in Walk(self) if isinstance(n, Button)]
                # 滑鼠移到按鈕上的時候執行放大按鈕的動畫
                buttons[0].MouseEnter += self.myMouseEnter
                # 滑鼠離開按鈕的時候執行恢復原狀的動畫
                buttons[0].MouseLeave += self.myMouseLeave

        # 滑鼠移到按鈕上的時候呼叫的事件處理器
        def myMouseEnter(self, sender, e):
                myButton = sender
                myHeightAnimation = DoubleAnimation()
                myHeightAnimation.From = myButton.Height
                myHeightAnimation.To = 200.0
                myHeightAnimation.Duration = Duration(TimeSpan(0,0,3))
                myButton.BeginAnimation(Button.HeightProperty, 
                                        myHeightAnimation)

        # 滑鼠離開按鈕的時候呼叫的事件處理器
        def myMouseLeave(self, sender, e):
                myButton = sender
                myHeightAnimation = DoubleAnimation()
                myHeightAnimation.From = myButton.Height
                myHeightAnimation.To = 100.0
                myHeightAnimation.Duration = Duration(TimeSpan(0,0,1))
                myButton.BeginAnimation(Button.HeightProperty, 
                                        myHeightAnimation)

# 引用自 avalon.py 的 LoadXaml() 函式
def LoadXaml(filename):
    from System.IO import *
    from System.Windows.Markup import XamlReader
    f = FileStream(filename, FileMode.Open)
    try:
        element = XamlReader.Load(f)
    finally:
        f.Close()
    return element

# 引用自 avalon.py 的 Walk() 函式
def Walk(tree):
    yield tree
    if hasattr(tree, 'Children'):
        for child in tree.Children:
            for x in Walk(child):
                yield x
    elif hasattr(tree, 'Child'):
        for x in Walk(tree.Child):
            yield x
    elif hasattr(tree, 'Content'):
        for x in Walk(tree.Content):
            yield x

# 執行模組時的程式起始點
if __name__ == "__main__":
        app = Application()
        app.Run(Win())
