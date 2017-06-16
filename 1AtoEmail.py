#!/usr/bin/env python
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import glob
import os
import time

emailDict = {u'Spicer Hampton Inn': 'nancylarson@tpihospitality.com', u'Craftsman Inn':'',u'Woodspring Suites Ankeny': 'gm.ankenyws@gmail.com', u'Quality Inn Indianola': 'gm.qualityinnindianola@gmail.com', u'Osceola Quality Inn': 'pcpatel222@gmail.com', u'St. Cloud GrandStay': 'stcloud@grandstay.net', u'Marina Inn': '', u'Stillwater GrandStay': 'stillwater@grandstay.net', u'Grand Ely Resort': 'info@grandelylodge.com', u'Bridgewood Best Western Premier': '', u'St. Cloud Best Western Kelly Inn': 'mlaughlin@kellyinns.com', u'Chandler Fairfield Inn & Suites': '', u'Westwood Shores': '', u'Woodcliff Hotel & Spa': 'fgrabosky@woodcliffhotelspa.com', u'Pine Ridge Inn': '', u'Sauk Centre AmericInn': 'pdurbin@americinnsaukcentre.com', u'Fort Collins AmericInn': '', u'West Des Moines Hampton Inn': '', u'Woodspring Suites Pleasant Hill': 'gm.pleasanthillws@gmail.com', u'Newport Resort': '', u'West Yellowstone Westgate': 'jgideon@kellyinns.com', u'Rockford Hampton Inn': '', u'Middleton Fairfield Inn & Suites': '', u'Anamosa AmericInn': '', u'West Des Moines Staybridge Suites': 'jhill@kellyinns.com', u'Fairfield AmericInn': '', u'Aberdeen Best Western Ramkota Inn': '', u'Chandler Courtyard': '', u'Yankton Best Western Kelly Inn': 'shaberman@kellyinns.com', u'Bloomington Staybridge Suites': 'gm@ssbloomington.com', u'Austin Holiday Inn': 'gm@hiaustin.com', u'Griswold AmericInn': '', u'Happy Valley Homewood Suites': '', u'Nicollet Inn Best Western PLUS': 'jeff@nicolletinn.com', u'Sioux Falls LaQuinta': 'lq6598gm@laquinta.com', u'Beaumont Days Inn': '', u'Willmar Holiday Inn Express': 'gm@willmarhotels.com', u'Sioux Falls Staybridge Suites': 'sfstaybridge@midconetwork.com', u'Alexandria AmericInn': 'alexandria.mn@americinn.com', u'Gateway Grand Best Western PLUS': 'gm@gatewaygrand.com', u'Hueston Woods Lodge': '', u'AT&T Executive Education and Conference Center': 'craig.millar@attconf.utexas.edu', u'LaVista Hampton Inn & Suites': '', u'La Crosse GrandStay': '', u'West Yellowstone Kelly Inn': 'dshill@kellyinns.com', u'Alexandria Holiday Inn': '', u'Mount Pleasant AmericInn': 'mountpleasant.ia@americinn.com', u'Sioux Falls SW Holiday Inn Express': 'fsdsf@midconetwork.com', u'Chan AmericInn': '', u'Cambridge Crossings Inn': 'cambridge@crossingsinn.com', u'Austin Days Inn': 'gm@hiaustin.com', u'Hartford AmericInn': '', u'Rapid City Comfort Inn': '', u'Lincoln Sands Best Western PLUS': 'nathanc@lincolnandassociates.com', u'Happy Valley Courtyard': '', u'Westchase Best Western PLUS': '', u'Bloomington West Holiday Inn Express': '', u'Rochester Springhill Suites': 'gm@springhillrochester.com', u'Cypress Bend Resort': '', u'Eagan Staybridge Suites': 'gm@sseagan.com', u'Astoria Lincoln Inn': 'dawnd@lincolnandassociates.com', u'Alexandria Arrowwood Resort': '', u'Ramsey Comfort Suites': 'gm.mn054@choicehotels.com', u'Plymouth Crowne Plaza': '', u'Rapid City GrandStay Residential': '', u'Bismarck Best Western Ramkota Hotel': '', u'Sun Valley AmericInn': 'hailey.id@americinn.com', u'Oklahoma City Airport AmericInn': '', u'Roseville Holiday Inn Express': 'gm@hixroseville.com', u'Casper Best Western Ramkota': '', u'Maple Grove Hilton Garden Inn': '', u'Muscatine AmericInn': 'muscatine.ia@americinn.com', u'Happy Valley Hampton Inn & Suites': '', u'Yakima Comfort Suites': 'conniew@lincolnandassociates.com', u'Naples Staybridge Suites': 'gm@ssnaples.com', u'Aspen Select Hotel': '', u'Shoreview Hilton Garden Inn': 'gm@hiltonshoreview.com', u'Fairmont Holiday Inn': 'gm@hifairmont.com', u'Boardwalk Comfort Inn': 'tanyag@lincolnandassociates.com', u'Fairmont Quality Inn': 'gm@hifairmont.com', u'Billings LaQuinta': 'lq6635gm@laquinta.com', u'Rochester Courtyard': 'gm@courtyardrochester.com', u'St. Cloud Quality Inn': 'gm.mn404@choicehotels.com', u'Fargo Country Inn & Suites': 'brad.renslow@countryinns.com', u'Shoreview Best Western': 'gm@bestwesternshoreview.com', u'Eau Claire GrandStay Residential': '', u'Willmar Best Western PLUS': 'gm@willmarhotels.com', u'Seaside Holiday Inn Express': 'lawandaj@lincolnandassociates.com', u'Valley City AmericInn': 'manager@valleycityamericinn.com', u'Osage AmericInn': '', u'Sibley AmericInn': '', u'Country Inn & Suites Woodbury': '', u'Watertown Best Western Ramkota Inn': '', u'Bemidji AmericInn': 'manager@americinnbemidji.com', u'Des Moines Airport AmericInn': 'desmoinesairport.ia@americinn.com', u'Jackson Cabot Lodge': '', u'Fargo 13 Kelly Inn': 'bmcgavin@kellyinns.com', u'Bismarck AmericInn': 'manager@americinnbismarck.com', u'Shawnee Lodge': '', u'Ames GrandStay': '', u'Bloomington AmericInn': '', u'Kearney AmericInn': '', u'Fort Dodge AmericInn': '', u'Oshkosh Waterfront Hotel': '', u'Fargo Inn & Suites': 'manager@fargoinn.com', u'Rapid City Comfort Suites': '', u'Maple Grove Hampton Inn': 'gm@hamptoninnmaplegrove.com', u'Augusta Riverwalk Baymont Inn & Suites': '', u'Fairmont Hampton Inn': 'gm@hifairmont.com', u'Willmar Country Inn & Suites': 'gm@countryinnwillmar.com', u'DeWitt AmericInn': '', u'Rockford Hilton Garden Inn': '', u'Milsaps Cabot Lodge': '', u'Minot Country Inn & Suites':'', u'East Towne Mall Hampton Inn': '', u'Elms Hotel & Spa': 'jmormino@elmshotelandspa.com', u'Madison East Fairfield Inn & Suites': '', u'Rochester Guesthouse Inn & Suites': 'manager@rochesterlodging.net', u'Mankato Hilton Garden Inn': '', u'Maple Grove Staybridge Suites': 'gm@ssmaplegrove.com', u'Deadwood Lodge': '', u'Fargo South 45 AmericInn': 'smiller@americinnfargo.com', u'Empire Towers Best Western': 'empiretowers@midconetwork.com', u'TRYP St. Augustine': 'manager@sebastianhotel.com', u'Empire Holiday Inn Express': 'hiexp@midconetwork.com', u'Rochester Homewood Suites': 'gm@homewoodrochester.com', u'Middleton Courtyard': '', u'Newton Super 8': 'gm.super8newton@gmail.com', u'Marshalltown Comfort Inn': 'gm.comfortinnmarshalltown@gmail.com', u'Schaumburg AmericInn': '', u'Fargo West Acres AmericInn': 'lellefson@americinnfargo.com', u'Worthington AmericInn': '', u'Madison West Hampton Inn & Suites': '', u'Minnetonka Hampton Inn': 'gm@hamptonminnetonka.com', u'Baldwin AmericInn': '', u'Valley City GrandStay': 'valleycity@grandstay.net', u'Roseville Hampton Inn': 'gm@hamptonroseville.com', u'Appleton Hampton Inn': '', u'Newton AmericInn': '', u'Eagan Hilton Garden Inn': 'gm@hiltoneagan.com', u'Park Place Inn': '', u'Baudette AmericInn': 'americinnlow@mncable.net', u'Best Western Augusta West': 'krkondur@aol.com', u'Scottsdale North Hilton Garden Inn': '', u'Rochester Aspen Suites': '', u'Ellensburg Lincoln Inn': 'tims@lincolnandassociates.com', u'Fallon Best Western': 'h.gandhi@bwfallon.com', u'Sheyboygan GrandStay': '', u'Pierre Clubhouse Hotel & Suites': '', u'The Cody Hotel': 'cwatson@thecody.com', u'Rockford Fairfield Inn & Suites': '', u'Invoices for Coaches': '', u'Evaluations and Audio Files': '', u'Bismarck Kelly Inn': 'gmbismarck@kellyinns.com', u'New Brighton Homewood Suites': 'gm@homewoodnb.com', u'Cedar Shore Resort': '', u'Beaumont Howard Johnson': '', u'Glendale Hampton Inn & Suites': '', u'Litchfield AmericInn': 'litchfield.mn@americinn.com', u'Madison East Courtyard': '', u'Mandan Comfort Inn & Suites': 'manager@comfortinnmandan.com', u'Albuquerque Clubhouse Inn & Suites': '', u'Seville Plaza Best Western PLUS': 'jacibw@gmail.com', u'Minot Best Western Kelly Inn': 'adelorme@kellyinns.com', u'Tualatin Comfort Inn': 'paulh@lincolnandassociates.com', u'Middleton Residence Inn': '', u'St. Louis Park Homewood Suites': 'gm@homewoodslp.com', u'Avondale Courtyard': '', u'Fergus Falls AmericInn': 'manager@americinnfergusfalls.com', u'Fort Myers Pierview Hotel': 'gm@pierviewhotelfmb.com', u'Golden Valley Holiday Inn Express': 'gm@higoldenvalley.com', u'Morris GrandStay': 'morris@grandstay.net', u'New Ulm Best Western PLUS': 'gm@bestwesternnewulm.com', u'Fargo Clubhouse Inn & Suites': '', u'Bismarck Radisson': '', u'Paynesville Inn & Suites': 'ptaplah@paynesvilleinn.com', u'Johnston AmericInn': 'johnston.ia@americinn.com', u'Bloomington Hilton Garden Inn': 'gm@hiltonbloomington.com', u'Happy Valley Residence Inn': '', u'Billings Best Western Kelly Inn': 'bwbillings@kellyinns.com', u'Lakeville Holiday Inn': '', u'Madison West Homewood Suites': '', u'Sioux Falls Best Western Ramkota': '', u'Tea GrandStay': 'tea@grandstay.net', u'Billings Kelly Inn': 'sfield@kellyinns.com', u'Copperleaf Boutique Hotel & Spa': '', u'Sioux Falls Clubhouse Inn': '', u'St. Cloud AmericInn': 'manager@americinnstcloud.com', u'Omaha Best Western Kelly Inn': 'cbroer@kellyinns.com', u'Moses Lake Comfort Suites': 'adamb@lincolnandassociates.com', u'Okoboji Arrowwood Resort': '', u'Brainerd Lakes Arrowwood': '', u'Omaha AmericInn': '', u'Maple Grove Courtyard': 'gm@courtyardmaplegrove.com', u'Ankeny Quality Inn': 'gm.ia182@choicehotels.com', u'Bloomington Best Western Plus': '', u'Killeen Hawthorne Suites': '', u'Omak Lake Inn': '', u'Killeen Days Inn': '', u'Eagan Hampton Inn': '', u'Fargo 44 Best Western Kelly Inn': 'lamann@kellyinns.com', u'Sante Fe Best Western': 'jnygaard@kellyinns.com', u'Mitchell Kelly Inn': 'dhalder@kellyinns.com', u'Willmar Days Inn': 'gm@willmarhotels.com', u'Rapid City Best Western Ramkota': '', u'Spokane BW Peppertree': '', u'Ankeny AmericInn': 'ankeny.ia@americinn.com', u'Chandler Home2 Suites': '', u'Fairmont Super 8': 'gm@hifairmont.com', u'Pierre Ramkota Inn': '', u'Indianapolis AmericInn': '', u'Landmark Best Western PLUS': 'teresa_munoz@acihotels.com', u'Roseville Home2 Suites': 'gm@home2suitesroseville.com', u'Becker Crossings Inn': 'becker@crossingsinn.com', u'Burr Oak Lodge': '', u'Brookfield Hampton Inn': '', u'Bloomington Hampton Inn': 'gm@hamptoninnbloomington.com', u'West Yellowstone Clubhouse Inn': 'jschoenhard@kellyinns.com', u'Rapid City Days Inn': 'blodgettpam@gmail.com', u'Walla Walla Holiday Inn Express': 'jenniferp@lincolnandassociates.com', u'Altoona Best Western': 'gm@bwaltoonainn.com',  u'Altoona Comfort Inn': 'gm.altoonacomfortinn@gmail.com', u'Bridges Bay Resort': '', u'Middleton Hilton Garden Inn': '', u'Two Harbors AmericInn': '', u'Topeka Clubhouse Inn & Suites': '', u'Maple Grove Holiday Inn & Waterpark': 'gm@himaplegrove.com'}

