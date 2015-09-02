# -*- coding: big5 -*-
# 使用 _ (底線) 隱藏屬性與方法的範例
class Capsule:
        sizeA = 10      # 一般屬性
        _sizeB = 20     # 加上一個 _ 的屬性
        __sizeC = 30    # 加上兩個 _ 的屬性

