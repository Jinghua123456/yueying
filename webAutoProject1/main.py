import unittest

from common import doSuit, doReport

if __name__ == '__main__':
    #获取测试套件
    # 通过第一种方法，需要第一步的suit对象
    # suit=unittest.TestSuite()
    # suit=doSuit.addTestByMethod(suit)

    # 通过第二种方法，需要第一步的suit对象
    suit = unittest.TestSuite()
    suit=doSuit.addTestByClass(suit)

    #通过第三种方法，不需要第一步的suit对象，会自动生成一个
    # suit=doSuit.addTestByAuto()


    #执行套件，并在控制台打印测试用例执行情况
    # run=unittest.TextTestRunner()
    # run.run(suit)

    #执行并生成text格式测试报告
    # run=doReport.doTextReport(suit)
    #执行并生成HTML格式测试报告
    # run=doReport.doHTMLReport(suit)
    #执行并生成漂亮的HTML格式测试报告
    run=doReport.doHTMLReportBuf(suit)
