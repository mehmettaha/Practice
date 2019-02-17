import os
import datetime
import shutil

#constants
filepath = "C:/beslenme"
template = "template.xlsx"

#make a file name with today's date
todays = datetime.date.today().strftime("%d.%m.%Y")
todays = todays + ".xlsx"

source = "{0}{1}{2}".format(filepath,"/",template)
destination = "{0}{1}{2}".format(filepath,"/",todays)

#copy template and rename with today's date if not exist
if todays not in os.listdir(filepath):
    shutil.copyfile(source,destination)

#open today's file 
os.system(destination)
    