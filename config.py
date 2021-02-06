# VitalSource login credentials
login_email = "email@gmail.com"
login_password = "password"

# VitalSource links
login_url = "https://bookshelf.vitalsource.com/#/user/signin"   # VitalSource login URL
book_url = "https://bookshelf.vitalsource.com/#/books/xxxxxx"   # VitalSource book URL
total_pages = 100                                               # Total no of pages in book
book_name = "Book-Name"                                         # Book Name

# Progam flags
verbose_mode = True     # Toggle program output
min_page_size = 20      # Minimum file size of crawled page (in KB)
sleep_time = 10         # No of seconds to sleep to allow page to load completely
long_sleep_time = 120   # No of seconds to long sleep to allow manual CAPTCHA challenge completion

# Program files
gecko_driver_file = "selenium/geckodriver"  # Driver file path
media_folder = "media/"                     # Media folder path
verbose_file = "output.txt"                 # Output file if verbose mode set to False

# Email notification
outgoing_email = 'sender@gmail.com'     # Outgoing email address
outgoing_email_password = 'password'    # Outgoing email password
outgoing_email_name = "Sender"          # Outgoing email name
incoming_email = 'recipient@gmail.com'  # Incoming email address