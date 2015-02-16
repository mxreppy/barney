__author__ = 'mikey'
import pika

from barney.settings import SQS_QUEUE as QUEUE
from datetime import datetime
import json


def post(message_type='None', body=None):
    body['message_type'] = message_type

    print("start connection attempt to {} at {}".format(
        QUEUE,
        datetime.now().time())
    )

    try:
        credentials = pika.PlainCredentials('guest', 'guest')

        connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                host='rabbit.dev.nrgpl.us',
                port=5672,
                credentials=credentials,
                connection_attempts=5,
                # socket_timeout=1,  # seconds, I think...
            )
        )

        channel = connection.channel()
        channel.queue_declare(queue=QUEUE)

        channel.basic_publish(
            exchange='',
            routing_key=QUEUE,
            body=json.dumps(body)
        )

        connection.close()
        print("close connection attempt at {}".format(datetime.now().time()))

    except Exception as e:
        print("error at {}".format(datetime.now().time()))

        print("rabbit exception! {}".format(e))
        raise

    print("wrote to rabbit queue {}".format(QUEUE))


