# -*- coding: big5 -*-
import sys
def use_fepy_socket(libname="C:\\IPCE-r6\\Lib"):
    """�N socket �Ҳմ��� fepy ���Ѫ�����"""
    sys.path.append(libname)
    import imp, os
    name = 'socket'
    sys.modules[name] = module = imp.new_module(name)
    path = os.path.join(libname, name + '.py')
    execfile(path, module.__dict__)
