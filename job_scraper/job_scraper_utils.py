from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

def configure_webdriver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    stealth(driver,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
            )
    return driver

def search_jobs(driver, country, job_position, job_location, date_posted):
    full_url = f"{country}/jobs?q={'+'.join(job_position.split())}&l={job_location}&fromage={date_posted}"
    print(f"Scraping URL: {full_url}")
    driver.get(full_url)

    try:
        job_count_element = driver.find_element(By.XPATH, '//div[starts-with(@class, "jobsearch-JobCountAndSortPane-jobCount")]')
        total_jobs = job_count_element.find_element(By.XPATH, './span').text
        print(f"Total jobs found: {total_jobs}")
    except NoSuchElementException:
        print("No job count element found.")
        total_jobs = "Unknown"

    return full_url, total_jobs

def scrape_job_data(driver, country):
    """Scrape job data from the currently loaded page in the driver."""
    df = pd.DataFrame(columns=['Link', 'Job Title', 'Company', 'Location'])
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    job_cards = soup.find_all('div', class_='job_seen_beacon')

    for job in job_cards:
        try:
            link = country + job.find('a', {'data-jk': True}).get('href')
        except AttributeError:
            link = None

        try:
            title = job.find('h2', {'class': 'jobTitle'}).text.strip()
        except AttributeError:
            title = None

        try:
            company = job.find('span', {'class': 'companyName'}).text.strip()
        except AttributeError:
            company = None

        try:
            location = job.find('div', {'class': 'companyLocation'}).text.strip()
        except AttributeError:
            location = None

        df = pd.concat([df, pd.DataFrame({'Link': [link], 'Job Title': [title], 'Company': [company], 'Location': [location]})], ignore_index=True)

    return df

def clean_data(df):
    """Clean the scraped job data DataFrame."""
    df = df.dropna()

    df = df.drop_duplicates(subset=['Link'])

    df = df.reset_index(drop=True)

    return df


def send_email(to_email, subject, body):
    """Send an email using SMTP."""
    email_host = os.getenv('EMAIL_HOST', 'smtp.gmail.com')
    email_port = int(os.getenv('EMAIL_PORT', 587))
    email_host_user = os.getenv('EMAIL_HOST_USER')
    email_host_password = os.getenv('EMAIL_HOST_PASSWORD')

    if not all([email_host_user, email_host_password]):
        raise ValueError("Email credentials are not properly set in environment variables.")

    msg = MIMEMultipart()
    msg['From'] = email_host_user
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP(email_host, email_port) as server:
            server.starttls()
            server.login(email_host_user, email_host_password)
            server.send_message(msg)
            print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")
        raise
    from django.shortcuts import render