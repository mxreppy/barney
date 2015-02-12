from django.db import models
from datetime import datetime
# from boto.sqs.message import RawMessage

from webform.queue.messages import post

# import json

# import needed to enumerate
import webform.receiver as receiver

print('webform receiver queue {}'.format(receiver.QUEUE))


# Create your models here.


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
        # m = RawMessage()
        # m.set_body(json.dumps(message_body))
        print("sending body {}".format(message_body))
        # non intuitive way to send messages via the receiver...
        # receiver.receive_message(m)

        post(message_type='validate_address', body=message_body)
        print('sent')
        pass
