from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time, requests, pprint
from dotenv import load_dotenv
load_dotenv()
from os import environ

# login variables
username = environ.get('GITHUB_USERNAME')
password = environ.get('GITHUB_PASSWORD')

name = input('Enter the name of the company: ')
role = input('Enter the title of the job: ')
link = input('Enter the link of the application: ')

# opens up Chrome
driver = webdriver.Chrome('/Users/romebell/downloads/chromedriver-4')
time.sleep(3)

# actions
actions = ActionChains(driver)

def login():
    driver.get('https://github.com/login')
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="login_field"]').send_keys(username) # input username
    driver.find_element_by_xpath('//*[@id="password"]').send_keys(password) # input password
    time.sleep(0.25)
    driver.find_element_by_xpath('//*[@id="login"]/div[4]/form/div/input[12]').click() # click on the button
    time.sleep(3)
    print('Login was successful')

def app_text(name, role, link):
    app = {
        "input_name": name,
        "input_role": role,
        "input_link": link,
        "name": "## ",
        "job_title": f"### Job Title: ",
        "job_link_start": "- [ ] Job Link: { [link](",
        "job_link_end": ") }",
        "rejected": f"- [ ] Rejected",
        "senior_role": "- [ ] Senior Role",
        "phone": "- [ ] Phone Screen",
        "coding_challenge": f"- [ ] Coding Challenge",
        "video_screen": "- [ ] Video Screen",
        "tech_interview": "- [ ] Technical Interview",
        "onsite": "- [ ] Onsite",
        "offer": "- [ ] Offer",
        "notes": "## Notes"
    }

    return app

def make_job_card():
    print('REMINDER: Fill out card for submitted apps today!')
    # go to Applications
    driver.get('https://github.com/josh-w42/job_applications/projects/1')
    time.sleep(2)

    driver.find_element_by_xpath('//*[@id="column-12657769"]/div[1]/div[1]/button').click()
    time.sleep(1.5)
    try:
        driver.find_element_by_xpath('//*[@id="column-12657769"]/div[1]/div[2]/form[1]/text-expander/textarea')
        pass
    except:
        print('Element is not found, trying again...')
        make_job_card()

    text = app_text(name, role, link)

    # Enter card info
    # name
    driver.find_element_by_xpath('//*[@id="column-12657769"]/div[1]/div[2]/form[1]/text-expander/textarea').send_keys('...')
    time.sleep(0.25)
    driver.find_element_by_xpath('//*[@id="column-12657769"]/div[1]/div[2]/form[1]/text-expander/textarea').send_keys(Keys.ENTER)
    time.sleep(0.25)
    driver.find_element_by_xpath('//*[@id="column-12657769"]/div[1]/div[2]/form[1]/text-expander/textarea').send_keys(f"{text.get('name')}{text.get('input_name')}")
    driver.find_element_by_xpath('//*[@id="column-12657769"]/div[1]/div[2]/form[1]/text-expander/textarea').send_keys(Keys.ENTER)
    time.sleep(0.1)

    driver.find_element_by_xpath('//*[@id="column-12657769"]/div[1]/div[2]/form[1]/text-expander/textarea').send_keys(f"{text.get('job_title')}{text.get('input_role')}")
    driver.find_element_by_xpath('//*[@id="column-12657769"]/div[1]/div[2]/form[1]/text-expander/textarea').send_keys(Keys.ENTER)
    time.sleep(0.1)

    entire_link = f"{text.get('job_link_start')}{text['input_link']}{text.get('job_link_end')}"
    driver.find_element_by_xpath('//*[@id="column-12657769"]/div[1]/div[2]/form[1]/text-expander/textarea').send_keys(entire_link)
    driver.find_element_by_xpath('//*[@id="column-12657769"]/div[1]/div[2]/form[1]/text-expander/textarea').send_keys(Keys.ENTER)
    time.sleep(0.1)

    driver.find_element_by_xpath('//*[@id="column-12657769"]/div[1]/div[2]/form[1]/text-expander/textarea').send_keys(text.get('rejected'))
    driver.find_element_by_xpath('//*[@id="column-12657769"]/div[1]/div[2]/form[1]/text-expander/textarea').send_keys(Keys.ENTER)
    time.sleep(0.1)
    
    driver.find_element_by_xpath('//*[@id="column-12657769"]/div[1]/div[2]/form[1]/text-expander/textarea').send_keys(text.get('phone'))
    driver.find_element_by_xpath('//*[@id="column-12657769"]/div[1]/div[2]/form[1]/text-expander/textarea').send_keys(Keys.ENTER)
    time.sleep(0.1)

    driver.find_element_by_xpath('//*[@id="column-12657769"]/div[1]/div[2]/form[1]/text-expander/textarea').send_keys(text.get('senior_role'))
    driver.find_element_by_xpath('//*[@id="column-12657769"]/div[1]/div[2]/form[1]/text-expander/textarea').send_keys(Keys.ENTER)
    time.sleep(0.1)

    driver.find_element_by_xpath('//*[@id="column-12657769"]/div[1]/div[2]/form[1]/text-expander/textarea').send_keys(text.get('coding_challenge'))
    driver.find_element_by_xpath('//*[@id="column-12657769"]/div[1]/div[2]/form[1]/text-expander/textarea').send_keys(Keys.ENTER)
    time.sleep(0.1)

    driver.find_element_by_xpath('//*[@id="column-12657769"]/div[1]/div[2]/form[1]/text-expander/textarea').send_keys(text.get('video_screen'))
    driver.find_element_by_xpath('//*[@id="column-12657769"]/div[1]/div[2]/form[1]/text-expander/textarea').send_keys(Keys.ENTER)
    time.sleep(0.1)

    driver.find_element_by_xpath('//*[@id="column-12657769"]/div[1]/div[2]/form[1]/text-expander/textarea').send_keys(text.get('tech_interview'))
    driver.find_element_by_xpath('//*[@id="column-12657769"]/div[1]/div[2]/form[1]/text-expander/textarea').send_keys(Keys.ENTER)
    time.sleep(0.1)

    driver.find_element_by_xpath('//*[@id="column-12657769"]/div[1]/div[2]/form[1]/text-expander/textarea').send_keys(text.get('onsite'))
    driver.find_element_by_xpath('//*[@id="column-12657769"]/div[1]/div[2]/form[1]/text-expander/textarea').send_keys(Keys.ENTER)
    time.sleep(0.1)

    driver.find_element_by_xpath('//*[@id="column-12657769"]/div[1]/div[2]/form[1]/text-expander/textarea').send_keys(text.get('offer'))
    driver.find_element_by_xpath('//*[@id="column-12657769"]/div[1]/div[2]/form[1]/text-expander/textarea').send_keys(Keys.ENTER)
    time.sleep(0.1)

    driver.find_element_by_xpath('//*[@id="column-12657769"]/div[1]/div[2]/form[1]/text-expander/textarea').send_keys(text.get('notes'))
    driver.find_element_by_xpath('//*[@id="column-12657769"]/div[1]/div[2]/form[1]/text-expander/textarea').send_keys(Keys.ENTER)
    time.sleep(0.1)

    driver.find_element_by_xpath('//*[@id="column-12657769"]/div[1]/div[2]/form[1]/div/button[1]').click()
    print(f"App for {text.get('input_name')} is complete. GREAT WORK, YOU!")

if __name__ == '__main__':
    login()
    make_job_card()
    print('*** Bot is closing in 5 seconds... ***')
    print('REMINDER: Fill out card for submitted apps today!')
    time.sleep(5)
    driver.close()
    
