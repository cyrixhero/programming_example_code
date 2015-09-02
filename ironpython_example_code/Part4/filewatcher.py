# -*- coding: big5 -*-
from System import *                # �פJ System
from System.IO import *             # �פJ System.IO

class App:
        # ��l�Ƥ�k
        def __init__(self, source = ".", target = "New"):
                self.checkfolder(source, False)            # �ˬd�ƻs�ӷ��ؿ�
                self._source = source                      # �d�U�ƻs�ӷ�
                self._target = target                      # �d�U�ƻs�ؼ�
                self.checkfolder(target,True)              # �ˬd�ƻs�ؼХؿ�
                self._w = FileSystemWatcher(source)        # �إ߹���
                # �ƥ�L�o���u�ʵ� FileName
                self._w.NotifyFilter = NotifyFilters.FileName
                self._w.Created += self.created            # �n�O�ƥ�B�z��
                # �}�l�ʵ�
                self.start()

        # �إ��ɮת��ƥ�B�z��
        def created(self, sender, e):
                self.movefile(e.Name)

        # �����ɮת���k
        def movefile(self, filename):
                try:
                        source = Path.Combine(self._source, filename)
                        target = Path.Combine(self._target, filename)
                        File.Move(source, target)
                except:
                        raise u"�L�k�����ɮ�"
                print filename, u"�w���ʨ�s�ؿ�"

        # �ˬd�ؿ��O�_�s�b
        def checkfolder(self, folder, create = False):
                try:
                        ret = Directory.Exists(folder)     # �ؿ��w�s�b
                        if ret :
                                return
                        if create :                        # �إ߷s�ؿ�
                                Directory.CreateDirectory(folder)
                                return
                finally:
                        pass
                raise u"�ˬd�ؿ��ɵo�Ϳ��~"

        # ����ʵ�
        def stop(self):
                self._w.EnableRaisingEvents = False

        # �}�l�ʵ�
        def start(self):
                self._w.EnableRaisingEvents = True

import sys
# �ҲճQ���ɮװ���
if __name__ == "__main__":
        
        count = len(sys.argv)
        if count == 2:         # �޼ƥu���@��
                app = App(sys.argv[1])
        elif count > 2:        # �޼Ʀ���ӥH�W
                app = App(sys.argv[1], sys.argv[2])
        else:                  # �����w�޼�
                app = App()
        print u"�}�l�ʵ��ؿ�"
        print u"�� Enter �����ʵ�"
        raw_input()            # ���ݫ���

