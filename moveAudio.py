#!/usr/bin/env python
import glob
import os

match = []

emailed = "emailed/"
list2 = glob.glob("*.mp3")
list3 = glob.glob("*.MP3")
list4 = list2+list3
list1 = glob.glob("emailed/*xls")
for x in list1:
  x = x.replace(x[:8], '')
  x = x.rstrip(".xls")
  print x
  match.append(x)
print "match list ", match
for y in list4:
  if 'MP3' in y:
    z=y.partition(".MP3")
  if 'mp3' in y:
    z=y.partition(".mp3")
  z=z[0]
  z=z.strip()
  print "z is ", z
  if z in match:
    os.rename(y,emailed+y)
