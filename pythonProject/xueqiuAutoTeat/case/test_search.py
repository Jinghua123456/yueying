import pytest,yaml,allure,os
from page.app import App

@allure.feature("搜索")
class Testsearch:
    @pytest.mark.parametrize("key,price",yaml.safe_load(open('D:\\pythonCoding\\pythonProject\\xueqiuAutoTeat\\TestCase\\search.yml')))
    @allure.story("搜索股价")
    def test_search(self,key,price):
        with allure.step("首页点击搜索，进入搜索页面，输入关键词搜索，并断言"):
            assert App().start().main().goto_search_page().searchinput(key).get_price()>float(price)
    @allure.story("点击头像进入我的页面")
    def test_photo001(self):
        App().start().main().goto_my_photo()

# if __name__ == '__main__':
#
#     pytest.main(['./case/test_search.py','-sv','--alluredir',"../Testroport/report"])
#     os.system(f"allure generate ../Testroport/report -o ../Testroport/report --clean")
