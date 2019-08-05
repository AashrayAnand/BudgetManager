# use sys to get optional arguments, time for sleeps,
# csv to write data to file
import sys, time, csv


# import the strings used by Selenium to find elements
from selenium_strings import *

# utility functions
from utils import *

# get datetime functions for setting time range
from datetime import date, timedelta

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from selenium.webdriver import FirefoxOptions

#opts = FirefoxOptions()
#opts.add_argument("--headless")

# create firefox browser drivers
browser = webdriver.Firefox()#options=opts)
date_today = date.today()
date_one_month_ago = date_today - timedelta(days=30)
date_today_str = str(date_today.month) + '/' + str(date_today.day) + '/' + str(date_today.year)
date_one_month_ago_str = str(date_one_month_ago.month) + '/' + str(date_one_month_ago.day) + '/' + str(date_one_month_ago.year)


# function to write scraped data to csv
def write_to_file(transaction_amounts, merchant_names, month_selector, day_selector, year_selector):
    items = [len(transaction_amounts), len(merchant_names), len(month_selector), len(day_selector), len(year_selector)]
    if max(items) != min(items):
        print("lists differ in length", transaction_amounts)
        browser.quit()
        return
    data = []
    for i in range(len(transaction_amounts)):
        row = [month_dict[month_selector[i]] + '/' + day_selector[i] + '/' + year_selector[i], merchant_names[i], transaction_amounts[i][2:]]
        data.append(row)
    with open("out.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["date", "merchant", "amount ($)"])
        writer.writerows(data)
# given an input set of credentials, logs browser into
# bank account
def login(user_argument, password_argument):
    # navigate to page
    browser.get(bank_url)

    # locate and click the login button
    login_page_button = browser.find_element_by_xpath(login_page_selector)
    if not found(browser, login_page_button, "button to reach login"):
        return
    login_page_button.click()
    time.sleep(3)

    # select elements of login form, fill them out and submit form,
    # user provided arguments used to authenticate
    username = browser.find_element_by_id(user_id)
    password = browser.find_element_by_id(password_id)
    if not found(browser, username, "username"):
        return
    if not found(browser, password, "password"):
        return

    # send credentials to form and submit
    username.send_keys(user_argument)
    password.send_keys(password_argument)
    login_submit_button = browser.find_element_by_xpath(login_form_selector)
    if not found(browser, login_submit_button, "button to submit login form"):
        return
    login_submit_button.click()
    filter_transactions()

def filter_transactions():
    time.sleep(8)
    checking_account = browser.find_element_by_xpath(checking_account_selector)
    if not found(browser, checking_account, "button to view checking account"):
        return
    checking_account.click()
    time.sleep(8)
    filter_toggle = browser.find_element_by_xpath(filter_toggle_selector)
    if not found(browser, filter_toggle, "button to filter transactions"):
        return
    filter_toggle.click()
    time.sleep(8)

    date_input = browser.find_element_by_id(date_input_selector)
    if not found(browser, date_input, "form field to filter by date"):
        return
    date_input.send_keys(date_one_month_ago_str + '-' + date_today_str)
    time.sleep(8)

    submit_search_button = browser.find_element_by_id(submit_search_button_selector)
    if not found(browser, submit_search_button, "button to search with filter"):
        return
    submit_search_button.click()
    time.sleep(8)

    # load all of the transactions by clicking button over and over
    save_transaction_data()

def save_transaction_data():
    load_more_transactions_button = browser.find_element_by_id(load_more_transactions_id)
    if not found(browser, load_more_transactions_button, "button to load more transactions"):
        return
    # repeatadly load transactions until all are displayed
    while load_more_transactions_button.is_displayed():
        load_more_transactions_button.click()
        time.sleep(5)
        load_more_transactions_button = browser.find_element_by_id(load_more_transactions_id)
        if not found(browser, load_more_transactions_button, "button to load more transactions"):
            return

    # scrape all of the information for each transactions,
    # they each consist of: [amount ($), merchant name, month, day, year]
    transaction_amounts = list(res.text for res in browser.find_elements_by_xpath(transaction_amount_selector))
    merchant_names = list(res.text for res in browser.find_elements_by_xpath(merchant_names_selector))
    month_selector = list(res.text for res in browser.find_elements_by_xpath(date_month_selector))
    day_selector = list(res.text for res in browser.find_elements_by_xpath(date_day_selector))
    year_selector = list(res.text for res in browser.find_elements_by_xpath(date_year_selector))

    # write the data to file
    write_to_file(transaction_amounts, merchant_names, month_selector, day_selector, year_selector)
