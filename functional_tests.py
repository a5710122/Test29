from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self): 
        self.browser = webdriver.Firefox()

    def tearDown(self): 
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self): 

        self.browser.get('http://localhost:8000')
        
        self.assertIn('Test26', self.browser.title) 

        inputbox = self.browser.find_element_by_id('number1')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'you number'
        )

        inputbox.send_keys('10')
        inputbox.send_keys(Keys.ENTER)
      

        self.fail('Finish the test!') 


if __name__ == '__main__': 
    unittest.main(warnings='ignore')