#!/usr/bin/env python
import os 
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage
from email.MIMEBase import MIMEBase
from email import Encoders
import glob
import time

#Create Module
def mail(to, subject, text, attach):
   msg = MIMEMultipart()
   msg['From'] = gmail_user
   msg['To'] = ", ".join(recipient)
   msg['Subject'] = subject

   msg.attach(MIMEText(text))

   #get all the attachments
   for file in none:
      part = MIMEBase('application', 'octet-stream')
      part.set_payload(open(file, 'rb').read())
      Encoders.encode_base64(part)
      part.add_header('Content-Disposition', 'attachment; filename="%s"' % file)
      msg.attach(part)

   mailServer = smtplib.SMTP("smtp.gmail.com", 587)
   mailServer.ehlo()
   mailServer.starttls()
   mailServer.ehlo()
   mailServer.login(gmail_user, gmail_pwd)
   mailServer.sendmail(gmail_user, to, msg.as_string())
   # Should be mailServer.quit(), but that crashes...
   mailServer.close()



dawn = ['St. Cloud Best Western Kelly Inn','Fargo 13 Kelly Inn','Bismarck Kelly Inn','Sante Fe Best Western','Minot Best Western Kelly Inn','West Des Moines Staybridge Suites']
tom = ['Sioux Falls SW Holiday Inn Express','Sioux Falls Staybridge Suites','Sioux Falls LaQuinta','Empire Towers Best Western','Empire Holiday Inn Express']
jeff = ['West Yellowstone Clubhouse Inn','The Cody Hotel','Billings LaQuinta','Billings Best Western Kelly Inn','Billings Kelly Inn', 'West Yellowstone Kelly Inn', 'Yellowstone Westgate']
dave = ['Yankton Best Western Kelly Inn','Omaha Best Western Kelly Inn','Mitchell Kelly Inn','Fargo 44 Best Western Kelly Inn']
none = []



#run 1 for dawn
#this is the secret sauce !!! x = '*% s*' % (edem1)
emailed = "emailed"
t = time.localtime()
timestamp = time.strftime('%b-%d-%Y_%H%M', t)
timestr = time.strftime("%Y%m")+emailed
thefile = open(timestr, 'a+')
emailedFiles = "emailed/"
gmail_user = "evaluations@starperformanceinc.com"
gmail_pwd = "lemondesk834"
list1 = glob.glob("*xls")
xls = ".xls"
for idem in list1:#this bit gets at the dict key from every file name
  if 'Call' in idem:
    eval2=idem.partition("Call")
  else:
    eval2=idem.partition("Group")#shortens each filename
  eval2=eval2[0]
  eval2=eval2.strip()
  x = idem.rstrip(xls)
  y = '*% s*' % (x)#this gets every file for each hotel
  filenames = glob.glob(y)# gets each mp3, MP3, and xls, for just that call. 
  fn = "    ".join(str(a) for a in filenames)
  print filenames
  #Set up users for email
  recipient = ["dkoble@kellyinns.com","rgalliger@kellyinns.com"]
  print recipient
  if eval2 in dawn:
    mail(recipient,"New Star Performance Evaluations and Audio on Google Drive",fn, none)
# if they want attachments
#mail(recipient,"New Star Performance Evaluations and Audio on Google Drive",filenames, filenames)

#run 2 for tom
fn = ""
filenames = []

#this is the secret sauce !!! x = '*% s*' % (edem1)
emailed = "emailed"
t = time.localtime()
timestamp = time.strftime('%b-%d-%Y_%H%M', t)
timestr = time.strftime("%Y%m")+emailed
thefile = open(timestr, 'a+')
emailedFiles = "emailed/"
gmail_user = "evaluations@starperformanceinc.com"
gmail_pwd = "lemondesk834"
list1 = glob.glob("*xls")
xls = ".xls"
for idem in list1:#this bit gets at the dict key from every file name
  if 'Call' in idem:
    eval2=idem.partition("Call")
  else:
    eval2=idem.partition("Group")#shortens each filename
  eval2=eval2[0]
  eval2=eval2.strip()
  x = idem.rstrip(xls)
  y = '*% s*' % (x)#this gets every file for each hotel
  filenames = glob.glob(y)# gets each mp3, MP3, and xls, for just that call. 
  fn = "    ".join(str(a) for a in filenames)
  print filenames
  #Set up users for email
  recipient = ["tmorris@kellyinns.com","rgalliger@kellyinns.com"]
  print recipient
  if eval2 in tom:
    mail(recipient,"New Star Performance Evaluations and Audio on Google Drive",fn, none)

#run 3 for jeff
fn = ""
filenames = []

#this is the secret sauce !!! x = '*% s*' % (edem1)
emailed = "emailed"
t = time.localtime()
timestamp = time.strftime('%b-%d-%Y_%H%M', t)
timestr = time.strftime("%Y%m")+emailed
thefile = open(timestr, 'a+')
emailedFiles = "emailed/"
gmail_user = "evaluations@starperformanceinc.com"
gmail_pwd = "lemondesk834"
list1 = glob.glob("*xls")
xls = ".xls"
for idem in list1:#this bit gets at the dict key from every file name
  if 'Call' in idem:
    eval2=idem.partition("Call")
  else:
    eval2=idem.partition("Group")#shortens each filename
  eval2=eval2[0]
  eval2=eval2.strip()
  x = idem.rstrip(xls)
  y = '*% s*' % (x)#this gets every file for each hotel
  filenames = glob.glob(y)# gets each mp3, MP3, and xls, for just that call. 
  fn = "    ".join(str(a) for a in filenames)
  print filenames
  #Set up users for email
  recipient = ["jschoenhard@kellyinns.com","rgalliger@kellyinns.com"]
  print recipient
  if eval2 in jeff:
    mail(recipient,"New Star Performance Evaluations and Audio on Google Drive",fn, none)

#run 4 for dave
fn = ""
filenames = []

#this is the secret sauce !!! x = '*% s*' % (edem1)
emailed = "emailed"
t = time.localtime()
timestamp = time.strftime('%b-%d-%Y_%H%M', t)
timestr = time.strftime("%Y%m")+emailed
thefile = open(timestr, 'a+')
emailedFiles = "emailed/"
gmail_user = "evaluations@starperformanceinc.com"
gmail_pwd = "lemondesk834"
list1 = glob.glob("*xls")
xls = ".xls"
for idem in list1:#this bit gets at the dict key from every file name
  if 'Call' in idem:
    eval2=idem.partition("Call")
  else:
    eval2=idem.partition("Group")#shortens each filename
  eval2=eval2[0]
  eval2=eval2.strip()
  x = idem.rstrip(xls)
  y = '*% s*' % (x)#this gets every file for each hotel
  filenames = glob.glob(y)# gets each mp3, MP3, and xls, for just that call. 
  fn = "    ".join(str(a) for a in filenames)
  print filenames
  #Set up users for email
  recipient = ["dwollman@kellyinns.com","rgalliger@kellyinns.com"]
  print recipient
  if eval2 in dave:
    mail(recipient,"New Star Performance Evaluations and Audio on Google Drive",fn, none)




