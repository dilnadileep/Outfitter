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
        
        # login=driver.find_element(By.CSS_SELECTOR,"a.nav-link[href='/signin/']")
        # login.click()
        # time.sleep(2)
        # email=driver.find_element(By.CSS_SELECTOR,"input#email.form-control.form-control-lg[name='email']")
        # email.send_keys("dilna20052002@gmail.com")
        # password=driver.find_element(By.CSS_SELECTOR,"input#password.form-control.form-control-lg[name='password']")
        # password.send_keys("Dilna@123")
        # presubmit=driver.find_element(By.CSS_SELECTOR,"img.img-fluid")
        # presubmit.click()
        # submit=driver.find_element(By.ID,"LoginBtn")
        # submit.click()
        # time.sleep(2)
        
        # dash=driver.find_element(By.ID,"sele")
        # dash.click()
        # time.sleep(3)
        
        # shop_cart=driver.find_element(By.CSS_SELECTOR,"a.nav-link[href='/cart/']")
        # shop_cart.click()
        # time.sleep(2)
        # order=driver.find_element(By.CSS_SELECTOR,"a.nav-link[href='/c_order_customer/']")
        # order.click()
        # time.sleep(2)
        
        # view_rec=driver.find_element(By.CSS_SELECTOR,"a.btn.btn-primary[href='/invoice2/24/']")
        # view_rec.click()
        # time.sleep(2)
        # print("Invoice downloaded")

        
        
        # add_gar=driver.find_element(By.ID,"add_gar1")
        # add_gar.click()
        # time.sleep(5)
        # add_new=driver.find_element(By.CSS_SELECTOR,"button.btn.btn-primary[data-bs-toggle='modal'][data-bs-target='#addProductModal']")
        # add_new.click()
        # time.sleep(2)
        
        
        # category2=driver.find_element(By.CSS_SELECTOR,"select#category2.form-control.form-control-lg[name='category2'][required]")
        # category2.click()
        # time.sleep(2)
        # category3=driver.find_element(By.CSS_SELECTOR,"option[value='Gown']")
        # category3.click()
        # time.sleep(2)
        
        # des=driver.find_element(By.CSS_SELECTOR,"input#description.form-control.form-control-lg[name='description'][type='text'][size='50']")
        # des.send_keys("georgett Embroider net fabric Lehenga")
        # time.sleep(1)
        
        # time_p=driver.find_element(By.CSS_SELECTOR,"select#time.form-control.form-control-lg[name='time']")
        # time_p.click()
        # nine_day=driver.find_element(By.CSS_SELECTOR,"option[value='9_Days']")
        # nine_day.click()
        # time.sleep(1)
        
        # image_input = driver.find_element(By.CSS_SELECTOR, "input#image.form-control.form-control-lg[name='image'][type='file'][accept='image/*']")
        # image_path = 'C:\\Users\\dilna\\OneDrive\\Pictures\\Outfitter\\c_lehanga\\alia_lehanga7.jpeg'
        # image_input.send_keys(image_path)
        # time.sleep(2)

        # price=driver.find_element(By.CSS_SELECTOR,"input#price.form-control.form-control-lg[name='price'][type='text']")
        # price.send_keys("1250")
        # time.sleep(1)
        
        # save_bt=driver.find_element(By.CSS_SELECTOR,"button#savebtn.btn.btn-primary[name='savebtn'][type='submit'][disabled]")
        # click_test=driver.find_element(By.ID,"test_id")
        # click_test.click()
        # save_bt.click()
        # time.sleep(3)
        # print("Product added succesfully")
       
       
        # dash=driver.find_element(By.ID,"sele")
        # dash.click()
        # time.sleep(3)

        # profile=driver.find_element(By.CSS_SELECTOR,"a.nav-link[href='/profile/']")
        # profile.click()
        # time.sleep(2)
        # number=driver.find_element(By.ID,"num")
        # number.clear()
        # number.send_keys("9846242069")
        # gender=driver.find_element(By.ID,"gender")
        # gender.click()
        # time.sleep(1)
        # female=driver.find_element(By.CSS_SELECTOR,"option[value='female']")
        # female.click()
        # time.sleep(1)
        # state=driver.find_element(By.ID,"state")
        # state.click()
        # time.sleep(1)
        # kerala=driver.find_element(By.CSS_SELECTOR,"option[value='Tamil Nadu']")
        # kerala.click()
        # time.sleep(1)
        # district=driver.find_element(By.ID,"district")
        # district.click()
        # time.sleep(1)
        # idukki=driver.find_element(By.CSS_SELECTOR,"option[value='Karur']")
        # idukki.click()
        # ad1=driver.find_element(By.CSS_SELECTOR,"input#ad1.form-control.form-control-lg[name='ad1']")
        # ad1.clear()
        # ad1.send_keys("apartment building")
        # time.sleep(1)
        # ad2=driver.find_element(By.CSS_SELECTOR,"input#ad2.form-control.form-control-lg[name='ad2']")
        # ad2.clear()
        # ad2.send_keys("KP 2nd street")
        # time.sleep(1)
        # pincode=driver.find_element(By.ID,"pincode")
        # pincode.clear()
        # pincode.send_keys("673526")
        # time.sleep(1)
        # input_date1= "2001-10-20"
        # formatted_date = datetime.strptime(input_date1, '%Y-%m-%d').strftime('%m-%d-%Y')
        # opendate_input = driver.find_element(By.ID, "age1")
        # opendate_input.send_keys(formatted_date)
        # time.sleep(1)
        # savebt=driver.find_element(By.ID,"savebtn")
        # savebt.click()
        # time.sleep(2)

        # print("Profile updated")

        # cele_c=driver.find_element(By.ID,"add_gar1")
        # cele_c.click()
        # time.sleep(2)
        # cart_c=driver.find_element(By.CSS_SELECTOR,"a.nav-link[href='/cart_order/']")
        # cart_c.click()
        # time.sleep(2)
        # upd=driver.find_element(By.CSS_SELECTOR,"button[type='submit']")
        # upd.click()
        # time.sleep(2)
        # print("Tailor assigned")
        
        # t_indexp=driver.find_element(By.CSS_SELECTOR,"a[href='/t_index/']")
        # t_indexp.click()
        # time.sleep(2)
        # add_g=driver.find_element(By.CSS_SELECTOR,"button.instagram-button > a.nav-link[href='/add_garment/']")
        # add_g.click()
        # time.sleep(2)
        
        # add_new=driver.find_element(By.CSS_SELECTOR,"button.btn.btn-primary[data-bs-toggle='modal'][data-bs-target='#addProductModal']")
        # add_new.click()
        # time.sleep(2)
        
        # category=driver.find_element(By.CSS_SELECTOR,"select#category.form-control.form-control-lg[name='category'][required]")
        # category.click()
        # time.sleep(1)
        # blouse=driver.find_element(By.CSS_SELECTOR,"option[value='Sareee_Blouse']")
        # blouse.click()
        # time.sleep(1)
        
        # des=driver.find_element(By.CSS_SELECTOR,"input#description.form-control.form-control-lg[name='description'][type='text'][size='50']")
        # des.send_keys("available in all colors")
        # time.sleep(1)
        
        # time_p=driver.find_element(By.CSS_SELECTOR,"select#time.form-control.form-control-lg[name='time']")
        # time_p.click()
        # nine_day=driver.find_element(By.CSS_SELECTOR,"option[value='9_Days']")
        # nine_day.click()
        # time.sleep(1)
        
        # image_input = driver.find_element(By.CSS_SELECTOR, "input#image.form-control.form-control-lg[name='image'][type='file'][accept='image/*']")
        # image_path = 'C:\\Users\\dilna\\Desktop\\Outfitter\\project\\media\\products\\blouse3_ZpyPHlD.jpeg'
        # image_input.send_keys(image_path)
        # time.sleep(2)

        # price=driver.find_element(By.CSS_SELECTOR,"input#price.form-control.form-control-lg[name='price'][type='text']")
        # price.send_keys("1250")
        # time.sleep(1)
        
        # save_bt=driver.find_element(By.CSS_SELECTOR,"button#savebtn.btn.btn-primary[name='savebtn'][type='submit'][disabled]")
        # click_test=driver.find_element(By.ID,"test_id")
        # click_test.click()
        # save_bt.click()
        # time.sleep(3)

        # redi=driver.find_element(By.CSS_SELECTOR,"a[href='/t_index/']")
        # redi.click()
        # time.sleep(2)
        
        # req=driver.find_element(By.CSS_SELECTOR,"button.instagram-button > a.nav-link[href='/order_request/']")
        # req.click()
        # time.sleep(2)
        
        # approve=driver.find_element(By.CSS_SELECTOR,"button.approve-button[type='submit']")
        # approve.click()
        # time.sleep(2)
        
        # redi2=driver.find_element(By.CSS_SELECTOR,"a[href='/t_index/']")
        # redi2.click()
        # time.sleep(2)

        # print("Order approved added succesfully")

# if __name__ == '__main__':
#     import unittest
#     unittest.main()