# -*- coding: big5 -*-
import sys

# �H�G�i��ƻs�ɮ�
f1 = open("test.png", "rb")     # ��J��
f2 = open("test2.png", "wb")    # �ƻs�ؼ�
f2.write(f1.read())             # �ƻs�ɮפ��e
# �����ɮ�
f1.close()
f2.close()
