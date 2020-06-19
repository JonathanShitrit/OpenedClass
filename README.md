# OpenedClass
A Python app deployed on Heroku that uses Selenium to notify you, via text message, when CUNY classes you want have an available seat. Test.py utilizes SMTPLIB module to send an email which is converted to sms via TMobile's sms gateway.


## Setup
1. Alter test.py and replace your gmail account info on lines 8 and 9
2. Use your corresponding carrier's sms gateway:
  * AT&T: [number]@txt.att.net
  * Sprint: [number]@messaging.sprintpcs.com or [number]@pm .sprint.com
  * T-Mobile: [number]@tmomail.net
  * Verizon: [number]@vtext.com
  * Boost Mobile: [number]@myboostmobile.com
  * Cricket: [number]@sms.mycricket.com
  * Metro PCS: [number]@mymetropcs.com
  * Tracfone: [number]@mmst5.tracfone.com
  * U.S. Cellular: [number]@email.uscc.net
  * Virgin Mobile: [number]@vmobl.com
3. In runner.py line 63 enter your real number
