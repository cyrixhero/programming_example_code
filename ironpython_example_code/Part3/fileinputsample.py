# -*- coding: big5 -*-
import sys

sys.path.append("C:\\Python24\\Lib")    # �[�J CPython 2.4 �����O�w���|
import fileinput                        # �פJ fileinput
for line in fileinput.input():
        # �q�޼ƫ��w���ɮשμзǿ�J�@��Ū���@���ƳB�z
        tsv = line.split()              # �H�ťզr������ list
        print "|".join(tsv)             # �N�����H '|' �s�_�����

#
#  �u^Z�v: ���@�� [CTRL]+[Z] ������J�B�ĤG�����}�j��
#

fileinput.close()                       # ���� fileinput �ǦC
