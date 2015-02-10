__author__ = 'mikey'
import boto
import json
from boto.sqs.message import RawMessage

# QUEUE_NAME = 'arn:aws:sqs:us-east-1:106715121600:django-example-reppy'
QUEUE_NAME = 'django-example-reppy'


def post(message_type='None', body=None):

    # Connect to SQS and open the queue
    sqs = boto.connect_sqs()
    # q = sqs.create_queue(QUEUE_NAME)
    my_queue = sqs.get_queue(QUEUE_NAME)
    body['message_type'] = message_type

    # Put the message in the queue
    m = RawMessage()
    m.set_body(json.dumps(body))
    status = my_queue.write(m)

    print("wrote to queue, status = '{}'".format(status))
