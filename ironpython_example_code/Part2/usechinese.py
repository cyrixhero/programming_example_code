# -*- coding: big5 -*-
import sys

# �󴫹w�]�s�X�覡
sys.setdefaultencoding("big5")
# �}�� Big5 �ɮר���ܥX��
first = open(u"����.txt", "r")
for line in first:
    print line
# �����ɮ�
first.close()
