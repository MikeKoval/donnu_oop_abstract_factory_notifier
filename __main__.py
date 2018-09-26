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
        r = requests.post("https://hooks.slack.com/services/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", headers={'Content-type': 'application/json'}, data=json.dumps({"text":text}))
        print(r.status_code)


class SmsNotifier(AbstractNotifier):
    def send(self, text):
        account_sid = 'AC98f6c61030d962a9fbb9f98183acf314'
        auth_token = 'a3a7afadc4a5d15bb35c164145e297d3'
        client = Client(account_sid, auth_token)

        message = client.messages \
                .create(
                     body=text,
                     from_='+18507248985',
                     to='+380966852997'
                 )

        print(message.sid)

if (sys.argv[1] == 'sms'):
    notifier = SmsNotifier()
else:
    notifier = SlackNotifier()

notifier.send(sys.argv[2])