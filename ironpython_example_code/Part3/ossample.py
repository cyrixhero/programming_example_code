# -*- coding: shift_jis -*-
import sys

sys.path.append("C:\\Python24\\Lib")     # CPython���C�u�����̃p�X��ǉ�����
import os                                # os�̃C���|�[�g
# os���W���[����walk()�֐����g�����t�H���_�̍ċA����
for dpath, dnames, fnames in os.walk("./"):
        for fname in fnames:             # �t�@�C�����Ń��[�v
                if fname.endswith("py"): # �g���q�𔻒f����
                        print fname      # �t�@�C������\��
