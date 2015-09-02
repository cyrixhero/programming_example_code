# -*- coding: big5 -*-
import sys
sys.path.append("C:\\IPCE-r6\\Lib")
import random
import unittest

# 測試案例
class TestSample(unittest.TestCase):
        # 測試準備
        def setUp(self):
                self.seq = range(10)
        # 檢查打亂排序的結果是否仍是正確的元素
        def testshuffle(self):
                random.shuffle(self.seq)
                self.seq.sort()
                self.assertEqual(self.seq, range(10))
        # 檢查隨機抽出的元素是否正確
        def testchoice(self):
                element = random.choice(self.seq)
                self.assert_(element in self.seq)
        #
        def testsample(self):
                # 呼叫 random.sample(self.seq, 20) 檢查是否有錯
                self.assertRaises(ValueError, random.sample, self.seq, 20)
                # 檢查取樣結果是否正確
                for element in random.sample(self.seq, 5):
                        self.assert_(element in self.seq)
#
if __name__ == "__main__":
        unittest.main()
else:
        suite = unittest.TestSuite()
        suite.addTest(unittest.makeSuite(TestSample))
        unittest.TextTestRunner(verbosity=2).run(suite)
