__author__ = 'mikey'

# from webform.queue.sqs import post as sqs_post
from webform.queue.rabbit import post as rabbit_post


def post(message_type='None', body=None):
    print('posting message type {} and body {}'.format(message_type, body))
    rabbit_post(message_type=message_type, body=body)

