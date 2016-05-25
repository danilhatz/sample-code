import unittest
import os
import random
import string
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.common.keys import Keys
import urllib2
import json
from time import sleep
import datetime


def str_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))





class ComplexIOSTests(unittest.TestCase):
    def setUp(self):
        # set up appium
        # ** Important Note **
        # Make sure you have build the UICatalog applcation in your local repository
        app = os.path.join(
            '/Users/danilkhatsanovsky/sample-code/sample-code/apps/UICatalog/build/Release-iphonesimulator',
            'UICatalog.app')
        app = os.path.abspath(app)
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                'app': app,
                'platformName': 'iOS',
                'platformVersion': '9.3',
                'deviceName': 'iPhone 4s',
                'context': 'NATIVE_APP'

            })
        self._values = []

    def tearDown(self):
        self.driver.quit()

    # def _open_menu_position(self, index):
    #     # Opens up the menu at position [index] : starts at 0.
    #     table = self.driver.find_element_by_class_name("UIATableView")
    #     self._row = table.find_elements_by_class_name("UIATableCell")[index]
    #     self._row.click()

    # def test_click_element(self):
    #     self.driver.swipe(129, 300, 146, 90, duration=800)
    #     self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]').click()
    #     self.driver.find_element_by_xpath(
    #         '//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]/UIAStaticText[1]').click()
    #     decisions = self.driver.find_element_by_xpath(
    #         '//UIAApplication[1]/UIAWindow[4]/UIAActionSheet[1]/UIACollectionView[1]/UIACollectionCell[1]')
    #     decisions.click()
    #     self.assertTrue(decisions)
    #     self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAButton[1]').click()
    #     self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[2]').click()
    #     cell_is_displayed = self.driver.find_element_by_xpath(
    #         "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]").is_displayed
    #
    #     self.assertTrue(cell_is_displayed, 'Cell should be visible')

    def test_swipe(self):
        self.driver.find_element_by_xpath("//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[5]").click()
        self.driver.swipe(start_x=109, start_y=230, end_x=109, end_y=160)
        date = self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIAStaticText[1]')
        future_date = (datetime.datetime.now() + datetime.timedelta(days=2)).strftime("%B %d, %Y, %I:%M %p").lstrip(
            "0").replace(" 0", " ")
        self.assertRegexpMatches(date.get_attribute("name"), future_date)

    # def test_frames(self):
    #         # go into webview frame
    #         self._open_menu_position(15)
    #
    #         # get the contexts and switch to webview
    #         contexts = self.driver.contexts
    #         self.assertEqual([u'NATIVE_APP', u'WEBVIEW_1'], contexts)
    #         self.driver.switch_to.context(contexts[1])
    #
    #         # Find the store link
    #         sleep(4) # let the page load, perhaps
    #         logo = self.driver.find_element_by_xpath('//*/UIATextField[@value="http://apple.com"]')
    #         self.assertIsNotNone(logo)
    #
    #         # leave the webview
    #         self.driver.switch_to.context(contexts[0])
    #
    #         # Verify we are out of the webview
    #         scroll_after = self.driver.find_element_by_class_name("UIAScrollView")
    #         self.assertTrue(scroll_after)

    # def test_text_field_edit(self):
    #         # go to the text fields section
    #         self._open_menu_position(13)
    #
    #         text_field = self.driver.find_elements_by_class_name("UIATextField")[0]
    #
    #         # get default/empty text
    #         default_val = text_field.get_attribute("value")
    #
    #         # write some random text to element
    #         rnd_string = str_generator()
    #         text_field.send_keys(rnd_string)
    #         self.assertEqual(text_field.get_attribute("value"), rnd_string)
    #
    #         # clear and check if is empty/has default text
    #         text_field.clear()
    #         self.assertEqual(text_field.get_attribute("value"), default_val)
    #
    # def test_slider(self):
    #         # go to controls
    #         self._open_menu_position(10)
    #
    #         # get the slider
    #         slider = self.driver.find_element_by_class_name("UIASlider")
    #         self.assertEqual(slider.get_attribute("value"), "42%")
    #
    #         slider.set_value(0)
    #         self.assertEqual(slider.get_attribute("value"), "0%")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ComplexIOSTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
