import time

from page.Basepage import Basepage
from appium.webdriver.common.mobileby import MobileBy as By
from page.Search import Search
from page.photo import Photo


class Main(Basepage):
    def goto_my_photo(self):
        self.find(By.ID,"profile_image").click()
        time.sleep(6)
        return Photo(self._driver)
    def goto_search_page(self):
        self.find(By.ID,"home_search").click()
        time.sleep(6)
        return Search(self._driver)



