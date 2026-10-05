import smtplib
import ssl
import time
import os
import platform
import imagehash
import base64
import datetime
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from selenium import webdriver
from PIL import Image
from io import BytesIO
from random import randint
from multiprocessing.pool import ThreadPool as Pool
HASH_SIZE = 128
MAX_HASH_DIFFERENCE = 65536
class EmailClient:
    def __init__(self, sender_email, password):
        self.sender_email = sender_email
        self.password = password
        self.port = 465
        self.smtp_server = "smtp.gmail.com"
    def send_email(self, receiver_email, message):
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(self.smtp_server, self.port, context=context) as server:
            server.login(self.sender_email, self.password)
            server.sendmail(self.sender_email, receiver_email, message)
class ChromeDriver:
    def __init__(self, executable_path, data_dir=None):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--ignore-certificate-errors")
        self.options.add_argument("--test-type")
        self.options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=self.options, executable_path=executable_path)
    def open_page(self, url, scroll_percent=0):
        if scroll_percent != 0:
            denominator = (100 / scroll_percent)
            self.driver.get(url)
            self.driver.execute_script(f"window.scrollTo(0, document.body.scrollHeight / {denominator});")
        else:
            self.driver.get(url)
        time.sleep(2)
    def close(self):
        self.driver.close()
    def take_screenshot(self):
        page_screenshot = self.driver.get_screenshot_as_png()
        page_screenshot = Image.open(BytesIO(page_screenshot))
        return page_screenshot
class ChangeMonitor:
    def __init__(self, chrome_driver, email_client):
        self.chrome_driver = chrome_driver
        self.email_client = email_client
    def calculate_hash_difference_percent(self, old_hash, new_hash):
        difference = old_hash - new_hash
        percent_difference = (difference / MAX_HASH_DIFFERENCE) * 100
        return percent_difference
    def prepare_email_message(self, old_screenshot, new_screenshot, url):
        message = MIMEMultipart()
        message_body = f"Change alert for {url}"
        message["Subject"] = "Change alert!"
        message["From"] = self.email_client.sender_email
        message["To"] = self.email_client.sender_email
        message.attach(MIMEText(message_body, "plain"))
        message = self.attach_screenshot(message, new_screenshot, "new_screenshot.png")
        message = self.attach_screenshot(message, old_screenshot, "old_screenshot.png")
        return message.as_string()
    def attach_screenshot(self, message, screenshot, filename):
        stream = BytesIO()
        screenshot.save(stream, "PNG")
        stream.seek(0)
        screenshot_data = stream.read()
        part = MIMEBase("application", "octet-stream")
        part.set_payload(screenshot_data)
        encoders.encode_base64(part)
        part.add_header("Content-Disposition", f"attachment; filename={filename}")
        message.attach(part)
        return message
    def check_for_changes(self, args):
        url, check_interval, scroll_percent = args
        old_screenshot = None
        while True:
            self.chrome_driver.open_page(url, scroll_percent)
            if old_screenshot is None:
                old_screenshot = self.chrome_driver.take_screenshot()
            else:
                new_screenshot = self.chrome_driver.take_screenshot()
                old_hash = imagehash.phash(old_screenshot, hash_size=HASH_SIZE)
                new_hash = imagehash.phash(new_screenshot, hash_size=HASH_SIZE)
                percent_difference = self.calculate_hash_difference_percent(old_hash, new_hash)
                current_time = datetime.datetime.now().strftime("%I:%M:%S %p")
                if percent_difference > 1:
                    message = self.prepare_email_message(old_screenshot, new_screenshot, url)
                    self.email_client.send_email(self.email_client.sender_email, message)
                    print(f"\nChange detected at {current_time}!\n")
                    print("The screenshots are different by: ", percent_difference)
                else:
                    print(f"No change detected at {current_time}.")
                old_screenshot = new_screenshot
            minimum_sleep = int(check_interval * 0.7)
            time.sleep(randint(minimum_sleep, check_interval))
def get_chrome_driver_name():
    if platform.system() == "Windows":
        return "chromedriver_windows.exe"
    elif platform.system() == 'Linux':
        return "chromedriver_linux"
    else:
        return "chromedriver_mac"
def get_email_credentials():
    try:
        credentials = open("../credentials.txt", "r").read().split(",")
        return credentials[0], credentials[1]
    except:
        return "some_email@domain.com", "some_password"
def main():
    email, password = get_email_credentials()
    urls_to_monitor = [("https:
    dummy_url = "https:
    directory_this_script = os.path.dirname(os.path.realpath(__file__))
    chrome_driver_name = get_chrome_driver_name()
    chrome_driver_location = os.path.join(directory_this_script, "bin", chrome_driver_name)
    pool = Pool(len(urls_to_monitor))
    for url in urls_to_monitor:
        driver = ChromeDriver(chrome_driver_location)
        email_client = EmailClient(email, password)
        monitor = ChangeMonitor(driver, email_client)
        pool.apply_async(monitor.check_for_changes, (url,))
    pool.close()
    pool.join()
if __name__ == '__main__':
    main()