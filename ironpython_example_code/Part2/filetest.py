# -*- coding: big5 -*-
import sys

# �󴫹w�]�s�X�覡
sys.setdefaultencoding("big5")
# �}�Ҳ� 1 �Ӥ޼Ʀr����w���ɮ�
first = open(sys.argv[1], 'r')
# �}�Ҳ� 2 �Ӥ޼Ʀr����w���ɮ�
second = open(sys.argv[2], 'w')
# ����ɦW
print u'��J�ɦW�O ', sys.argv[1]
print u'��X�ɦW�O ', sys.argv[2]
# ��X�ɮפ��e
for line in first:
        second.write(line)
# �����ɮ�
first.close()
second.close()
raw_input()
