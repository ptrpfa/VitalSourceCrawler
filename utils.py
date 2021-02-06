from termcolor import colored
from config import *
import smtplib                                  
from email.mime.text import MIMEText            
from email.mime.multipart import MIMEMultipart  
from email.header import Header                 
from email.utils import formataddr              
import os
import re

# Function to check for improperly crawled pages
def check_crawled_pages ():

    # Get list of crawled files
    list_files = os.listdir (media_folder)

    # Remove irrelevant files
    list_files.remove (".gitignore")

    # Initialise list containing improperly crawled pages
    list_incomplete = []

    # Loop through each file
    for file in list_files:

        # Get file path
        file_path = media_folder + file

        # Get file size (in KB)
        file_size = os.stat (file_path).st_size / 1024

        # Check if file size meets the minimum size defined
        if (file_size < min_page_size):

            # Set regex
            regex = '^%s-(\d+)\.png$' % book_name

            # Get file index
            index = int (re.match (regex, file).group (1)) - 1

            # Add file into list of improperly crawled pages
            list_incomplete.append (index)

    # Sort list
    list_incomplete.sort ()

    # Return list containing improperly crawled pages
    return list_incomplete

# Email function for sending email notifications regarding Pangaea program
def send_email_notification (send_to_email, subject, message):

    # Set email header
    msg = MIMEMultipart ()
    msg ['From'] = formataddr ((str (Header (outgoing_email_name, 'utf-8')), outgoing_email))
    msg ['To'] = send_to_email
    msg ['Subject'] = subject

    # Set email message
    msg.attach (MIMEText (message, 'html'))
    text = msg.as_string ()

    try:

        # Start SMTP server
        server = smtplib.SMTP ('smtp.gmail.com', 587)
        server.starttls ()

        # Login to server
        server.login (outgoing_email, outgoing_email_password)
        
        # Send email notification
        server.sendmail (outgoing_email, send_to_email, text)

        green ("Email notification sent to %s !" % incoming_email)

    except Exception as error:

        # Log exception/error
        red ("Exception occurred in send_email_notification () function: " + str (error))

    finally:

        # Close server regardless whether the email was sent successfully or not
        server.quit ()

# Functions for printing colored debugging messages
def red (text):

    # Check if program is operating in verbose mode or not
    if (not verbose_mode):

        with open (verbose_file, 'a') as vb:
            print (text, file = vb)

    else:

        print (colored (text, 'red'))

def yellow (text):

    # Check if program is operating in verbose mode or not
    if (not verbose_mode):

        with open (verbose_file, 'a') as vb:
            print (text, file = vb)

    else:

        print (colored (text, 'yellow'))

def green (text):

    # Check if program is operating in verbose mode or not
    if (not verbose_mode):

        with open (verbose_file, 'a') as vb:
            print (text, file = vb)

    else:

        print (colored (text, 'green'))

def blue (text):

    # Check if program is operating in verbose mode or not
    if (not verbose_mode):

        with open (verbose_file, 'a') as vb:
            print (text, file = vb)

    else:

        print (colored (text, 'blue'))

def magenta (text):

    # Check if program is operating in verbose mode or not
    if (not verbose_mode):

        with open (verbose_file, 'a') as vb:
            print (text, file = vb)

    else:
    
        print (colored (text, 'magenta'))

def cyan (text):

    # Check if program is operating in verbose mode or not
    if (not verbose_mode):

        with open (verbose_file, 'a') as vb:
            print (text, file = vb)

    else:

        print (colored (text, 'cyan'))

def white (text):

    # Check if program is operating in verbose mode or not
    if (not verbose_mode):

        with open (verbose_file, 'a') as vb:
            print (text, file = vb)

    else:

        print (colored (text, 'white'))