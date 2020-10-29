# OpenedClas
A Python app deployed on Heroku that uses Selenium to notify you, via text message, when CUNY classes you want have an available seat. Sms.py utilizes gmail email server and their SMTPLIB module to send an email which is converted to sms on TMobile's sms gateway.


## Setup
1. Alter sms.py and replace your gmail account info on lines 8 and 9
2. On line 16 use your corresponding carrier's sms gateway:
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
3. In functions.py line 49 enter your real number
4. Run with `python3 runner.py`

### Run Remotely on Heroku (optional)
1. A great guide on how to get started with python and selenium on heroku https://www.youtube.com/watch?v=Ven-pqwk3ec 
