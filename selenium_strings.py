# this file includes different string arguments that are
# used by selenium to find elements while browing, they
# are given descriptive names to deduce the element(s) they represent

# URL for FTCU bank online portal
bank_url = 'https://firsttechfed.com'

# selector for button which sends user to login page
login_page_selector = "//a[@aria-label='Online Banking Login Link']"

# selector for login form submission button
login_form_selector = "//button[@type='submit']"

# selector for button to view checking account
checking_account_selector = "//ul[@aria-label='Checking Account']/li/a/div/div/h4"

# selector for filter toggle drop down menu
filter_toggle_selector = "//a[@id='filter_toggle']"

# ID selectors for username and password form fields
user_id = 'UserName'
password_id = 'Password'

# ID selector for button to load more transactions
load_more_transactions_id = 'load-more-transactions'

# ID selector for date input box
date_input_selector = 'date'

# ID selector for button to filter transactions
submit_search_button_selector = 'submit-search'

# class selector for the amounts of each transaction
transaction_amount_selector = "//div[contains(@class, 'amount trans-amount credit') or contains(@class, 'amount trans-amount debit')]"
# class selector for the names of the merchants for each transaction
merchant_names_selector = "//div[@class='transaction-details']/div[@class='details']/span[@class='description multi-2']"

# class selector for the date components of each transaction
date_month_selector = "//div[@class='transaction-details']/div[@class='date']/span[@class='month']"
date_day_selector = "//div[@class='transaction-details']/div[@class='date']/span[@class='day']"
date_year_selector = "//div[@class='transaction-details']/div[@class='date']/span[@class='year']"
