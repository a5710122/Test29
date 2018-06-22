from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time

class NewVisitorTest(unittest.TestCase):

    def setUp(self): 
        self.browser = webdriver.Firefox()

    def tearDown(self): 
        self.browser.quit()

    def test_webapp_by_user(self): 
        # ไก่เป็นนักศึกษาในคณะวิศวกรรมศาสตร์       
        # เขาได้ยินการเข้าร่วมการตอบแบบสอบถามออนไลน์เพื่อแลกรางวัล
        # เขาจึงเข้าไปดู homepage ของ แบบสอบถามออนไลน์
        self.browser.get('http://localhost:8000/quiz')
        self.assertIn('quiz test29', self.browser.title) 
        
        # ในเว็ปแบบสอบถามออนไลน์ไก่ได้เห็นหัวข้อของคำถาม
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('quiz', header_text)
        
        #เมื่อไก่เห็นคำถามในเว็บแอปแบบสอบถามออนไลน์เขาจึงกดเข้าไปในคำถามแรก
        self.browser.find_element_by_id('quiz_select1').click()

        #ไก่กดเลือกคำตอบแรก
        self.browser.find_element_by_id('choice1').click()

        #เมื่อไก่เลือกคำตอบแล้วจึงกด vote
        self.browser.find_element_by_id('vote').click()
        
        #เมื่อไก่ตอบเสร็จเขาจึงได้กดเพื่อกลับไปที่หน้าคำถามแรกอีกครั้งเพื่อให้หมูทำต่อจากเขา
        self.browser.find_element_by_id('vote_again').click()
        time.sleep(2)

        self.fail('Finish the test!') 


if __name__ == '__main__': 
    unittest.main(warnings='ignore')
