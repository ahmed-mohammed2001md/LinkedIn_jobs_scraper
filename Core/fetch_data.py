
from seleniumwire import webdriver  
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
from Core.automation import Automation
from Core.process_data import Process
import Core.configure as config
from Core.save import Save
import time, random, os


class Fetch:


    def get_data(urls, mode = 0):
        '''
        This mehtod get data from urls and it has 2 modes to get data from
            0- single link
            1- txt file

        when you no 1 the app will remove every sucess extracted link from txt file

        Args:
            urls : takes str link or list links
            mode : 0 or 1

        '''

        # add chrome options
        chrome_options = Options()

        # Add headers and other settings to mimic a real browser
        # chrome_options.add_argument('--headless=new') # Don't pop up the website for redcue requests and data usage
        chrome_options.add_argument(f"--user-agent={UserAgent(os='iOS').random}")
        chrome_options.add_argument("--accept-language=en-US,en;q=0.9")
        chrome_options.add_argument("--referer=https://www.google.com/")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")

        # Disable images and CSS
        chrome_options.add_argument('--blink-settings=imagesEnabled=false')
        chrome_options.add_experimental_option("prefs", {
            "profile.managed_default_content_settings.images": 2,  # Disable images
            "profile.managed_default_content_settings.stylesheet": 2, # Disable CSS
        })

        seleniumwire_options = {
            'proxy' : {
                # 'http' : config.PROXY,
                # 'https' : config.PROXY,
                'connection_timeout': 30,  # Default is 5 seconds
                'verify_ssl': False,  # Try disabling SSL verification if needed
            },
            'enable_har': False,  # Disable HAR capture if not needed
            'disable_capture': True,  # Don't capture requests by default
            'request_storage': 'memory',  # Use memory instead of disk
            'request_storage_max_size': 100,  # Limit stored requests
            'exclude_hosts': [
            '*.css', '*.png', '*.jpg', '*.gif', '*.svg',
            '*.woff', '*.woff2', '*.ttf',
            '*google-analytics.com*',  # Analytics
            ]

        }

        # Disable the "Chrome is being controlled by automated test software" notification
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])

        # add values to the driver options and seleniumwire_options
        driver = webdriver.Chrome(options=chrome_options, seleniumwire_options=seleniumwire_options)

        # get data after login
        # driver = Automation.sign_in(driver)

        # if the urls is single value (str) put it in list
        if isinstance(urls, str):
            urls = list([urls])


        # progress
        adding_progress = 100 / len(urls)
        progress = 0

        # get data from pages
        for url in urls:
            try:
                # run urls and get data
                driver.get(url)
                data = Process.process_data(BeautifulSoup(driver.page_source, 'html.parser'))
                Save.excel(data)

                # remove the link from txt file after get data from it
                if mode == 1:
                    # /urls.txt
                    remove_url_from_file(f'{os.getcwd()}/{config.URLS_TXT}', url)

                time.sleep(random.uniform(10 , 15))

            except Exception as e:
                print(e)

            # add progress
            progress += adding_progress
            print(f'-=-=-=-= {progress:.2f} -=-=-=-=')

        time.sleep(15)


def remove_url_from_file(file_path, url_to_remove):
    '''
        this method remove the urls from txt who the app scarped the data from
        so, we have no duplicated data
    '''
    # Read all lines from the file
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    # Filter out the URL we want to remove
    # Using strip() to remove any whitespace/newline characters for comparison
    new_lines = [line for line in lines if line.strip() != url_to_remove]
    
    # Write the remaining lines back to the file
    with open(file_path, 'w') as file:
        file.writelines(new_lines)
