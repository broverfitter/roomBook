from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import time, os
import configparser

class UCLRoomBooker:
    def __init__(self):
        options = Options()
        options.add_argument("--headless")

        self.driver = webdriver.Firefox(options=options)
        self.wait = WebDriverWait(self.driver, 10)

        self.config = configparser.ConfigParser()
        self.config.read("config.ini")

    def BookRoom(self, hour, driver, wait):
        driver.get("https://library-calendars.ucl.ac.uk/r/new/availability?lid=872&zone=0&gid=0&capacity=4")

        next_day_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='button'][@class='fc-next-button btn btn-default btn-sm']"))
        )
        next_day_btn.click()
        next_day_btn.click()
        next_day_btn.click()

        time_slot = wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//a[contains(@title, '{hour}:00') and contains(@title, '{self.config['DEFAULT']['room']}')]"))
        )
        time_slot.click()
        
        end_time_dropdown = wait.until(
            EC.presence_of_element_located((By.XPATH, 
                "//select[@class='form-control input-sm b-end-date' and contains(@id, 'bookingend_')]"
            ))
        )
        end_time_select = Select(end_time_dropdown)

        options = end_time_select.options
        end_time_select.select_by_index(len(options) - 1)

        submit_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, 
                "//button[@class='btn btn-primary' and @id='submit_times']"
            ))
        )
        submit_btn.click()

        time.sleep(1)

        email_field = wait.until(
            EC.presence_of_element_located((By.ID, "i0116"))
        )
        email_field.clear()
        email_field.send_keys(self.config["DEFAULT"]["email"])
        email_field.send_keys(Keys.RETURN)

        time.sleep(1)

        password_field = wait.until(
            EC.presence_of_element_located((By.ID, "i0118"))
        )
        password_field.clear()
        password_field.send_keys(self.config["DEFAULT"]["password"])
        password_field.send_keys(Keys.RETURN)
        password_field.send_keys(Keys.RETURN)

        time.sleep(1)

        no_button = wait.until(
            EC.element_to_be_clickable((By.ID, "idBtn_Back"))
        )
        no_button.click()

        complete = wait.until(
        EC.element_to_be_clickable((By.XPATH, 
            "//button[@class='btn btn-primary' and @name='continue' and @id='terms_accept']"
        ))
        )
        complete.click()

        time.sleep(0.5)

        submit_final = wait.until(
            EC.element_to_be_clickable((By.XPATH,
                "//button[@class='btn btn-primary' and @type='submit' and @id='btn-form-submit']"
            ))
        )
        submit_final.click()

    def run_booking(self, time):
        self.BookRoom(time, self.driver, self.wait)
        self.driver.quit()

config = configparser.ConfigParser()
config.read("config.ini")

rb = UCLRoomBooker()
rb.run_booking(config["DEFAULT"]["time"])