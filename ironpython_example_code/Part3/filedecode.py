# -*- coding: big5 -*-
import sys

# �H�G�i��Ҧ��}�� Big5 ���ɮ�
f = open("test.txt", "rb")
for line in f:
    # �ন Unicode
    wk = line.decode("big5")
    print wk
# �����ɮ�
first.close()
