# Program for combining PNG images crawled from VitalSource into a single PDF file
# NOTE: There may be limitations set by PIL on the number of images it can combine and export into a single PDF file.
#       As such, you may choose to export your images into multiple PDFs and combine them into a single PDF in the end.

from PIL import Image
import os
from config import *
import re
from natsort import natsorted

# Get list of all images in media folder
list_images = os.listdir (media_folder)
list_images.remove ('.gitignore')

""" Convert PNG images to JPEG """
# Create subfolder in media folder
os.mkdir (media_folder + 'jpg')

# Convert PNG images in media folder into JPEG
print ("Converting PNG images into JPEG..")

for image in list_images [1:]:
    pil_image = Image.open (media_folder + image)
    file_name = "%sjpg/%s.jpg" % (media_folder, re.match (r'(.+)\.png', image).group (1))
    pil_image.convert ('RGB').save (file_name, format = 'JPEG', quality = 100, optimize = True)

print ("PNG images successfully converted into JPEG!")

""" Convert JPEG images into PDF """
jpg_folder = media_folder + 'jpg/'
list_images = os.listdir (jpg_folder)
list_images = natsorted (list_images)
base_image = Image.open (jpg_folder + list_images [0])
addition_list = []

for image in list_images [1:]:
    p_image = Image.open (jpg_folder + image)
    p_image_copy = p_image.copy ()
    addition_list.append (p_image_copy)
    p_image.close ()

# Convert pages into PDF
base_image.save ('combined.pdf', "PDF", resolution=100.0, save_all = True, append_images = addition_list)

print ("Images successfully converted into PDF!")