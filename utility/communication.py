import datetime
import smtplib
import string

from user_profile.models import UserProfile
from show.models import Show, Performer

carrier_mapping['VZ'] = 'vtext.com'
carrier_mapping['AT'] = 'txt.att.net'
carrier_mapping['SP'] = ''
carrier_mapping['TM'] = 'tmomail.com'

def remind_tomorrows_performers():
  # get tomorrows show
  upcoming_show = Show.objects.filter(date=datetime.date.tomorrow())
  performers = upcoming_show.performers.all()
  for performer in performers
    send_text_reminder(performer)

def send_text_reminder(performer)
  user = performer.user
  user_profile = user.get_profile()
  role = performer.get_role_display()

  carrier = user_profile.carrier
  phone_number = user_profile.phone_number

  SUBJECT = "YOU GOT A TRUNK SHOW DOOD"
  TO = string.join("%s%s", phone_number, carrier_mapping[carrier])
  FROM = "mmoutenot@gmail.com"
  BODY = string.join(("From: $s" % FROM,
                      "To: %s" % TO,
                      "Subject: %s" % SUBJECT,
                      "",
                      "You've got a show tomorrow and you are %s", role),
                     "\r\n")

  server = smtplib.SMTP(HOST)
  server.sendmail(FROM, [TO], BODY)
  server.quit()

