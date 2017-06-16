#!/usr/bin/env python
import os 
import glob
import time



kellyProperties = ['St. Cloud Best Western Kelly Inn','Fargo 13 Kelly Inn','Bismarck Kelly Inn','Sante Fe Best Western','Minot Best Western Kelly Inn','West Des Moines Staybridge Suites','Sioux Falls SW Holiday Inn Express','Sioux Falls Staybridge Suites','Sioux Falls LaQuinta','Empire Towers Best Western','Empire Holiday Inn Express','West Yellowstone Clubhouse Inn','The Cody Hotel','Billings LaQuinta','Billings Best Western Kelly Inn','Billings Kelly Inn','Yankton Best Western Kelly Inn','Omaha Best Western Kelly Inn','Mitchell Kelly Inn','Fargo 44 Best Western Kelly Inn', 'West Yellowstone Kelly Inn', 'Yellowstone Westgate']




#this is the secret sauce !!! x = '*% s*' % (edem1)
movedFiles = "kellyIn/"
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
  if eval2 in kellyProperties:
    y = '*% s*' % (x)#this gets every file for each hotel
    filenames = glob.glob(y)# gets each mp3, MP3, and xls, for just that call. 
    fn = "    ".join(str(a) for a in filenames)
    print fn
    fn = []

#this is the secret sauce !!! x = '*% s*' % (edem1)
movedFiles = "kellyIn/"
list2 = glob.glob("*mp3")
list3 = glob.glob("*MP3")
list4 = list2+list3
xls = ".xls"
mp3 = ".mp3"
MP3 = ".MP3"
for idem in list4:#this bit gets at the dict key from every file name
  if 'Call' in idem:
    eval2=idem.partition("Call")
  else:
    eval2=idem.partition("Group")#shortens each filename
  eval2=eval2[0]
  eval2=eval2.strip()
  x = idem.rstrip(mp3)
  x = idem.rstrip(MP3)
  if eval2 in kellyProperties:
    y = '*% s*' % (x)#this gets every file for each hotel
    filenames = glob.glob(y)# gets each mp3, MP3, and xls, for just that call. 
    fn = "    ".join(str(a) for a in filenames)
    print fn
    fn = []
  



