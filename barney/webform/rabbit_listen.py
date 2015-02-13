__author__ = 'mikey'

import pika
from datetime import datetime

# from ..barney.settings import SQS_QUEUE as QUEUE

QUEUE = "django-example-reppy2"

connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        'localhost')
)
channel = connection.channel()
channel.queue_declare(queue=QUEUE)


def callback(ch, method, properties, body):
    print(" [x] rabbit listen at %s Received %r" % (
        datetime.now().time(),
        body,
    ))


channel.basic_consume(callback,
                      queue=QUEUE,
                      no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()