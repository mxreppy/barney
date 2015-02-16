__author__ = 'mikey'

import json
import pika
from datetime import datetime

# from ..barney.settings import SQS_QUEUE as QUEUE
# in venv, run directly as python3 weform/rabbit_listen.py

QUEUE = "django-example-reppy3"

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


def callback(ch, method, properties, body):
    body_dict = json.loads(body.decode('utf-8'))
    now = datetime.utcnow()
    print(" [x] rabbit listen at %s Received %r" % (
        now.time(),
        body_dict,
    ))

    # setting, cheap and sleazy isotime
    # 'timestamp': datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ')

    send_time = datetime.strptime(
        body_dict.get('timestamp', ''),
        '%Y-%m-%dT%H:%M:%S.%fZ'
    )

    delta = now - send_time

    print("message send+receive delta {}".format(
        delta)
    )


channel.basic_consume(callback,
                      queue=QUEUE,
                      no_ack=True)

print(' [*] Waiting for messages on {}. To exit press CTRL+C'.format(QUEUE))
channel.start_consuming()