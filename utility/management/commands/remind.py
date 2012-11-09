import datetime
import smtplib
import string

from user_profile.models import UserProfile
from show.models import Show, Performer

from django.conf import settings
from django.core import management
from django.core.management.base import BaseCommand

carrier_mapping = dict()
carrier_mapping['VZ'] = 'vtext.com'
carrier_mapping['AT'] = 'txt.att.net'
carrier_mapping['SP'] = ''
carrier_mapping['TM'] = 'tmomail.com'

FROMADDR = "mmoutenot@gmail.com"
LOGIN    = FROMADDR
PASSWORD = "7ucan$am.S07"

def send_text_reminder(server, performer):
  user = performer.user
  user_profile = user.get_profile()
  role = performer.get_role_display()

  print "Reminding %s for role %s" % (str(user), str(role))

  carrier = user_profile.carrier
  phone_number = user_profile.phone_number

  SUBJECT = "YOU GOT A TRUNK SHOW DOOD"
  TO = string.join("%s@%s" % (phone_number, carrier_mapping[carrier]))
  TOS = [TO]
  # TOS = ["mmoutenot@gmail.com"]
  FROM = "mmoutenot@gmail.com"
  msg = ("From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n"
                % (FROM, ", ".join(TOS), SUBJECT) )
  msg += "You've got a show tomorrow and you are %s" % str(role)

  server.sendmail(FROM, TOS, msg)

  print "sending reminder"


  print "reminder sent"


class Command(BaseCommand):
  option_list = BaseCommand.option_list

  def handle(self, *args, **options):

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.set_debuglevel(1)
    server.ehlo()
    server.starttls()
    server.login(LOGIN, PASSWORD)

    print "\tconnected to mail server"

    # get tomorrows show
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    upcoming_shows = Show.objects.filter(date=tomorrow)
    print upcoming_shows
    for show in upcoming_shows:
      performers = show.performers.all()
      print performers

      for performer in performers:
        send_text_reminder(server, performer)

    server.quit()


