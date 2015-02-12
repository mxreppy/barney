from django.db import models
from datetime import datetime

# from boto.sqs.message import RawMessage

from webform.queue.messages import post
from barney.settings import SQS_QUEUE


# import json

# import needed to enumerate the receiver queue system
# (may only be needed for the runreciever command)
import webform.receiver as receiver

print('webform receiver queue {}'.format(receiver.QUEUE))


class Order(models.Model):
    address = models.TextField(default='')
    plan = models.TextField(default='')
    validated_address = models.TextField(default='')
    sku = models.TextField(default='')

    def send_address_for_validation(self):
        message_body = {
            # 'message_type': 'validate_address',
            'order_id': self.id,
            'timestamp': datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
        }

        # Put the message in the queue
        print("sending body {}".format(message_body))

        # non intuitive way to send messages via the receiver...
        # also doesn't work currently, so not used

        # m = RawMessage()
        # m.set_body(json.dumps(message_body))
        # receiver.receive_message(m)

        post(message_type='validate_address', body=message_body)

        print('message sent')