# -*- coding: big5 -*-
import sys

sys.path.append("C:\\Python24\\Lib")     # �[�J CPython 2.4 �����O�w���|
import pickle                            # �פJ pickle �Ҳ�
o = [1,2,3,{"one":1, "two":2}]           # �إ߽�������
print o                                  # �ˬd���󤺮e
pickle.dump(o, open("pickle.dump", "w")) # �N���� pickle ��, �s�J�ɮ�
