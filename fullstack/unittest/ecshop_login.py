import os
import unittest

class EcshopLogin(unittest.TestCase):
    def test01_baili(self):
        print("测试百里")

    def test02_weiwei(self):
        print("测试微微")

    def test03_zhiliao(self):
        print("知了")

# if __name__ == '__main__':
#     suite = unittest.TestSuite()
#     suite.addTest(EcshopLogin("test01_baili"))
#     suite.addTest(EcshopLogin("test02_weiwei"))
#     unittest.main(defaultTest="suite")     #和下面效果一样
#     # unittest.TextTestRunner().run(suite)  #和上面效果一样

#使用用例集去执行
# if __name__ == '__main__':
#     suite = unittest.TestSuite()
#     testcases = [EcshopLogin("test01_baili"),EcshopLogin("test02_weiwei")]
#     suite.addTests(testcases)
#     unittest.main(defaultTest="suite")     #和下面效果一样
#     # unittest.TextTestRunner().run(suite)  #和上面效果一样

#使用加载器发现当前模块下所有以py结尾的用例
if __name__ == '__main__':
    suite = unittest.TestSuite()
    testcases = unittest.defaultTestLoader.discover(start_dir=os.getcwd(),pattern="*.py")
    suite.addTests(testcases)
    unittest.main(defaultTest="suite")     #和下面效果一样
