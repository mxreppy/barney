from django.shortcuts import render
from django.http import HttpResponseRedirect

from webform.forms import OrderForm
from webform.models import Order

from webform.queue.messages import post as message_post

# Create your views here.


def home1(request):
    print("in home")

    if request.method == 'POST':
        print("Posting address {} and plan {}".format(
            request.POST['address'],
            request.POST['plan'])
        )

        order = Order.objects.create()
        order.address = request.POST['address']
        order.plan = request.POST['plan']
        order.save()

        print('saved')

        return render(
            request,
            'home.html',
            {
                'order': order
            }
        )
    else:
        return render(request, 'home.html')


def home(request, order_id=None):

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        if order_id is None:
            order = Order.objects.create()
        else:
            order = Order.objects.get(id=order_id)
        # create a form instance and populate it with data from the request:
        form = OrderForm(request.POST)

        if form.is_valid():
            order.address = request.POST['address']
            order.plan = request.POST['plan']
            order.save()

            order.send_address_for_validation()

            # message_post(
            #     message_type='validate_address',
            #     body={
            #         'address': order.address,
            #         'order_id': order.id
            #     }
            # )

            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            # TODO: reverse
            return HttpResponseRedirect('/order/{}/'.format(order.id))

    # if a GET (or any other method) we'll create a blank form
    else:
        if order_id is None:
            order = Order.objects.create()
        else:
            order = Order.objects.get(id=order_id)
        form = OrderForm(instance=order)

    return render(request, 'home.html', {'form': form, 'order': order})