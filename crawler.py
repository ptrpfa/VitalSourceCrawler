from config import *
from utils import *
from selenium.webdriver import Firefox  
from selenium.webdriver.firefox.options import Options 
from time import sleep

# Initialise selenium
opts = Options ()    
browser = Firefox (executable_path = gecko_driver_file, options = opts) 
browser.maximize_window()
browser.implicitly_wait(30) # Wait up till 30 seconds to find elements

""" Login to VitalSource """
yellow ("Logging in to VitalSource..")

# Browse to login URL
browser.get (login_url)

# Accept VitalSource cookies
browser.find_element_by_class_name ("gDqDTR").click ()

# Enter user credentials
browser.find_element_by_xpath ("//input[@type='email']").send_keys (login_email)
browser.find_element_by_xpath ("//input[@type='password']").send_keys (login_password)
browser.find_element_by_class_name ("KaEKF").click ()
green ("Successfully logged in to VitalSource!\n")

""" Crawl previously improperly crawled pages """
yellow ("Checking for improperly crawled pages..")

# Get pages that have been improperly crawled previously, if any
list_incomplete = check_crawled_pages ()

# Loop through each improperly crawled page
for page in list_incomplete:

    # Set book url
    current_url = "%s/cfi/%s!" % (book_url, page)

    magenta ("\nCrawling page %s / %s (%s)" % (page + 1, total_pages, current_url))

    # Browse to book url
    browser.get (current_url)

    # Set sleeping time
    if (list_incomplete.index (page) == 0):
        sleeping_time = long_sleep_time         # Set sleep time to be longer for first page being crawled (to allow manual input to bypass CAPTCHA)
    else:
        sleeping_time = sleep_time

    # Sleep to let current page load/bypass CAPTCHA challenge
    cyan ("Sleeping for %ss to let page load..\n" % sleeping_time)
    sleep (sleeping_time)

    yellow ("Crawling page..")

    # Toggle to book's iframe
    iframe = browser.find_elements_by_tag_name ('iframe')
    browser.switch_to.frame (iframe [1])

    # Toggle to book content
    book_content = browser.find_element_by_id ('epub-content')
    browser.switch_to.frame (book_content)
    
    # Set current page's filename
    filename = "%s%s-%s.png" % (media_folder, book_name, page + 1)

    # Get a screenshot of the current page
    browser.find_element_by_tag_name ('body').screenshot (filename)
    green ("Page %s / %s current saved at %s" % (page + 1, total_pages, filename))

green ("\nFinished crawling previously improperly crawled pages!!\n")

# Initialise index
current_index = 0                       # Current index of page no being crawled (this needs to be updated after every 100+ pages have been crawled due to CAPTCHA challenge)
copy_current_index = current_index      # Copy of current index variable (to toggle longer sleep time)

# Loop until end of book
while (current_index < total_pages):

    # Set book url
    current_url = "%s/cfi/%s!" % (book_url, current_index)

    magenta ("\nCrawling page %s / %s (%s)" % (current_index + 1, total_pages, current_url))

    # Browse to book url
    browser.get (current_url)

    # Set sleeping time
    if (current_index == copy_current_index):
        sleeping_time = long_sleep_time     # Set sleep time to be longer for first page being crawled (to allow manual input to bypass CAPTCHA)
    else:
        sleeping_time = sleep_time

    # Sleep to let current page load
    cyan ("Sleeping for %ss to let page load..\n" % sleeping_time)
    sleep (sleeping_time)

    yellow ("Crawling page..")

    # Toggle to book's iframe
    iframe = browser.find_elements_by_tag_name ('iframe')
    browser.switch_to.frame (iframe [1])

    # Toggle to book content
    book_content = browser.find_element_by_id ('epub-content')
    browser.switch_to.frame (book_content)
    
    # Set current page's filename
    filename = "%s%s-%s.png" % (media_folder, book_name, current_index + 1)

    # Get a screenshot of the current page
    browser.find_element_by_tag_name ('body').screenshot (filename)
    green ("Page %s / %s current saved at %s" % (current_index + 1, total_pages, filename))

    # Increment current index
    current_index = current_index + 1

green ("\nEnd of Crawling!\n")

# Send email to notify user upon end of crawling
send_email_notification (incoming_email, "%s crawl status" % book_name, "Book successfully crawled!!")

# End of program
green ("End of Program!")