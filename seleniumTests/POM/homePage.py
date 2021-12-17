from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class HomePage():

    def __init__(self, driver):
        self.driver = driver

        self.username_textbox_name = "user[login]"
        self.password_textbox_name = "user[password]"
        self.login_button_class_name = "glyphicon-log-in"
        self.dropdown_button_id = "bg-nested-dropdown-brand"
        self.about_button_xpath = '//*[@id="Home"]/div/div/div[1]/nav/div/div[1]/li/ul/li[7]/a'
        self.eln_button_xpath = '//*[@id="Home"]/div/div/div[1]/nav/div/div[1]/li/ul/li[5]/a'
        self.signup_button_xpath = '//*[@id="Home"]/div/div/div[1]/nav/div/div[2]/ul/li/a'
        self.edit_button_classname = "btn-primary"
        self.close_button_classname = "close"
        self.cancel_button_classname = "btn-warning"
        self.export_dropdown_button_id = "export-dropdown"
        self.import_button_xpath = '//*[@id="app"]/div/div[1]/nav/div/ul/div[3]/div[1]/div[1]/ul/li[7]/a'
        self.import_file_select_button_xpath = '/html/body/div[2]/div[2]/div/div/div[2]/div/div[1]/input'
        self.import_import_button_xpath = '/html/body/div[2]/div[2]/div/div/div[2]/div/div[2]/button[2]'
        self.export_button_xpath = '//*[@id="app"]/div/div[1]/nav/div/ul/div[3]/div[1]/div[1]/ul/li[6]/a'
        self.export_checkbox_xpath = '/html/body/div[2]/div[2]/div/div/div[2]/div/div[2]/ul/li[1]/label'
        self.export_export_button_xpath = '//*[@id="md-export-dropdown"]/span'

    def enter_username(self, username):
        elem = self.driver.find_element(By.NAME, self.username_textbox_name)
        elem.clear()
        elem.send_keys(username)

    def enter_password(self, password):
        elem = self.driver.find_element(By.NAME, self.password_textbox_name)
        elem.clear()
        elem.send_keys(password)

    def click_login(self):
        elem = self.driver.find_element(By.CLASS_NAME, self.login_button_class_name)
        elem.click()

    def press_return_login(self):
        elem = self.driver.find_element(By.NAME, self.password_textbox_name)
        elem.send_keys(Keys.RETURN)

    def click_about(self):
        elem = self.driver.find_element(By.ID, self.dropdown_button_id)
        elem.click()
        elem = self.driver.find_element(By.XPATH, self.about_button_xpath)
        elem.click()
        self.driver.implicitly_wait(5)

    def click_signup(self):
        elem = self.driver.find_element(By.XPATH, self.signup_button_xpath)
        elem.click()
        self.driver.implicitly_wait(5)

    def click_eln(self):
        elem = self.driver.find_element(By.ID, self.dropdown_button_id)
        elem.click()
        elem = self.driver.find_element(By.XPATH, self.eln_button_xpath)
        elem.click()
        self.driver.implicitly_wait(5)

    def click_edit(self):
        elem = self.driver.find_element(By.CLASS_NAME, self.edit_button_classname)
        elem.click()

    def click_edit_close(self):
        elem = self.driver.find_element(By.CLASS_NAME, self.close_button_classname)
        elem.click()

    def click_edit_cancel(self):
        elem = self.driver.find_element(By.CLASS_NAME, self.cancel_button_classname)
        elem.click()

    def click_import(self):
        elem = self.driver.find_element(By.ID, self.export_dropdown_button_id)
        elem.click()
        elem = self.driver.find_element(By.XPATH, self.import_button_xpath)
        elem.click()
    
    def enter_path_import_file_select(self, path):
        elem = self.driver.find_element(By.XPATH, self.import_file_select_button_xpath)
        elem.send_keys(path)

    def click_import_import(self):
        elem = self.driver.find_element(By.XPATH, self.import_import_button_xpath)
        elem.click()

    def click_import_close(self):
        elem = self.driver.find_element(By.CLASS_NAME, self.close_button_classname)
        elem.click()

    def click_export(self):
        elem = self.driver.find_element(By.ID, self.export_dropdown_button_id)
        elem.click()
        elem = self.driver.find_element(By.XPATH, self.export_button_xpath)
        elem.click()

    def click_export_checkbox(self):
        elem = self.driver.find_element(By.XPATH, self.export_checkbox_xpath)
        elem.click()

    def click_export_export(self):
        elem = self.driver.find_element(By.XPATH, self.export_export_button_xpath)
        elem.click()

    def click_export_close(self):
        elem = self.driver.find_element(By.CLASS_NAME, self.close_button_classname)
        elem.click()