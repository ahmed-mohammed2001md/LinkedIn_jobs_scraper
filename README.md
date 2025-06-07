A powerful LinkedIn job scraper that extracts job listings from single or multiple pages, with proxy support and sign-in automation.

# Features
<ul>

<li>Interactive Mode: Choose between single URL or batch scraping</li>

<li>Dual Scraping Modes:</li>
<ul>
<li>Single page scraping</li>

<li>Bulk scraping from urls.txt file</li>
</ul>
<li>Proxy Support: Rotate proxies to avoid rate limiting</li>

<li>Login Automation: Automate LinkedIn sign-in process</li>

<li>Configurable: Easy setup through config files</li>
</ul>
# Installation
Clone the repository:

bash
git clone https://github.com/ahmed-mohammed2001md/LinkedIn_jobs_scraper.git

cd LinkedIn_jobs_scraper


# Install requirements:

bash
pip install -r requirements.txt
Main dependencies include:

selenium

beautifulsoup4

requests

# Configuration
Set up your credentials:

Edit core/configur.py:

python
EMAIL = "your@email.com"
PASSWORD = "yourpassword"
Enable sign-in automation (if needed):

Uncomment the signIn section in core/fetch_data.py

Add proxies (optional):

Add your proxies to the configuration file in the specified format

# Usage
When you run the application, it will first ask you to choose between:

Scraping from a single URL

Scraping multiple URLs from urls.txt

## Single Page Scraping
bash
python main.py
Then select option 1 and enter the URL when prompted.

## Multiple Pages Scraping
Add URLs to urls.txt (one per line)

Run:

bash
python main.py
Then select option 2.

## With Proxy
Configure your proxies in core/configur.py before running the scraper.

# Output
Scraped job data is saved in the output/ directory with timestamped files.

# Disclaimer
This tool is for educational purposes only. Use it responsibly and in compliance with LinkedIn's Terms of Service. The developers are not responsible for any misuse of this tool.

# Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

