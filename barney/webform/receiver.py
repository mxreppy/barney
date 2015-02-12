from django_sqs import receiver
from datetime import datetime

from webform.models import Order
import json

QUEUE="django-example-reppy2"

@receiver(QUEUE)
def receive_message(msg):
    print('at {}, msg received: {}'.format(
        datetime.now().time(),
        msg.get_body()
    )
    )

    try:
        _dict = json.loads(msg.get_body())

        order = Order.objects.get(id=_dict['order_id'])

        order.validated_address = 'address validated at {}'.format(
            datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
        )
        order.save()
        print('address validated')
    except Exception as e:
        print('unable to process message {}, error {}'.format(
            msg.get_body(),
            e)
        )

        raise

