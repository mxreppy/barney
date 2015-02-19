from django_sqs import receiver
from datetime import datetime
from barney.settings import SQS_QUEUE

# circular
from webform.models import Order
import json

QUEUE = SQS_QUEUE

@receiver(QUEUE)
def receive_message(msg):
    # print('at {}, msg received: {}'.format(
    #     datetime.now().time(),
    #     msg.get_body()
    # )
    # )

    try:
        body_dict = json.loads(msg.get_body())

        now = datetime.utcnow()
        print(" [x] sqs listen at %s Received %r" % (
            now.time(),
            body_dict,
        ))

        # setting, cheap and sleazy isotime on the sending side
        # 'timestamp': datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
        send_time = datetime.strptime(
            body_dict.get('timestamp', ''),
            '%Y-%m-%dT%H:%M:%S.%fZ'
        )

        delta = now - send_time

        print("message send+receive delta {}".format(
            delta)
        )

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

