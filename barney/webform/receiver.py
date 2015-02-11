from django_sqs import receiver
from datetime import datetime


@receiver("django-example-reppy")
def receive_message(msg):
    print('at {}, msg received: {}'.format(
        datetime.now().time(),
        msg.get_body()
    )
    )