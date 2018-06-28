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
        # ดลกับปุณเป็นแฟนก่อน 
        # วันนึง ปุณได้ยินเรื่องเว็บส่งคำถาม และตอบคำถามออนไลน์แบบง่ายๆ
        # เป็นเหมือนเกมให้ฝ่ายนึงไปตั้งคำถาม แล้วให้อีกฝ่ายมาตอบ ถ้าตอบถูกจะได้คะแนน
        # ปุณจึงเข้าไปดู homepage ของ เว็บคำถามออนไลน์ชื่อ "Quiz test29"
        self.browser.get('http://localhost:8000/quiz')
        self.assertIn('quiz test29', self.browser.title) 
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Quiz', header_text)
        
        # ปุณต้องการเพิ่มคำถามของตนเองเข้าไป
        self.browser.find_element_by_id('add_question').click()

        # เว็บได้พาปุณมาหน้าการเพิ่มคำถาม 
        self.assertIn('Add and fix question', self.browser.title) 
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Add and fix question', header_text)
        
       
        # ปุณเพิ่ม คำถาม what is my favorite color  
        inputbox = self.browser.find_element_by_id('new_text_question')  
        self.assertEqual(inputbox.get_attribute('placeholder'),'Your Question')
        inputbox.send_keys('what is my favorite color')

        # ปุณเพิ่ม choice : green เป็น false
        inputbox = self.browser.find_element_by_id('new_text_choice1')  
        self.assertEqual(inputbox.get_attribute('placeholder'),'Your choice 1')
        inputbox.send_keys('green')
        self.browser.find_element_by_id('choice1_false').click()
        
        # ปุณเพิ่ม choice : blue เป็น true
        inputbox = self.browser.find_element_by_id('new_text_choice2')  
        self.assertEqual(inputbox.get_attribute('placeholder'),'Your choice 2')
        inputbox.send_keys('blue')
        self.browser.find_element_by_id('choice2_true').click()

        # เมื่อปุณกด submit ก็ได้เห็นคำถามที่ตนเพิ่มเข้าไปด้านล่าง แล้วกลับไปหน้า homepage
        self.browser.find_element_by_id('submit').click()
        self.browser.find_element_by_id('back_home_page').click()
        
        # ต่อมาดลได้เข้ามาที่เว็บตอบคำถาม "Quiz test29" ตามที่ปุณบอก แล้วกดเข้าไปที่คำถาม
        # what is my favorite color
 
        time.sleep(5)
        self.fail('Finish the test!') 


if __name__ == '__main__': 
    unittest.main(warnings='ignore')
