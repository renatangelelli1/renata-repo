import chromedriver_autoinstaller

from selenium import webdriver
from pyvirtualdisplay import Display
# display = Display(visible=0, size=(800, 800))  
# display.start()

chromedriver_autoinstaller.install()

class TestProcess:
    
    def test_create_process(self):
        chrome_options = webdriver.ChromeOptions()    
        # Add your options as needed    
        options = [
        # Define window size here
        "--window-size=1200,1200",
            "--ignore-certificate-errors"
        
            #"--headless",
            #"--disable-gpu",
            #"--window-size=1920,1200",
            #"--ignore-certificate-errors",
            #"--disable-extensions",
            #"--no-sandbox",
            #"--disable-dev-shm-usage",
            #'--remote-debugging-port=9222'
]
        for option in options:
            chrome_options.add_argument(option)
            driver = webdriver.Chrome(options = chrome_options)
            driver.get('http://github.com')
            print(driver.title)
            with open('./GitHub_Action_Results.txt', 'w') as f:
                f.write(f"This was written with a GitHub action {driver.title}")
            driver.quit()

