from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time
from django.test import LiveServerTestCase
class NewVisitorTest(unittest.TestCase):

    def setUp(self): 
        self.browser = webdriver.Firefox()

    def tearDown(self): 
        self.browser.quit()

    def test_webapp_by_user(self): 
        # ปุณได้ยินเรื่อง เว็บตั้งคำถาม และตอบคำถามออนไลน์เพื่อชิงรางวัล
        # โดยทาง admin เจ้าของเว็บจะให้คนเข้ามาตั้งคำถามและตอบคำถาม
        # คำถามไหนโดนใจและมีคนตอบเยอะจะได้รับเลือกไปเป็นคำถามที่จะถาม idol ชื่อ pipe ตอบ
        # ถ้า idol ตอบถูก เจ้าของคำถามจะได้รางวัล และ โดนใจ idol คนส่งคำถามจะได้รางวัล
        # ปุณจึงเข้าไปดู homepage ของ เว็บตั้งคำถาม และตอบคำถามออนไลน์ชื่อ "Quiz test29"
        self.browser.get('http://localhost:8000/')
        self.assertIn('Home quiz test29', self.browser.title) 
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Welcome to HomePage Quiz Test29', header_text)

        #ปุณเห็น link ไปหน้า quiz จึงกดเข้าไป
        self.browser.find_element_by_id('to_page_quiz').click()
        
        # ปุณจึงได้เห็นหน้า Quiz แล้วเห็นว่ายังไม่มีคำถาม
        self.assertIn('quiz test29', self.browser.title) 
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Quiz', header_text)
        text = self.browser.find_element_by_tag_name('p1').text
        self.assertIn('No quiz are available.', text)
        
        # ปุณจึงเพิ่มคำถามเข้าไป
        self.browser.find_element_by_id('add_question').click()

        # เว็บได้พาปุณมาหน้าการเพิ่มคำถาม 
        self.assertIn('Add question', self.browser.title) 
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Add question', header_text)
        
        # ปุณใส่ ชื่อของตัวเองลงไป 
        inputbox = self.browser.find_element_by_id('create_question_by')  
        self.assertEqual(inputbox.get_attribute('placeholder'),'Your name')
        inputbox.send_keys('Poon')
       
        # ปุณเพิ่ม คำถาม what is pipe favorite color  
        inputbox = self.browser.find_element_by_id('new_text_question')  
        self.assertEqual(inputbox.get_attribute('placeholder'),'Your Question')
        inputbox.send_keys('what is pipe favorite color')

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

        # แต่ปุณเกิดไม่พอใจในคำถามจึงไปขอร้องให้ admin ลบคำถามของเธอ admin จึงได้ลบคำถาม
        # what is pipe favorite color  
        self.browser.find_element_by_id('delete_question').click()
        self.assertIn('Delete Question', self.browser.title) 
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Delete Question', header_text)
        
        inputbox = self.browser.find_element_by_id('create_question_by')  
        self.assertEqual(inputbox.get_attribute('placeholder'),'Your name')
        inputbox.send_keys('admin') 
        inputbox = self.browser.find_element_by_id('delete_quest_text')  
        self.assertEqual(inputbox.get_attribute('placeholder'),'Your Question')
        inputbox.send_keys('what is pipe favorite color')
        self.browser.find_element_by_id('submit').click()
        self.browser.find_element_by_id('back_home').click()
        
        # ปุณจึงเข้ามาดูหน้า Quiz แล้วเห็นว่าคำถามของเธอถูกลบไปแล้วเธอจึงมาเพิ่มใหม่
        self.assertIn('quiz test29', self.browser.title) 
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Quiz', header_text)
        text = self.browser.find_element_by_tag_name('p1').text
        self.assertIn('No quiz are available.', text)
        
        self.browser.find_element_by_id('add_question').click()
        
        self.assertIn('Add question', self.browser.title) 
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Add question', header_text)
         
        inputbox = self.browser.find_element_by_id('create_question_by')  
        self.assertEqual(inputbox.get_attribute('placeholder'),'Your name')
        inputbox.send_keys('Poon')
          
        inputbox = self.browser.find_element_by_id('new_text_question')  
        self.assertEqual(inputbox.get_attribute('placeholder'),'Your Question')
        inputbox.send_keys('what is pipe favorite food')

        inputbox = self.browser.find_element_by_id('new_text_choice1')  
        self.assertEqual(inputbox.get_attribute('placeholder'),'Your choice 1')
        inputbox.send_keys('pizza')
        self.browser.find_element_by_id('choice1_true').click()
        
        inputbox = self.browser.find_element_by_id('new_text_choice2')  
        self.assertEqual(inputbox.get_attribute('placeholder'),'Your choice 2')
        inputbox.send_keys('BBQ')
        self.browser.find_element_by_id('choice2_false').click()

        # เมื่อปุณกด submit ก็ได้เห็นคำถามที่ตนเพิ่มเข้าไปด้านล่าง แล้วกลับไปหน้า homepage ก็พบคำถามใหม่ถูกเพิ่มมาแล้ว
        self.browser.find_element_by_id('submit').click()
        self.browser.find_element_by_id('back_home_page').click()

        # ต่อมาดลเป็นเพื่อนในห้องเรียนของ ปุณ ได้เข้ามาที่เว็บตอบคำถาม "Quiz test29" ตามที่ปุณบอก แล้วกดเข้าไปที่คำถาม
        # what is pipe favorite color
        self.browser.find_element_by_id('quiz_select1').click()

        # เว็บได้พาดลมาหน้าการตอบคำถาม และเห็นคำถาม
        self.assertIn('Choice question', self.browser.title) 
        
        # ดลใส่ ชื่อของตัวเองลงไป 
        inputbox = self.browser.find_element_by_id('username')  
        self.assertEqual(inputbox.get_attribute('placeholder'),'Your name')
        inputbox.send_keys('don') 

        # ดลจึงได้ตอบคำถาม 
        self.browser.find_element_by_id('choice1').click()
        self.browser.find_element_by_id('vote').click()

        # เว็บได้พาดลมาหน้าการผลการตอบคำถาม และเห็นคะแนนของตนเอง
        self.assertIn('results question', self.browser.title) 
        
         # ดลจึงได้กลับ ไปตอบคำถามอีกรอบ 
        self.browser.find_element_by_id('vote_again').click()

        # เว็บได้พาดลมาหน้าการตอบคำถามอีกครั้ง 
        self.assertIn('Choice question', self.browser.title)
        inputbox = self.browser.find_element_by_id('username')  
        self.assertEqual(inputbox.get_attribute('placeholder'),'Your name')
        inputbox.send_keys('don') 
        self.browser.find_element_by_id('choice2').click()
        self.browser.find_element_by_id('vote').click()

        # เว็บได้พาดลมาหน้าการผลการตอบคำถาม  และเห็นคะแนนของตนเอง
        self.assertIn('results question', self.browser.title) 

       
        
        self.fail('Finish the test!') 


if __name__ == '__main__': 
    unittest.main(warnings='ignore')
