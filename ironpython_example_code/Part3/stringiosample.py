# -*- coding: big5 -*-
import sys

sys.path.append("C:\\Python24\\Lib")    # �[�J CPython 2.4 �����O�w���|
import StringIO                         # �פJ StringIO �Ҳ�
f = StringIO.StringIO()                 # �إߵ����ɮת���
f.write("a" * 2)                        # �g�J 2 �ӬۦP�r��
f.write("b" * 2)
f.write("c" * 2)
f.write("d" * 2)
f.write("e" * 2)
f.seek(0)                               # Ū�g��m�^�����Y
print f.read()                          # Ū���ɮפ��e
f.seek(6)                               # Ū�g��m����� 7 �Ӧr��
print f.read()                          # Ū���ɮפ��e
f.close()                               # ���������ɮ�, ����O����
