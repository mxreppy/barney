from django.shortcuts import render
from django.http import HttpResponseRedirect

from webform.forms import OrderForm
from webform.models import Order

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

    # if order_id is None and \
    #     request.method == 'POST' and \
    #         request.POST['id'] is not None:
    #     print(request.POST)
    #     order_id = request.POST['id']
    #     print("id is '{}'".format(order_id))
    #
    # if order_id is None:
    #     order = Order.objects.create()
    # else:
    #     order = Order.objects.get(id=order_id)

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        if order_id is None:
            order = Order.objects.create()
        else:
            order = Order.objects.get(id=order_id)
        # create a form instance and populate it with data from the request:
        form = OrderForm(request.POST)

        # print(request.POST)

        # check whether it's valid:
        if form.is_valid():
            order.address = request.POST['address']
            order.plan = request.POST['plan']
            order.save()

            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/order/{}/'.format(order.id))

    # if a GET (or any other method) we'll create a blank form
    else:
        if order_id is None:
            order = Order.objects.create()
        else:
            order = Order.objects.get(id=order_id)
        form = OrderForm(initial=order)

    return render(request, 'home.html', {'form': form, 'order': order})