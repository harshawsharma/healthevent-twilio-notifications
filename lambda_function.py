import logging
import os
from twilio.rest import Client


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def lambda_handler(event, context):
    logger.setLevel(logging.DEBUG)
    logger.debug("Event is --- %s" % event)
    message = str(event['detail']['eventDescription'][0]['latestDescription'] + "\n\nClick here for details:" + " https://phd.aws.amazon.com/phd/home?region=us-east-1#/event-log?eventID="+event['detail']['eventArn'])
    return send_message(message)

def send_message(message):

    #Get these credentials from http://twilio.com/user/account
    ACCOUNT_SID = os.environ['TWILIO_ACCOUNT_SID']
    AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(ACCOUNT_SID, AUTH_TOKEN)


    send = client.messages.create(to=os.environ['ToPhoneNo'],  # Any phone number
                                                    from_=os.environ['FromPhoneNo'],  # Must be a valid Twilio number
                                                    body=message
                                                    )
    logger.debug("Call_response is-- %s" % send)
