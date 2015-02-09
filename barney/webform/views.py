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


def home(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = OrderForm(request.POST)

        print(request.POST)

        # check whether it's valid:
        if form.is_valid():
            order = Order.objects.create()
            order.address = request.POST['address']
            order.plan = request.POST['plan']
            order.save()

            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = OrderForm()

    return render(request, 'home.html', {'form': form})