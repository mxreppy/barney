__author__ = 'mikey'
import boto
import json
from boto.sqs.message import RawMessage

from webform.receiver import QUEUE


def post(message_type='None', body=None):

    # Connect to SQS and open the queue
    sqs = boto.connect_sqs()
    my_queue = sqs.get_queue(QUEUE)

    body['message_type'] = message_type

    # Put the message in the queue
    m = RawMessage()
    m.set_body(json.dumps(body))
    status = my_queue.write(m)

    print("wrote to queue, status = '{}'".format(status))
