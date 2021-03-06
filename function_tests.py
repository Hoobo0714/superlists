from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys

class NerVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        #她去看了应用的首页
        self.browser.get('http://localhost:8000')

        #她注意到网页的标题和头部都含有To-Do这个词
        self.assertIn('To-Do',self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do',header_text)

        #应用邀请她输入一个待办事项
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'),'Enter a to-do item')

        #她在一个文本框中输入了‘buy peacock feathers’
        #伊迪斯的爱好是使用苍蝇做鱼饵钓鱼
        inputbox.send_keys('buy peacock feathers')

        #她按回车键后，页面更新了
        #待办事项中显示了‘1、buy peacock feathers’
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(any(row.text == '1:buy peacock feathers' for row in rows),"New to-do item did not appear in table")

        #页面中又显示了一个文本框，可以输入其他的待办事项
        #她输入了‘use peacock feathers to make a fly’
        #伊迪斯做事很有调理


if __name__ == '__main__':
    unittest.main()