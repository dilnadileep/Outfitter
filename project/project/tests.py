from datetime import datetime
from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Hosttest(TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.live_server_url = 'http://127.0.0.1:8000/'

    def tearDown(self):
        self.driver.quit()
        
    def test_01_login_page(self):
        driver = self.driver
        driver.get(self.live_server_url)
        driver.maximize_window()
        time.sleep(1)
        
        login=driver.find_element(By.CSS_SELECTOR,"a.nav-link[href='/signin/']")
        login.click()
        time.sleep(2)
        email=driver.find_element(By.CSS_SELECTOR,"input#email.form-control.form-control-lg[name='email']")
        email.send_keys("tisha@gmail.com")
        password=driver.find_element(By.CSS_SELECTOR,"input#password.form-control.form-control-lg[name='password']")
        password.send_keys("Tisha@123")
        presubmit=driver.find_element(By.CSS_SELECTOR,"img.img-fluid")
        presubmit.click()
        submit=driver.find_element(By.ID,"LoginBtn")
        submit.click()
        
        profile=driver.find_element(By.CSS_SELECTOR,"a.nav-link[href='/profile/']")
        profile.click()
        time.sleep(2)
        number=driver.find_element(By.ID,"num")
        number.clear()
        number.send_keys("9846242069")
        gender=driver.find_element(By.ID,"gender")
        gender.click()
        time.sleep(1)
        female=driver.find_element(By.CSS_SELECTOR,"option[value='female']")
        female.click()
        time.sleep(1)
        state=driver.find_element(By.ID,"state")
        state.click()
        time.sleep(1)
        kerala=driver.find_element(By.CSS_SELECTOR,"option[value='Tamil Nadu']")
        kerala.click()
        time.sleep(1)
        district=driver.find_element(By.ID,"district")
        district.click()
        time.sleep(1)
        idukki=driver.find_element(By.CSS_SELECTOR,"option[value='Karur']")
        idukki.click()
        ad1=driver.find_element(By.CSS_SELECTOR,"input#ad1.form-control.form-control-lg[name='ad1']")
        ad1.clear()
        ad1.send_keys("apartment building")
        time.sleep(1)
        ad2=driver.find_element(By.CSS_SELECTOR,"input#ad2.form-control.form-control-lg[name='ad2']")
        ad2.clear()
        ad2.send_keys("KP 2nd street")
        time.sleep(1)
        pincode=driver.find_element(By.ID,"pincode")
        pincode.clear()
        pincode.send_keys("673526")
        time.sleep(1)
        input_date1= "2001-10-20"
        formatted_date = datetime.strptime(input_date1, '%Y-%m-%d').strftime('%m-%d-%Y')
        opendate_input = driver.find_element(By.ID, "age1")
        opendate_input.send_keys(formatted_date)
        time.sleep(1)
        savebt=driver.find_element(By.ID,"savebtn")
        savebt.click()
        time.sleep(2)

        t_indexp=driver.find_element(By.CSS_SELECTOR,"a[href='/t_index/']")
        t_indexp.click()
        time.sleep(2)
        add_g=driver.find_element(By.CSS_SELECTOR,"button.instagram-button > a.nav-link[href='/add_garment/']")
        add_g.click()
        time.sleep(2)
        
        add_new=driver.find_element(By.CSS_SELECTOR,"button.btn.btn-primary[data-bs-toggle='modal'][data-bs-target='#addProductModal']")
        add_new.click()
        time.sleep(2)
        
        category=driver.find_element(By.CSS_SELECTOR,"select#category.form-control.form-control-lg[name='category'][required]")
        category.click()
        time.sleep(1)
        blouse=driver.find_element(By.CSS_SELECTOR,"option[value='Sareee_Blouse']")
        blouse.click()
        time.sleep(1)
        
        des=driver.find_element(By.CSS_SELECTOR,"input#description.form-control.form-control-lg[name='description'][type='text'][size='50']")
        des.send_keys("available in all colors")
        time.sleep(1)
        
        time_p=driver.find_element(By.CSS_SELECTOR,"select#time.form-control.form-control-lg[name='time']")
        time_p.click()
        nine_day=driver.find_element(By.CSS_SELECTOR,"option[value='9_Days']")
        nine_day.click()
        time.sleep(1)
        
        image_input = driver.find_element(By.CSS_SELECTOR, "input#image.form-control.form-control-lg[name='image'][type='file'][accept='image/*']")
        image_path = 'C:\\Users\\dilna\\Desktop\\Outfitter\\project\\media\\products\\blouse3_ZpyPHlD.jpeg'
        image_input.send_keys(image_path)
        time.sleep(2)

        price=driver.find_element(By.CSS_SELECTOR,"input#price.form-control.form-control-lg[name='price'][type='text']")
        price.send_keys("1250")
        time.sleep(1)
        
        save_bt=driver.find_element(By.CSS_SELECTOR,"button#savebtn.btn.btn-primary[name='savebtn'][type='submit'][disabled]")
        click_test=driver.find_element(By.ID,"test_id")
        click_test.click()
        save_bt.click()
        time.sleep(3)

        redi=driver.find_element(By.CSS_SELECTOR,"a[href='/t_index/']")
        redi.click()
        time.sleep(2)
        
        req=driver.find_element(By.CSS_SELECTOR,"button.instagram-button > a.nav-link[href='/order_request/']")
        req.click()
        time.sleep(2)
        
        approve=driver.find_element(By.CSS_SELECTOR,"button.approve-button[type='submit']")
        approve.click()
        time.sleep(2)
        
        redi2=driver.find_element(By.CSS_SELECTOR,"a[href='/t_index/']")
        redi2.click()
        time.sleep(2)

        print("Order approved added succesfully")

if __name__ == '__main__':
    import unittest
    unittest.main()