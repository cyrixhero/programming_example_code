# -*- coding: big5 -*-
import sys
sys.path.append("C:\\IPCE-r6\\Lib")
import random
import unittest

# ���ծר�
class TestSample(unittest.TestCase):
        # ���շǳ�
        def setUp(self):
                self.seq = range(10)
        # �ˬd���ñƧǪ����G�O�_���O���T������
        def testshuffle(self):
                random.shuffle(self.seq)
                self.seq.sort()
                self.assertEqual(self.seq, range(10))
        # �ˬd�H����X�������O�_���T
        def testchoice(self):
                element = random.choice(self.seq)
                self.assert_(element in self.seq)
        #
        def testsample(self):
                # �I�s random.sample(self.seq, 20) �ˬd�O�_����
                self.assertRaises(ValueError, random.sample, self.seq, 20)
                # �ˬd���˵��G�O�_���T
                for element in random.sample(self.seq, 5):
                        self.assert_(element in self.seq)
#
if __name__ == "__main__":
        unittest.main()
else:
        suite = unittest.TestSuite()
        suite.addTest(unittest.makeSuite(TestSample))
        unittest.TextTestRunner(verbosity=2).run(suite)
