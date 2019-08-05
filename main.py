from transaction_collector import *
from data_upload import *

def main():
    # check credentials provided
    if len(sys.argv) < 3:
        print("no credentials provided, got following arguments: ", sys.argv)
        browser.quit()
        return
    login(sys.argv[1], sys.argv[2])
    upload_file()
    browser.quit()


if __name__ == '__main__':
    main()