shortlist = []
#emailDict = {'david': 'aegis4244@gmail.com', 'abby': ''}
list1 = glob.glob("*xls")
emailed = "emailed"
t = time.localtime()
timestamp = time.strftime('%b-%d-%Y_%H%M', t)
timestr = time.strftime("%Y%m")+emailed
thefile = open(timestr, 'a+')
emailedFiles = "emailed/"
for idem in list1:#this bit gets at the dict key from every file name
	if 'Call' in idem:
		eval2=idem.partition("Call")
	else:
		eval2=idem.partition("Group")#shortens each filename
	eval2=eval2[0]
	eval2=eval2.strip()
	if emailDict[eval2] != "":
		toaddr = emailDict[eval2]
		print eval2, toaddr
		shortlist.append(toaddr)
		idems = emailedFiles+idem
		fromaddr = "evaluations@starperformanceinc.com"
		msg = MIMEMultipart()
		msg['From'] = fromaddr
		msg['To'] = toaddr
		msg['Subject'] = "New evaluations and audio are available"
		body = "Your newest Star Performance evaluation and audio are available on your Google Drive."
		msg.attach(MIMEText(body, 'plain'))
		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.starttls()
		server.login(fromaddr, "lemondesk834")
		text = msg.as_string()
		server.sendmail(fromaddr, toaddr, text)
		server.quit()
		idems = emailedFiles+idem
		print idem, idems
		os.rename(idem,idems)
		print>>thefile, toaddr + " " + idem + " " + timestamp













