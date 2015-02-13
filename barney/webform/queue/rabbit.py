__author__ = 'mikey'
import pika

from barney.settings import SQS_QUEUE as QUEUE

import json


def post(message_type='None', body=None):
    body['message_type'] = message_type

    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            'localhost')
    )
    channel = connection.channel()
    channel.queue_declare(queue=QUEUE)

    channel.basic_publish(
        exchange='',
        routing_key=QUEUE,
        body=json.dumps(body)
    )

    connection.close()

    print("wrote to rabbit queue {}".format(QUEUE))


