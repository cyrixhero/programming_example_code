# -*- coding: big5 -*-
import clr  # �פJ clr
# �s�W WPF �������O�w���Ѧ�
clr.AddReferenceByPartialName("PresentationCore")
clr.AddReferenceByPartialName("PresentationFramework")
clr.AddReferenceByPartialName("WindowsBase")
# �פJ���n�Ҳ�
from System import *
from System.Windows import *
from System.Windows.Media import *
from System.Windows.Media.Animation import *
from System.Windows.Controls import *

class Win(Window):

        # ��l�Ƥ�k
        def __init__(self):
                self.Title = u"�ʵe���s"
                self.Height = 300               # �]�w��������
                self.Width = 300                # �]�w�����e��
                # ���J myfirstwpf.xaml
                self.Content = LoadXaml("myfirstwpf.xaml")
                # Walk() �禡�� avalon �Ҳմ���
                buttons = [n for n in Walk(self) if isinstance(n, Button)]
                # �ƹ�������s�W���ɭ԰����j���s���ʵe
                buttons[0].MouseEnter += self.myMouseEnter
                # �ƹ����}���s���ɭ԰����_�쪬���ʵe
                buttons[0].MouseLeave += self.myMouseLeave

        # �ƹ�������s�W���ɭԩI�s���ƥ�B�z��
        def myMouseEnter(self, sender, e):
                myButton = sender
                myHeightAnimation = DoubleAnimation()
                myHeightAnimation.From = myButton.Height
                myHeightAnimation.To = 200.0
                myHeightAnimation.Duration = Duration(TimeSpan(0,0,3))
                myButton.BeginAnimation(Button.HeightProperty, 
                                        myHeightAnimation)

        # �ƹ����}���s���ɭԩI�s���ƥ�B�z��
        def myMouseLeave(self, sender, e):
                myButton = sender
                myHeightAnimation = DoubleAnimation()
                myHeightAnimation.From = myButton.Height
                myHeightAnimation.To = 100.0
                myHeightAnimation.Duration = Duration(TimeSpan(0,0,1))
                myButton.BeginAnimation(Button.HeightProperty, 
                                        myHeightAnimation)

# �ޥΦ� avalon.py �� LoadXaml() �禡
def LoadXaml(filename):
    from System.IO import *
    from System.Windows.Markup import XamlReader
    f = FileStream(filename, FileMode.Open)
    try:
        element = XamlReader.Load(f)
    finally:
        f.Close()
    return element

# �ޥΦ� avalon.py �� Walk() �禡
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

# ����Ҳծɪ��{���_�l�I
if __name__ == "__main__":
        app = Application()
        app.Run(Win())
