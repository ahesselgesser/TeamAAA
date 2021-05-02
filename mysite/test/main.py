from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import unittest
"""
PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("http://127.0.0.1:8000/")
#sleep(5)
simple_upload = driver.find_element_by_link_text("Simple Upload")
simple_upload.click()
try:
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "sub"))
    )
    element.click()
finally:
    time.sleep(10)
    driver.quit()
"""
class Program_test_case(unittest.TestCase):
    def setUp(self):
        self.driver =  webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
        self.driver.get("http://127.0.0.1:8000/")
        time.sleep(2)
    
    def test_title(self):
       # print(self.driver.title)
        result = str(self.driver.title)
        self.assertEqual("AAA_Team", result)

    def test_main_page(self):
        id_test = str(self.driver.find_element_by_id("home_p2").text)
        print(id_test)
        self.assertEqual("Team AAA",id_test)

    def test_click_simple_upload(self):
        element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "Simple_Upload")))
        element.click()
        id_test = str(self.driver.find_element_by_id("header_upload").text)
        self.assertEqual("Upload",id_test)

    def test_file_upload_submit_without_files(self):
        element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "Simple_Upload")))
        element.click()

        element2 = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "sub")))
        element2.click()

        id_test = str(self.driver.find_element_by_id("header_upload").text)
        self.assertEqual("Upload",id_test)
    
    def test_file_upload_submit_with_files(self):
        element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "Simple_Upload")))
        element.click()

        element2 = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "choose_file")))
        element2.send_keys("C://Users/User/Desktop/math (MS) Report 2018.docx")
        #time.sleep(3)

        element3 = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "sub")))
        element3.click()
        #time.sleep(3)

        id_test = str(self.driver.find_element_by_id("upload_success").text)
        self.assertEqual("Successfully Uploaded!",id_test)

        element4 = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "Delete_reports")))
        element4.click()
        time.sleep(1)

        element5 = self.driver.find_element_by_name("delete_file")
        element5.click()

    def test_file_upload_submit_with_files2(self):
        element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "Simple_Upload")))
        element.click()

        element2 = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "choose_file")))
        element2.send_keys("C://Users/User/Desktop/ArtSci(BSCS)Report2019.docx")
        #time.sleep(3)

        element3 = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "sub")))
        element3.click()
        #time.sleep(3)

        id_test = str(self.driver.find_element_by_id("upload_success").text)
        self.assertEqual("Successfully Uploaded!",id_test)

        element4 = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "Delete_reports")))
        element4.click()
        time.sleep(1)

        element5 = self.driver.find_element_by_name("delete_file")
        element5.click()
        
    
    def test_delete_reports_page(self):
        element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "Delete_reports")))
        element.click()
        time.sleep(1)
        id_test = str(self.driver.find_element_by_id("delete_page_header").text)
        self.assertEqual("Remove Reports",id_test)
    
    def test_delete_reports_page_delete_buttom(self):
        element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "Simple_Upload")))
        element.click()

        element2 = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "choose_file")))
        element2.send_keys("C://Users/User/Desktop/math (MS) Report 2018.docx")
        #time.sleep(3)

        element3 = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "sub")))
        element3.click()
        #time.sleep(3)

        element4 = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "Delete_reports")))
        element4.click()
        time.sleep(1)

        element5 = self.driver.find_element_by_name("delete_file")
        element5.click()
        #time.sleep(2)

        id_test = str(self.driver.find_element_by_tag_name("tbody").text)
        self.assertEqual("",id_test)
   
    def test_search_page(self):
        element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "search_page")))
        element.click()
        time.sleep(1)
        id_test = str(self.driver.find_element_by_id("header_search").text)
        self.assertEqual("Search Page",id_test)
    
    def test_report_show_page(self):
        element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "Simple_Upload")))
        element.click()

        element2 = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "choose_file")))
        element2.send_keys("C://Users/User/Desktop/math (MS) Report 2018.docx")
        #time.sleep(3)

        element3 = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "sub")))
        element3.click()
        #time.sleep(3)

        element4 = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "search_page")))
        element4.click()
        time.sleep(1)

        element5 = self.driver.find_element_by_link_text("Mathematics MS Masters 2018-19")
        element5.click()
        #time.sleep(2)

        element6 = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "report_title")))
        #time.sleep(2)
        id_test = str(self.driver.find_element_by_id("report_title").text)
        self.assertEqual("Mathematics MS Masters 2018-19",id_test)
        #time.sleep(3)

    def tearDown(self):
        #time.sleep(5)
        self.driver.close()

if __name__ == "__main__":
    unittest.main()