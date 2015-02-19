from django.db import models
from datetime import datetime

# from boto.sqs.message import RawMessage

from webform.queue.messages import post as post_message


class Order(models.Model):
    address = models.TextField(default='')
    plan = models.TextField(default='')
    validated_address = models.TextField(default='')
    sku = models.TextField(default='')

    def send_address_for_validation(self):
        message_body = {
            'order_id': self.id,
            'timestamp': datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
        }

        # Put the message in the queue
        print("sending body {}".format(message_body))

        post_message(message_type='validate_address', body=message_body)

        print('message sent')