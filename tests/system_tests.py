import unittest, os, time
from app import create_app, db
from tests import data
from selenium import webdriver
from config import TestingConfig
from flask_testing import LiveServerTestCase
from urllib.request import urlopen

basedir = os.path.abspath(os.path.dirname(__file__))


class SystemTest(unittest.TestCase):
    driver = None

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=os.path.join(basedir, 'chromedriver.exe'))
        if not self.driver:
            self.skipTest('Web browser not available')
        else:
            self.app = create_app(TestingConfig)
            self.app_context = self.app.app_context()
            self.app_context.push()
            db.create_all()
            data.add_data()
            self.driver.maximize_window()
            self.driver.get('http://localhost:5000/')

    def tearDown(self):
        if self.driver:
            self.driver.close()
            db.session.remove()
            db.drop_all()
            db.session.remove()
            self.app_context.pop()

    # def test_server_is_up_and_running(self):
    #     response = urlopen(self.get_server_url())
    #     self.assertEqual(response.code, 200)

    def test_register_login(self):
        # test register
        self.driver.get('http://localhost:5000/loginAndRegister')
        self.driver.implicitly_wait(5)
        sign_up_button = self.driver.find_element_by_id('sign-up')
        sign_up_button.click()
        register_username_field = self.driver.find_element_by_id('register_username')
        register_username_field.send_keys('RandomGuy')
        email_field = self.driver.find_element_by_id('email')
        email_field.send_keys('123456@gmail.com')
        register_password_field = self.driver.find_element_by_id('register_password')
        register_password_field.send_keys('12345')
        register_password2_field = self.driver.find_element_by_id('register_password2')
        register_password2_field.send_keys('12345')
        time.sleep(1)
        register_submit = self.driver.find_element_by_id('registration_submit')
        register_submit.click()
        # test login
        self.driver.implicitly_wait(5)
        time.sleep(1)
        login_username_field = self.driver.find_element_by_id('login_username')
        login_username_field.send_keys('RandomGuy')
        login_password_field = self.driver.find_element_by_id('login_password')
        login_password_field.send_keys('12345')
        time.sleep(1)
        login_submit = self.driver.find_element_by_id('login_submit')
        login_submit.click()

        # check login success
        self.driver.implicitly_wait(5)
        time.sleep(1)
        logout = self.driver.find_element_by_partial_link_text('Logout')
        self.assertEqual(logout.get_attribute('innerHTML'), 'RandomGuy_Logout', msg='Logged in')

    def test_tutorial(self):
        # test auth
        self.driver.get('http://localhost:5000/tutorials')
        self.driver.implicitly_wait(5)
        self.assertEqual(self.driver.find_element_by_class_name('title').get_attribute('innerHTML'), '401',
                         msg='unauthenticated')

        # login an account
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_partial_link_text('login your account').click()
        self.driver.implicitly_wait(5)
        time.sleep(1)
        login_username_field = self.driver.find_element_by_id('login_username')
        login_username_field.send_keys('John')
        login_password_field = self.driver.find_element_by_id('login_password')
        login_password_field.send_keys('12345')
        time.sleep(1)
        login_submit = self.driver.find_element_by_id('login_submit')
        login_submit.click()

        # redirect to tutorial page
        self.driver.implicitly_wait(5)
        time.sleep(1)
        tutorial_field = self.driver.find_element_by_partial_link_text('Tutorial')
        tutorial_field.click()
        self.assertEqual(self.driver.find_element_by_class_name('title').get_attribute('innerHTML'),
                         'Learn To Play XiangQi / Chinese Chess',
                         msg='authenticated')

        # next page
        self.driver.implicitly_wait(5)
        time.sleep(1)
        next_page_field = self.driver.find_element_by_id('next')
        next_page_field.click()
        self.assertEqual(self.driver.find_element_by_id('numberPagin_2').get_attribute('innerHTML'),
                         '2', msg='next page')

        # pre page
        self.driver.implicitly_wait(5)
        time.sleep(1)
        pre_page_field = self.driver.find_element_by_id('pre')
        pre_page_field.click()
        self.assertEqual(self.driver.find_element_by_id('numberPagin_1').get_attribute('innerHTML'),
                         '1', msg='pre page')

    def test_quiz(self):
        # test auth
        self.driver.get('http://localhost:5000/questionsInfo')
        self.driver.implicitly_wait(5)
        self.assertEqual(self.driver.find_element_by_class_name('title').get_attribute('innerHTML'), '401',
                         msg='unauthenticated')

        # login an account
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_partial_link_text('login your account').click()
        self.driver.implicitly_wait(5)
        time.sleep(1)
        login_username_field = self.driver.find_element_by_id('login_username')
        login_username_field.send_keys('Tom')
        login_password_field = self.driver.find_element_by_id('login_password')
        login_password_field.send_keys('qwerty')
        time.sleep(1)
        login_submit = self.driver.find_element_by_id('login_submit')
        login_submit.click()

        # redirect to quizInfo page
        self.driver.implicitly_wait(5)
        time.sleep(1)
        quiz_info_field = self.driver.find_element_by_partial_link_text('Quiz')
        quiz_info_field.click()
        self.assertEqual(self.driver.find_element_by_class_name('title').get_attribute('innerHTML'),
                         'INSTRUCTIONS',
                         msg='authenticated')

        # redirect to quiz page
        self.driver.implicitly_wait(5)
        time.sleep(1)
        quiz_field = self.driver.find_element_by_id('begin')
        quiz_field.click()
        self.assertEqual(self.driver.find_element_by_class_name('title').get_attribute('innerHTML'),
                         'Start your Quiz now:',
                         msg='quiz page')

        # submit quiz
        self.driver.implicitly_wait(5)
        time.sleep(1)
        submit_field = self.driver.find_element_by_id('submit')
        submit_field.click()
        self.assertEqual(self.driver.find_element_by_id('username').get_attribute('innerHTML'),
                         'Tom',
                         msg='quiz feedback')


if __name__ == '__main__':
    unittest.main()
