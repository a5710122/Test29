from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self): 
        self.browser = webdriver.Firefox()

    def tearDown(self): 
        self.browser.quit()

    def test_title_header(self): 
        # ไก่เป็นนักศึกษาในคณะวิศวกรรมศาสตร์       
        # เขาได้ยินการเข้าร่วมการตอปแปปสอปถามออนไลน์เพื่อแลกรางวัล
        # เขาจึงเข้าไปดู homepage ของ แปปสอปถามออนไลน์

        self.browser.get('http://localhost:8000/quiz')
        self.assertIn('quiz test29', self.browser.title) 
        
        # ในเว็ปแปปสอปถามออนไลน์ไก่ได้เห็นหัวข้อของคำถาม

        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('quiz', header_text)


        self.fail('Finish the test!') 


if __name__ == '__main__': 
    unittest.main(warnings='ignore')
