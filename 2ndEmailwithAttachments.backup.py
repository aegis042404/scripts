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
   for file in filenames:
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

#emailDict = {'david': ['aegis4244@gmail.com', 'aegis042404@gmail.com', 'abby@starperformanceinc.com'], 'abby': ''}


emailDict = {u'Craftsman Inn': ['powens@craftsmaninn.com', 'amoyer@craftsmaninn.com'], u'Osceola Quality Inn': 'pcpatel222@gmail.com', u'St. Cloud GrandStay': ['andyp@blueskyhospitalityllc.com','ginab@blueskyhospitalityllc.com','jennab@blueskyhospitalityllc.com','stcloud@grandstay.net'],  u'Marina Inn': ['crinker@marina-inn.com', 'rbobian@marina-inn.com', 'lrainey@marina-inn.com'], u'Stillwater GrandStay': ['stillwater@grandstay.net','andyp@blueskyhospitalityllc.com', 'ginab@blueskyhospitalityllc.com','jennab@blueskyhospitalityllc.com'] ,u'Grand Ely Resort': ['bill@mhgmn.com', 'kirk@mhgmn.com','mary@grandelylodge.com'], u'Bridgewood Best Western Premier':['rydove@bwneenah.com', 'rich@rbhospitality.com','jvanburen@bwneenah.com'], u'St. Cloud Best Western Kelly Inn': 'mlaughlin@kellyinns.com', u'Chandler Fairfield Inn & Suites':['lsaron@ncghotels.com'], u'Westwood Shores': ['foremostmgt@yahoo.com','wwsmgr@gmail.com'], u'Woodcliff Hotel & Spa': 'fgrabosky@woodcliffhotelspa.com', u'Pine Ridge Inn':'', u'Sauk Centre AmericInn': 'pdurbin@americinnsaukcentre.com', u'Fort Collins AmericInn': ['cwroge@trhospitality.com','fortcollinssouth.co@americinn.com', 'jcincoski@trhospitality.com'], u'West Des Moines Hampton Inn': ['jholman@ncghotels.com'], u'Woodspring Suites Pleasant Hill': 'gm.pleasanthillws@gmail.com', u'Newport Resort': ['foremostmgt@yahoo.com','sandy@newportresort.com','stay@newportresort.com'], u'West Yellowstone Westgate': 'jgideon@kellyinns.com', u'Rockford Hampton Inn': ['hamptonrockford@gmail.com'], u'Middleton Fairfield Inn & Suites': ['abuck@ncghotels.com','cduhr@ncghotels.com'], u'Anamosa AmericInn': ['anamosa.ia@americinn.com','jcincoski@trhospitality.com','pmchenry@trhospitality.com'], u'West Des Moines Staybridge Suites': 'jhill@kellyinns.com', u'Fairfield AmericInn': ['fairfield.ia@americinn.com','jcincoski@trhospitality.com','pmchenry@trhospitality.com'], u'Woodspring Suites Ankeny': '', u'Aberdeen Best Western Ramkota Inn': ['frontdesk@aberdeenramkota.net','gkueter@regency-mgmt.com','manager@aberdeenramkota.net','tbiegler@regency-mgmt.com'], u'Chandler Courtyard': ['lsaron@ncghotels.com'], u'Yankton Best Western Kelly Inn': 'shaberman@kellyinns.com', u'Bloomington Staybridge Suites': 'gm@ssbloomington.com', u'Austin Holiday Inn': 'gm@hiaustin.com', u'Griswold AmericInn':['cwroge@trhospitality.com','griswold.ct@americinn.com','jcincoski@trhospitality.com'], u'Happy Valley Homewood Suites': ['kpuntar@ncghotels.com','rmckenzie@ncghotels.com','tjohnson@ncghotels.com'], u'Nicollet Inn Best Western PLUS': 'jeff@nicolletinn.com', u'Sioux Falls LaQuinta': 'lq6598gm@laquinta.com', u'Beaumont Days Inn': ['bcirlot@amliberty.com','ckaplan@amliberty.com',' scolvin@amliberty.com'], u'Willmar Holiday Inn Express': 'gm@willmarhotels.com', u'Sioux Falls Staybridge Suites': 'sfstaybridge@midconetwork.com', u'Alexandria AmericInn': ['alexandria.mn@americinn.com','andyp@blueskyhospitalityllc.com','ginab@blueskyhospitalityllc.com','litchfield.mn@americinn.com','jennab@blueskyhospitalityllc.com'], u'Gateway Grand Best Western PLUS': 'gm@gatewaygrand.com', u'Hueston Woods Lodge': ['gkueter@regency-mgmt.com','mvanwinkle@huestonwoodslodge.com','tarvan@huestonwoodslodge.com'], u'AT&T Executive Education and Conference Center': 'craig.millar@attconf.utexas.edu', u'LaVista Hampton Inn & Suites': ['cgruber@ncghotels.com','gsobetski@ncghotels.com'], u'La Crosse GrandStay': ['lacrosse@grandstay.net','robin@birchlakehospitality.com'], u'West Yellowstone Kelly Inn': 'dshill@kellyinns.com', u'Alexandria Holiday Inn': ['bill@mhgmn.com','guestservices@hialexandria.com','kbehn@hialexandria.com','kirk@mhgmn.com'], u'Mount Pleasant AmericInn': 'mountpleasant.ia@americinn.com', u'Sioux Falls SW Holiday Inn Express': 'fsdsf@midconetwork.com', u'Chan AmericInn': ['chanhassen.mn@americinn.com','cwroge@trhospitality.com','jcincoski@trhospitality.com'], u'Cambridge Crossings Inn': ['andyp@blueskyhospitalityllc.com','cambridgecrossings@gmail.com','ginab@blueskyhospitalityllc.com','jennab@blueskyhospitalityllc.com'], u'Austin Days Inn': 'gm@hiaustin.com', u'Hartford AmericInn': ['hartford.sd@americinn.com','jcincoski@trhospitality.com','pmchenry@trhospitality.com'], u'Rapid City Comfort Inn': ['davisdathe@gmail.com','dianeheinis@gmail.com'], u'Lincoln Sands Best Western PLUS': 'nathanc@lincolnandassociates.com', u'Happy Valley Courtyard': ['celam@ncghotels.com'], u'Westchase Best Western PLUS': ['bcirlot@amliberty.com','ckaplan@amliberty.com','lcortes@amliberty.com','tom@starperformanceinc.com'], u'Bloomington West Holiday Inn Express': ['bill@mhgmn.com','kirk@mhgmn.com','agm@hiexbloomington.com'], u'Rochester Springhill Suites': 'gm@springhillrochester.com', u'Cypress Bend Resort': ['bcirlot@amliberty.com','rrolland@amliberty.com','ckaplan@amliberty.com','madison.sepulvado@cypressbend.com','gary.grant@cypressbend.com','tom@starperformanceinc.com'], u'Eagan Staybridge Suites': 'gm@sseagan.com', u'Astoria Lincoln Inn': 'dawnd@lincolnandassociates.com', u'Alexandria Arrowwood Resort': ['gkueter@regency-mgmt.com','jwild@arrowwoodresort.com','khemming@arrowwoodresort.com','kchisholm@arrowwoodresort.com'], u'Ramsey Comfort Suites': ['gm.mn404@choicehotels.com','andyp@blueskyhospitalityllc.com','ginab@blueskyhospitalityllc.com','gm.mn054@choicehotels.com','jennab@blueskyhospitalityllc.com'], u'Plymouth Crowne Plaza': [' gina.bannenberg@cpplymouth.com','gkueter@regency-mgmt.com','jeanette.bigelow@cpplymouth.com','mark.Olson@cpplymouth.com'], u'Rapid City GrandStay Residential': ['rapidcity@grandstay.net','robin@birchlakehospitality.com'], u'Bismarck Best Western Ramkota Hotel': ['dachtenberg@ramkotabismarck.com','gkueter@regency-mgmt.com','mark.Olson@cpplymouth.com'], u'Sun Valley AmericInn': 'hailey.id@americinn.com', u'Oklahoma City Airport AmericInn': ['jcincoski@trhospitality.com','okcairport.ok@americinn.com','handerson@trhospitality.com'], u'Roseville Holiday Inn Express': 'gm@hixroseville.com', u'Casper Best Western Ramkota': ['casperfom@ramkotacasper.com','dachtenberg@ramkotabismarck.com','dachtenberg@ramkotabismarck.com','gkueter@regency-mgmt.com','gm@ramkotacasper.com','reservations@ramkotacasper.com'], u'Maple Grove Hilton Garden Inn': ['MSeverson@ncghotels.com'], u'Muscatine AmericInn': 'muscatine.ia@americinn.com', u'Happy Valley Hampton Inn & Suites': ['kpuntar@ncghotels.com','rmckenzie@ncghotels.com'], u'Yakima Comfort Suites': 'conniew@lincolnandassociates.com', u'Naples Staybridge Suites': 'gm@ssnaples.com', u'Aspen Select Hotel': ['agm@rmnhotel.com','gkueter@regency-mgmt.com','gm@rmnhotel.com','mark.Olson@cpplymouth.com'], u'Shoreview Hilton Garden Inn': 'gm@hiltonshoreview.com', u'Fairmont Holiday Inn': 'gm@hifairmont.com', u'Boardwalk Comfort Inn': 'tanyag@lincolnandassociates.com', u'Fairmont Quality Inn': 'gm@hifairmont.com', u'Billings LaQuinta': 'lq6635gm@laquinta.com', u'Rochester Courtyard': 'gm@courtyardrochester.com', u'St. Cloud Quality Inn': ['andyp@blueskyhospitalityllc.com','ginab@blueskyhospitalityllc.com','gm.mn404@choicehotels.com','jennab@blueskyhospitalityllc.com'], u'Fargo Country Inn & Suites': 'brad.renslow@countryinns.com', u'Shoreview Best Western': 'gm@bestwesternshoreview.com', u'Eau Claire GrandStay Residential': ['eauclaire@grandstay.net','robin@birchlakehospitality.com'], u'Willmar Best Western PLUS': 'gm@willmarhotels.com', u'Seaside Holiday Inn Express': 'lawandaj@lincolnandassociates.com', u'Valley City AmericInn': 'manager@valleycityamericinn.com', u'Osage AmericInn': ['jcincoski@trhospitality.com','osage.ia@americinn.com','pmchenry@trhospitality.com'], u'Sibley AmericInn': ['jcincoski@trhospitality.com','pmchenry@trhospitality.com','sibley.ia@americinn.com'], u'Country Inn & Suites Woodbury': ['gm@ciwoodbury.com','jbhakta@jrhospitality.com'], u'Watertown Best Western Ramkota Inn': ['ccormier@ramkotawtn.com','gkueter@regency-mgmt.com','jan@ramkotasf.com','dstanley@ramkota.com'], u'Bemidji AmericInn': 'manager@americinnbemidji.com', u'Des Moines Airport AmericInn': 'desmoinesairport.ia@americinn.com', u'Jackson Cabot Lodge': ['ecox@mmihg.com','msturdivant@mmihg.com','smay@mmihg.com','ssledge@mmihg.com'], u'Fargo 13 Kelly Inn': 'bmcgavin@kellyinns.com', u'Bismarck AmericInn': 'manager@americinnbismarck.com', u'Shawnee Lodge': ['gkueter@regency-mgmt.com','tstevens@shawneeparklodge.com',' rmcintire@shawneeparklodge.com','tarvan@huestonwoodslodge.com'], u'Ames GrandStay': ['ames@grandstay.net','robin@birchlakehospitality.com'], u'Bloomington AmericInn': ['bloomingtonwest.mn@americinn.com','jcincoski@trhospitality.com', 'handerson@trhospitality.com'], u'Kearney AmericInn': ['jcincoski@trhospitality.com','kearney.ne@americinn.com','handerson@trhospitality.com'], u'Fort Dodge AmericInn': ['fortdodge.ia@americinn.com','jcincoski@trhospitality.com','pmchenry@trhospitality.com'], u'Oshkosh Waterfront Hotel': ['dschetter@bwoshkosh.com','rich@rbhospitality.com','rjensen@bwoshkosh.com'], u'Fargo Inn & Suites': 'manager@fargoinn.com', u'Rapid City Comfort Suites': ['davisdathe@gmail.com','dianeheinis@gmail.com'], u'Maple Grove Hampton Inn': 'gm@hamptoninnmaplegrove.com', u'Augusta Riverwalk Baymont Inn & Suites': ['krkondur@aol.com','tom@starperformanceinc.com'], u'Fairmont Hampton Inn': 'gm@hifairmont.com', u'Willmar Country Inn & Suites': 'gm@countryinnwillmar.com', u'DeWitt AmericInn': ['Dewitt.ia@americinn.com','pmchenry@trhospitality.com','jcincoski@trhospitality.com'], u'Rockford Hilton Garden Inn': ['nwidstrom@ncghotels.com','ressman@ncghotels.com','sstraka@ncghotels.com'], u'Milsaps Cabot Lodge': ['hburt@mmihg.com','msturdivant@mmihg.com','rroe@mmihg.com','ssledge@mmihg.com'], u'Minot Country Inn & Suites': 'cheryl.stanley@countryinns.com', u'East Towne Mall Hampton Inn': ['mnevins@ncghotels.com','pmattsson-boze@ncghotels.com'], u'Elms Hotel & Spa': 'jmormino@elmshotelandspa.com', u'Madison East Fairfield Inn & Suites': ['jstewart@ncghotels.com','jbrotz@ncghotels.com'], u'Rochester Guesthouse Inn & Suites': 'manager@rochesterlodging.net', u'Mankato Hilton Garden Inn': ['david.reyna@hilton.com','gkueter@regency-mgmt.com','mark.Olson@cpplymouth.com','steve.tacheny@hilton.com','tbiegler@regency-mgmt.com'], u'Maple Grove Staybridge Suites': 'gm@ssmaplegrove.com', u'Deadwood Lodge': ['gkueter@regency-mgmt.com','jschmaltz@custerresorts.com','agalbraith@deadwoodlodge.com','sberreth@deadwoodlodge.com'], u'Fargo South 45 AmericInn': 'smiller@americinnfargo.com', u'Empire Towers Best Western': 'empiretowers@midconetwork.com', u'Wyndham Garden Sebastian St. Augustine': 'manager@sebastianhotel.com', u'Empire Holiday Inn Express': 'hiexp@midconetwork.com', u'Rochester Homewood Suites': 'gm@homewoodrochester.com', u'Middleton Courtyard': ['jerskine@ncghotels.com','lknutson@ncghotels.com'], u'Newton Super 8': 'super8newton@live.com', u'Marshalltown Comfort Inn': 'gm.comfortinnmarshalltown@gmail.com', u'Schaumburg AmericInn': ['jcincoski@trhospitality.com',' schaumburg.il@americInn.com','handerson@trhospitality.com'], u'Fargo West Acres AmericInn': 'lellefson@americinnfargo.com', u'Worthington AmericInn': ['cwroge@trhospitality.com','jcincoski@trhospitality.com','worthington.mn@americinn.com'], u'Madison West Hampton Inn & Suites': ['mbubela@ncghotels.com','MNightAudit@ncghotels.com','sbracken@ncghotels.com','ttenhagen@ncghotels.com'], u'Minnetonka Hampton Inn': 'gm@hamptonminnetonka.com', u'Baldwin AmericInn': ['baldwin.wi@americinn.com','jcincoski@trhospitality.com','pmchenry@trhospitality.com'], u'Valley City GrandStay': 'valleycity@grandstay.net', u'Roseville Hampton Inn': 'gm@hamptonroseville.com', u'Appleton Hampton Inn': ['ahart@ncghotels.com','rkliment@ncghotels.com'], u'Newton AmericInn': ['jcincoski@trhospitality.com','newton.ia@americinn.com','pmchenry@trhospitality.com'], u'Eagan Hilton Garden Inn': 'gm@hiltoneagan.com', u'Park Place Inn': ['aparker@park-place-hotel.com','gkueter@regency-mgmt.com','jwild@arrowwoodresort.com','fom@park-place-hotel.com'], u'Baudette AmericInn': 'americinnlow@mncable.net', u'Best Western Augusta West': '', u'Scottsdale North Hilton Garden Inn': ['mrocha@ncghotels.com','tjohnson@ncghotels.com'], u'Rochester Aspen Suites': ['agm@rmnhotel.com','gkueter@regency-mgmt.com','gm@rmnhotel.com','mark.Olson@cpplymouth.com'], u'Ellensburg Lincoln Inn': 'tims@lincolnandassociates.com', u'Fallon Best Western': 'h.gandhi@bwfallon.com', u'Sheyboygan GrandStay': ['sheboygan@grandstay.net','robin@birchlakehospitality.com'], u'Pierre Clubhouse Hotel & Suites': ['gkueter@regency-mgmt.com','jan@ramkotasf.com','rmickelson@clubhouse-hotel.com','tallerdings@clubhouse-hotel.com'], u'The Cody Hotel': 'cwatson@thecody.com', u'Rockford Fairfield Inn & Suites': ['hbraem@ncghotels.com','nwidstrom@ncghotels.com'], u'Invoices for Coaches': '', u'Evaluations and Audio Files': '', u'Bismarck Kelly Inn': 'gm.bismarck@kellyinns.com', u'New Brighton Homewood Suites': 'gm@homewoodnb.com', u'Cedar Shore Resort': ['gkueter@regency-mgmt.com','jschmaltz@rapidnet.com','nikki@cedarshore.com','ron@cedarshore.com'], u'Beaumont Howard Johnson': ['bcirlot@amliberty.com','ckaplan@amliberty.com','scolvin@amliberty.com'], u'Glendale Hampton Inn & Suites': ['jdunkin@ncghotels.com'], u'Litchfield AmericInn': ['andyp@blueskyhospitalityllc.com','ginab@blueskyhospitalityllc.com','jennab@blueskyhospitalityllc.com','litchfield.mn@americinn.com'], u'Madison East Courtyard': ['ehoerl@ncghotels.com', 'alove@ncghotels.com','jryan@ncghotels.com'], u'Mandan Comfort Inn & Suites': 'manager@comfortinnmandan.com', u'Albuquerque Clubhouse Inn & Suites': ['gkueter@regency-mgmt.com','tkosel@clubhouseinn.com'], u'Seville Plaza Best Western PLUS': 'jacibw@gmail.com', u'Minot Best Western Kelly Inn': 'adelorme@kellyinns.com', u'Tualatin Comfort Inn': 'paulh@lincolnandassociates.com', u'Middleton Residence Inn': ['aschelling@ncghotels.com','cduhr@ncghotels.com'], u'St. Louis Park Homewood Suites': 'gm@homewoodslp.com', u'Avondale Courtyard': ['icaldwell-saar@ncghotels.com'], u'Fergus Falls AmericInn': 'manager@americinnfergusfalls.com', u'Fort Myers Pierview Hotel': 'gm@pierviewhotelfmb.com', u'Golden Valley Holiday Inn Express': 'gm@higoldenvalley.com', u'Morris GrandStay': ['andyp@blueskyhospitalityllc.com','jennab@blueskyhospitalityllc.com','morris@grandstay.net'], u'New Ulm Best Western PLUS': 'gm@bestwesternnewulm.com', u'Fargo Clubhouse Inn & Suites': ['chughes@clubhousefargo.com','jan@ramkotasf.com'], u'Bismarck Radisson': ['gkueter@regency-mgmt.com','sam.radisson@midconetwork.com','fom.radisson@midconetwork.com','frontdesk.radisson@outlook.com', 'jason.radisson@midconetwork.com', 'dachtenberg@ramkotabismarck.com'], u'Paynesville Inn & Suites': 'ptaplah@paynesvilleinn.com', u'Johnston AmericInn': 'johnston.ia@americinn.com', u'Bloomington Hilton Garden Inn': 'gm@hiltonbloomington.com', u'Happy Valley Residence Inn': ['celam@ncghotels.com','tjohnson@ncghotels.com'], u'Billings Best Western Kelly Inn': 'rjbratland@kellyinns.com', u'Lakeville Holiday Inn': ['andy@hilakeville.com'], u'Madison West Homewood Suites': ['bdoksus@ncghotels.com','churt@ncghotels.com','sbracken@ncghotels.com'], u'Sioux Falls Best Western Ramkota': ['gkueter@regency-mgmt.com','jan@ramkotasf.com','patrick@ramkotasf.com'], u'Tea GrandStay': ['andyp@blueskyhospitalityllc.com','jennab@blueskyhospitalityllc.com','tea@grandstay.net'], u'Billings Kelly Inn': 'sfield@kellyinns.com', u'Copperleaf Boutique Hotel & Spa': ['debj@copperleafhotel.com', 'rich@rbhospitality.com'], u'Sioux Falls Clubhouse Inn': ['gkueter@regency-mgmt.com','jan@ramkotasf.com','vcarman@clubhouse-hotel.com'], u'St. Cloud AmericInn': 'manager@americinnstcloud.com', u'Omaha Best Western Kelly Inn': ['cbroer@kellyinns.com','dwollman@kellyinns.com','rgalliger@kellyinns.com'], u'Moses Lake Comfort Suites': 'adamb@lincolnandassociates.com', u'Okoboji Arrowwood Resort': ['gm@arrowwoodokoboji.com', 'arrowwoodfom@arrowwoodokoboji.com'], u'Brainerd Lakes Arrowwood': ['carolyn.bare@arrowwoodbrainerd.com','gkueter@regency-mgmt.com','jwild@arrowwoodresort.com','shawn.kobs@arrowwoodbrainerd.com'], u'Omaha AmericInn': ['jcincoski@trhospitality.com','omaha.ne@americinn.com','handerson@trhospitality.com'], u'Maple Grove Courtyard': 'gm@courtyardmaplegrove.com', u'Ankeny Quality Inn': 'gm.ia182@choicehotels.com', u'Bloomington Best Western Plus': ['bbolduc@bestwesternbloomington.com','gkueter@regency-mgmt.com','mark.Olson@cpplymouth.com','mlewis@bestwesternbloomington.com','tbiegler@regency-mgmt.com'], u'Killeen Hawthorne Suites': ['bcirlot@amliberty.com','bshaw@amliberty.com','ckaplan@amliberty.com','tom@starperformanceinc.com'], u'Omak Lake Inn': ['khara@peppertreeinns.com','omakgm@peppertreeinns.com','valerie@peppertreeinns.com'], u'Killeen Days Inn': ['bcirlot@amliberty.com','bshaw@amliberty.com','ckaplan@amliberty.com','tom@starperformanceinc.com'], u'Eagan Hampton Inn': ['ndahl@ncghotels.com','kpeters@ncghotels.com', 'rlanoux@ncghotels.com'], u'Fargo 44 Best Western Kelly Inn': ['dwollman@kellyinns.com','lamann@kellyinns.com','rgalliger@kellyinns.com'], u'Sante Fe Best Western': 'jnygaard@kellyinns.com', u'Mitchell Kelly Inn': 'dhalder@kellyinns.com', u'Willmar Days Inn': 'gm@willmarhotels.com', u'Rapid City Best Western Ramkota': ['gkueter@regency-mgmt.com','jschmaltz@custerresorts.com','mlamphere@ramkotarc.com','vswenson@ramkotarc.com'], u'Spokane BW Peppertree': ['spokaneairportgm@peppertreeinns.com','valerie@peppertreeinns.com'], u'Ankeny AmericInn': 'ankeny.ia@americinn.com', u'Home2 Suites Glendale':['irodriguez@ncghotels.com'], u'Chandler Home2 Suites': ['kmorton@ncghotels.com'], u'Fairmont Super 8': 'gm@hifairmont.com', u'Pierre Ramkota Inn': ['gkueter@regency-mgmt.com','jan@ramkotasf.com','manager@pierreramkota.com','reservations@pierreramkota.com','agm@pierreramkota.com'], u'Indianapolis AmericInn': ['cwroge@trhospitality.com','jcincoski@trhospitality.com','Indyne.in@americinn.com'], u'Landmark Best Western PLUS': 'teresa_munoz@acihotels.com', u'Roseville Home2 Suites': 'gm@home2suitesroseville.com', u'Becker Crossings Inn': ['andyp@blueskyhospitalityllc.com','becker@crossingsinn.com','ginab@blueskyhospitalityllc.com','jennab@blueskyhospitalityllc.com'], u'Burr Oak Lodge': ['bmayle@stayburroak.com','dclark@stayburroak.com','gkueter@regency-mgmt.com','tarvan@huestonwoodslodge.com'], u'Brookfield Hampton Inn': ['djohnson@ncghotels.com'], u'Bloomington Hampton Inn': 'gm@hamptoninnbloomington.com', u'West Yellowstone Clubhouse Inn': 'jschoenhard@kellyinns.com', u'Rapid City Days Inn': 'blodgettpam@gmail.com', u'Walla Walla Holiday Inn Express': 'jenniferp@lincolnandassociates.com', u'Altoona Best Western': 'gm@bwaltoonainn.com',  u'Altoona Comfort Inn': 'gm.altoonacomfortinn@gmail.com', u'Bridges Bay Resort': ['gm@bridgesbayresort.com', 'operations@bridgesbayresort.com','arrowwoodsales@arrowwoodokoboji.com','gkueter@regency-mgmt.com','jan@ramkotasf.com'], u'Middleton Hilton Garden Inn': ['callen@ncghotels.com'], u'Two Harbors AmericInn': ['jcincoski@trhospitality.com','pmchenry@trhospitality.com','twoharbors.mn@americinn.com'], u'Topeka Clubhouse Inn & Suites': ['gkueter@regency-mgmt.com'], u'Maple Grove Holiday Inn & Waterpark': 'gm@himaplegrove.com'}

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
	print filenames
	#Set up users for email
	recipient = emailDict[eval2]
	print recipient
	if emailDict[eval2] != "" and len(filenames) == 2:
		mail(recipient,"Your New Star Performance Evaluations and Audio","Your newest Star Performance evaluation and audio are attached.",filenames)
		for z in filenames:
			idems = emailedFiles+z
			print z, idems
			os.rename(z,idems)
			str1 = ' '.join(recipient)
			print>>thefile, str1 + " " + z + " "+ timestamp



#Set up crap for the attachments
#files = "/tmp/test/dbfiles"
#filenames = [os.path.join(files, f) for f in os.listdir(files)]
#print filenames




#Create Module
def mail(to, subject, text, attach):
   msg = MIMEMultipart()
   msg['From'] = gmail_user
   msg['To'] = ", ".join(recipient)
   msg['Subject'] = subject

   msg.attach(MIMEText(text))

   #get all the attachments
   for file in filenames:
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

#send it
#mail(recipient,
 #  "Your New Star Performance Evaluations and Audio",
  # "Your newest Star Performance evaluation and audio are attached.",
  # filenames)

