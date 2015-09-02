# -*- coding: big5 -*-
# 使用新型類別 __slots__ 的範例
class Capsule(object):
        __slots__ = ["a", "b"]  # 限定使用 a 與 b 屬性
        def __init__(self):     # 初始化用的特殊方法
                self.a = 1      # 指派 a 屬性的值

