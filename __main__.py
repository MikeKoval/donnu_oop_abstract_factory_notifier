from twilio.rest import Client
import requests
import json
import sys
import abc

class AbstractNotifier(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def send(self, text):
        pass

class SlackNotifier(AbstractNotifier):
    def send(self, text):
        r = requests.post("", headers={'Content-type': 'application/json'}, data=json.dumps({"text":text}))
        print(r.status_code)


class SmsNotifier(AbstractNotifier):
    def send(self, text):
        account_sid = ''
        auth_token = ''
        client = Client(account_sid, auth_token)

        message = client.messages \
                .create(
                     body=text,
                     from_='',
                     to=''
                 )

        print(message.sid)

if (sys.argv[1] == 'sms'):
    notifier = SmsNotifier()
else:
    notifier = SlackNotifier()

notifier.send(sys.argv[2])
