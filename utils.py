def found(browser, item, name):
    if item is None:
        print("can not find the ", name, " element")
        browser.quit()
        return False
    return True

month_dict = {'JAN': '1',
              'FEB': '2',
              'MAR': '3',
              'APR': '4',
              'MAY': '5',
              'JUN': '6',
              'JUL': '7',
              'AUG': '8',
              'SEP': '9',
              'OCT': '10',
              'NOV': '11',
              'DEC': '12'}
