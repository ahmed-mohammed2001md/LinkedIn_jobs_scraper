
from seleniumwire import webdriver  
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

class Fetch:


    def get_data(url):
        
        # add https if the link dosnot has it
        if not url.startswith('https://') or not url.startswith('http://'):
            url = f'https://{url}'


        # add chrome options
        chrome_options = Options()

        # Add headers and other settings to mimic a real browser
        # chrome_options.add_argument('--headless=new') # Don't pop up the website for redcue requests and data usage
        chrome_options.add_argument(f"--user-agent={UserAgent(os='iOS').random}")
        chrome_options.add_argument("--accept-language=en-US,en;q=0.9")
        chrome_options.add_argument("--referer=https://www.google.com/")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")

        # # Disable images and CSS
        # chrome_options.add_argument('--blink-settings=imagesEnabled=false')
        # chrome_options.add_experimental_option("prefs", {
        #     "profile.managed_default_content_settings.images": 2,  # Disable images
        #     "profile.managed_default_content_settings.stylesheet": 2, # Disable CSS
        # })

        seleniumwire_options = {
            # 'proxy' : {
            #     'http' : proxy,
            #     'https' : proxy,
            #     'connection_timeout': 30,  # Default is 5 seconds
            #     'verify_ssl': False,  # Try disabling SSL verification if needed
            # },
            # 'enable_har': False,  # Disable HAR capture if not needed
            # 'disable_capture': True,  # Don't capture requests by default
            # 'request_storage': 'memory',  # Use memory instead of disk
            # 'request_storage_max_size': 100,  # Limit stored requests
            # 'exclude_hosts': [
            # '*.css', '*.png', '*.jpg', '*.gif', '*.svg',
            # '*.woff', '*.woff2', '*.ttf',
            # '*google-analytics.com*',  # Analytics
            # '*amazon-adsystem.com*'  # Ads
            # ]

        }

        # Disable the "Chrome is being controlled by automated test software" notification
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])

        # add values to the driver options and seleniumwire_options
        driver = webdriver.Chrome(options=chrome_options, seleniumwire_options=seleniumwire_options)

        driver.get(url)

        return BeautifulSoup(driver.page_source, 'html.parser')
