# -*- coding: big5 -*-
import sys

sys.path.append("C:\\Python24\\Lib")    # �[�J CPython 2.4 �����O�w���|
import pickle                           # �פJ pickle �Ҳ�
o = pickle.load(open("pickle.dump"))    # �q�ɮ״_�쪫��
print o                                 # �ˬd���󤺮e
