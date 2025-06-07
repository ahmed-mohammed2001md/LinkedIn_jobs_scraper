
from bs4 import BeautifulSoup, Tag
import Core.configure as config

class Process:

    def process_data(soup):

        title = soup.select_one(config.TITLE).text.strip() if soup.select_one(config.TITLE) else None
        company = soup.select_one(config.COMPANY).text.strip() if soup.select_one(config.COMPANY) else None
        location = soup.select_one(config.LOCATION).text.strip() if soup.select_one(config.LOCATION) else None
        date = soup.select_one(config.DATE).text.strip() if soup.select_one(config.DATE) else None
        people_applied = soup.select_one(config.PEOPLE_APPLIED).text.strip() if soup.select_one(config.PEOPLE_APPLIED) else None
        job_req = soup.select_one(config.JOB_REQ) if soup.select_one(config.JOB_REQ) else None
        
        full_data = {
            'title' : title,
            'company': company,
            'location' : location,
            'date' : date,
            'people applied' : people_applied,
            'seniority level' : '',
            'employment type' : '',
            'job function' : '',
            'industries' : ''
        }


        # get requirements of the job
        for req in job_req:
            if req and isinstance(req, Tag):
                # get key and value of the requirements
                req_name = req.select_one('h3').text.strip()
                req_value = req.select_one('span').text.strip()

                # add the requiremtns
                full_data[req_name.lower()] = req_value


        return full_data